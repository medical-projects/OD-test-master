from __future__ import print_function

import os
from termcolor import colored
import torch

from utils.args import args
import global_vars as Global
from datasets.NIH_Chest import NIHChestBinaryTest

if __name__ == '__main__':

    d2_tasks     = ['CIFAR10','UniformNoise', 'NormalNoise', 'MNIST', 'FashionMNIST', 'NotMNIST',  'CIFAR100', 'STL10', 'TinyImagenet']
    d3_tasks     = ['CIFAR10','UniformNoise', 'NormalNoise', 'MNIST', 'FashionMNIST', 'NotMNIST',  'CIFAR100', 'STL10', 'TinyImagenet']
    method_tasks     = [
                        'prob_threshold/0',
                        'odin/0',
                        ]

    # Construct the dataset cache
    ds_cache = {}
    D1 = NIHChestBinaryTest(root_path=os.path.join(args.root_path, 'NIHCC'))
    for m in [d2_tasks, d3_tasks]:
        for d in m:
            if not d in ds_cache:
                dataset = Global.all_datasets[d]
                if "name" in dataset.__dict__:
                    ds_cache[d] = dataset(root_path=os.path.join(args.root_path, dataset.name))
                else:
                    ds_cache[d] = dataset()

    results = []
    # If results exists already, just continue where left off.
    results_path = os.path.join(args.experiment_path, 'results.pth')
    if os.path.exists(results_path) and not args.force_run:
        print ("Loading previous checkpoint")
        results = torch.load(results_path)

    def has_done_before(method, d1, d2, d3):
        for m, ds, dm, dt, mid, a1, a2 in results:
            if m == method and ds == d1 and dm == d2 and dt == d3:
                return True
        return False


    args.D1 = 'NIHChest'
    for method in method_tasks:
        BT = Global.get_method(method, args)
        for d2 in d2_tasks:
            args.D2 = d2

            print ("Performing %s on %s vs. %s"%(colored(method, 'green'), colored('NIHChest', 'blue'), colored(d2, 'red')))

            ds1 = D1
            ds2 = ds_cache[args.D2]

            if not ds2.is_compatible(ds1):
                print ('%s is not compatible with %s, skipping.'%(colored(ds2.name, 'red'), colored(ds1.name, 'red')))
                continue

            if torch.ByteTensor(
                    [has_done_before(method, 'NIHChest', d2, d3) or not ds_cache[d3].is_compatible(ds1) or d2 == d3 for d3 in d3_tasks]
                ).all():
                continue

            valid_mixture = None

            if not method.startswith('binclass'):
                # Stage 1: Propose H
                d1_train = ds1.get_D1_train()
                BT.propose_H(d1_train)

                # Stage 2: Train for h \in H
                d1_valid = ds1.get_D1_valid()
                d2_valid = ds2.get_D2_valid(ds1)

                # Adjust the sizes.
                d1_valid_len = len(d1_valid)
                d2_valid_len = len(d2_valid)
                final_len = min(d1_valid_len, d2_valid_len)
                print("Adjusting %s and %s to %s"%(colored('D1=%d'%d1_valid_len, 'red'),
                                                colored('D2=%d'%d2_valid_len, 'red'),
                                                colored('Min=%d'%final_len, 'green')))
                d1_valid.trim_dataset(final_len)
                d2_valid.trim_dataset(final_len)
                valid_mixture = d1_valid + d2_valid
                print("Final valid size: %d+%d=%d"%(len(d1_valid), len(d2_valid), len(valid_mixture)))
            else:
                print(colored('Binary evaluation mode', 'red'))
                # There's no stage one; the method would do everything in the
                # second stage.

                # Get the first split. Overwrite the label
                d1_train = ds1.get_D1_train()
                d1_train.label = 0
                cls_name = d1_train.name

                # Stage 2: Train for h \in H
                d1_valid = ds1.get_D1_valid()
                d2_valid = ds2.get_D2_valid(ds1)

                # Adjust the sizes. Make sure this method does not see more valid data as other methods.
                d1_valid_len = len(d1_valid)
                d2_valid_len = len(d2_valid)
                final_len = min(d1_valid_len, d2_valid_len)
                print("Adjusting %s and %s to %s"%(colored('D1=%d'%d1_valid_len, 'red'),
                                                colored('D2=%d'%d2_valid_len, 'red'),
                                                colored('Min=%d'%final_len, 'green')))
                d1_valid.trim_dataset(final_len)
                d2_valid.trim_dataset(final_len)
                valid_mixture = d1_train + d1_valid + d2_valid

                print("Final valid size: %d+%d=%d"%(len(d1_valid), len(d2_valid), len(valid_mixture)))

            train_acc = BT.train_H(valid_mixture)

            for d3 in d3_tasks:
                args.D3 = d3

                if d2 == d3:
                    print (colored("Skipping, d2==d3", 'yellow'))
                    continue

                print ("Performing %s on %s vs. %s-%s"%(colored(method, 'green'), colored('NIHChest', 'blue'), colored(d2, 'red'), colored(d3, 'red')))

                if has_done_before(method, 'NIHChest', d2, d3):
                    print (colored("Skipped, has been done before.", 'yellow'))
                    continue

                ds3 = ds_cache[args.D3]

                if not ds3.is_compatible(ds1):
                    print ('%s is not compatible with %s, skipping.'
                            %(colored(ds3.name, 'red'),
                              colored(ds1.name, 'red')))
                    continue

                # Stage 3: Eval h on test data of d3
                d1_test = ds1.get_D1_test()
                d2_test = ds3.get_D2_test(ds1)

                # Adjust the sizes.
                d1_test_len = len(d1_test)
                d2_test_len = len(d2_test)
                final_len = min(d1_test_len, d2_test_len)
                print("Adjusting %s and %s to %s"%(colored('D1=%d'%d1_test_len, 'red'),
                                                colored('D2=%d'%d2_test_len, 'red'),
                                                colored('Min=%d'%final_len, 'green')))
                d1_test.trim_dataset(final_len)
                d2_test.trim_dataset(final_len)
                test_mixture = d1_test + d2_test
                print("Final test size: %d+%d=%d"%(len(d1_test), len(d2_test), len(test_mixture)))

                test_acc = BT.test_H(test_mixture)
                results.append((method, 'NIHChest', d2, d3, BT.method_identifier(), train_acc, test_acc))

                # Take a snapshot after each experiment.
                torch.save(results, results_path)

    for i, (m, ds, dm, dt, mi, a_train, a_test) in enumerate(results):
        print ('%d\t%s\t%15s\t%-15s\t%.2f%% / %.2f%%'%(i, m, '%s-%s'%(ds, dm), dt, a_train*100, a_test*100))
