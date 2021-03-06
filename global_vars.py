"""
    This file lists all the global variables that are used throughout the project.
    The two major components of this file are the list of the datasets and the list of the models.
"""

"""
    This is where we keep a reference to all the dataset classes in the project.
"""
import datasets.MNIST as MNIST
import datasets.FashionMNIST as FMNIST
import datasets.notMNIST as NMNIST
import datasets.CIFAR as CIFAR
import datasets.noise as noise
import datasets.STL as STL
import datasets.TinyImagenet as TI
import datasets.NIH_Chest as NC
import datasets.MURA as MU
import datasets.PADChest as PC
import datasets.malaria as mal
import datasets.ANHIR as ANH
import datasets.DRD as DRD
import datasets.DRIMDB as DRM
import datasets.IDC as IDC
import datasets.PCAM as PCAM
import datasets.RIGA as RIGA

all_dataset_classes = [ MNIST.MNIST, FMNIST.FashionMNIST, NMNIST.NotMNIST,
                        CIFAR.CIFAR10, CIFAR.CIFAR100,
                        STL.STL10, TI.TinyImagenet,
                        noise.UniformNoise, noise.NormalNoise,
                        STL.STL10d32, TI.TinyImagenetd32, NC.NIHChest, NC.NIHChestBinary, NC.NIHChestBinaryTest,
                        NC.NIHChestBinaryTrainSplit, NC.NIHChestBinaryValSplit, NC.NIHChestBinaryTestSplit, MU.MURA,
                        MU.MURAHAND, MU.MURAELBOW, MU.MURAFINGER, MU.MURAFOREARM, MU.MURAHUMERUS, MU.MURASHOULDER, MU.MURAWRIST,
                        PC.PADChest, PC.PADChestAP, PC.PADChestPA, PC.PADChestL, PC.PADChestAPHorizontal, PC.PADChestPED,
                        mal.Malaria, ANH.ANHIR, DRD.DRD, DRM.DRIMDB, IDC.IDC, PCAM.PCAM, PCAM.PCAMGray, RIGA.RIGA
                        ]

"""
    Not all the datasets can be used as a Dv, Dt (aka D2) for each dataset.
    The list below specifies which datasets can be used as the D2 for the other datasets.
    For instance, STL10 and CIFAR10 cannot face each other because they have 9 out 10 classes
    in common.
"""
d2_compatiblity = {
    # This can be used as d2 for            # this
    'MNIST': ['FashionMNIST', 'CIFAR10', 'CIFAR100', 'STL10', 'TinyImagenet', 'STL10d32', 'TinyImagenetd32', 'NIHCC',
              'NIHChestBinaryTest', 'NIHChestBinaryTrainSplit', 'PADChest', 'DRD', "PCAM"],
    'NotMNIST': ['MNIST', 'FashionMNIST', 'CIFAR10', 'CIFAR100', 'STL10', 'TinyImagenet', 'STL10d32', 'TinyImagenetd32',
                 'NIHCC', 'NIHChestBinaryTest', 'NIHChestBinaryTrainSplit', 'PADChest', 'DRD', "PCAM"],
    'FashionMNIST': ['MNIST', 'CIFAR10', 'CIFAR100', 'STL10', 'TinyImagenet', 'STL10d32', 'TinyImagenetd32', 'NIHCC',
                     'NIHChestBinaryTest', 'NIHChestBinaryTrainSplit', 'PADChest', 'DRD', "PCAM"],
    'CIFAR10': ['MNIST', 'FashionMNIST', 'CIFAR100', 'TinyImagenet', 'TinyImagenetd32', 'NIHCC', 'NIHChestBinaryTest',
                'NIHChestBinaryTrainSplit', 'PADChest', 'DRD', "PCAM"],
    'CIFAR100': ['MNIST', 'FashionMNIST', 'CIFAR10', 'STL10', 'TinyImagenet', 'STL10d32', 'TinyImagenetd32', 'NIHCC',
                 'NIHChestBinaryTest', 'NIHChestBinaryTrainSplit', 'PADChest', 'DRD', "PCAM"],
    'STL10': ['MNIST', 'FashionMNIST', 'CIFAR100', 'TinyImagenet', 'TinyImagenetd32', 'NIHCC', 'NIHCC',
              'NIHChestBinaryTrainSplit', 'PADChest', 'DRD', "PCAM"],
    'TinyImagenet': ['MNIST', 'FashionMNIST', 'CIFAR10', 'CIFAR100', 'STL10', 'STL10d32', 'NIHCC', 'NIHChestBinaryTest',
                     'NIHChestBinaryTrainSplit', 'PADChest', 'DRD', "PCAM"],
    'NIHChestBinary': ['MNIST', 'FashionMNIST', 'CIFAR10', 'CIFAR100', 'STL10', 'TinyImagenet', 'STL10d32',
                       'TinyImagenetd32', 'DRD', "PCAM"],
    'NIHCC': ['FashionMNIST', 'CIFAR10', 'CIFAR100', 'STL10', 'TinyImagenet', 'STL10d32', 'TinyImagenetd32', 'NIHCC',
              'DRD', "PCAM"],
    'NIHChestBinaryValSplit': ['FashionMNIST', 'CIFAR10', 'CIFAR100', 'STL10', 'TinyImagenet', 'STL10d32',
                               'TinyImagenetd32', 'NIHChestBinaryTrainSplit', 'DRD', "PCAM"],
    'MURA': ['NIHCC', 'PADChest'],
    'MURAHAND': ['NIHCC', 'PADChest'],
    'MURAWRIST': ['NIHCC', 'PADChest'],
    'MURAELBOW': ['NIHCC', 'PADChest'],
    'MURAFINGER': ['NIHCC', 'PADChest'],
    'MURAFOREARM': ['NIHCC', 'PADChest'],
    'MURAHUMERUS': ['NIHCC', 'PADChest'],
    'MURASHOULDER': ['NIHCC', 'PADChest'],
    'PADChest': ['NIHCC', 'PADChest'],
    'PADChestPA': ['NIHCC', 'PADChest'],
    'PADChestAP': ['NIHCC', 'PADChest'],
    'PADChestL': ['NIHCC', 'PADChest'],
    'PADChestAPHorizontal': ['NIHCC', 'PADChest'],
    'PADChestPED': ['NIHCC', 'PADChest'],
    'Malaria': ['PCAM', ],
    'ANHIR': ['PCAM', ],
    'IDC': ['PCAM', ],
    'DRIMDB': ['DRD', ],
    'RIGA': ['DRD', ],

    # STL10 is not compatible with CIFAR10 because of the 9-overlapping classes.
    # Erring on the side of caution.
}

# We can augment the following training data with mirroring.
# We make sure there's no information leak in-between tasks.
mirror_augment = {
    'FashionMNIST', 'CIFAR10', 'CIFAR100', 'STL10', 'TinyImagenet', 'STL10d32', 'TinyImagenetd32',
}

"""
    This where we keep a reference to all the models in the project.
"""

import models.classifiers as CLS
import models.autoencoders as AES
import models.pixelcnn.model as PCNN
import models.ALImodel as ALI

class ModelFactory(object):
    def __init__(self, parent_class, **kwargs):
        self.parent_class = parent_class
        self.kwargs = kwargs
    def __call__(self):
        return self.parent_class(**self.kwargs)

"""
    Each dataset has a list of compatible neural netwok architectures.
    Your life would be simpler if you keep the same family as the same index within each dataset.
    For instance, VGGs are all 0 and Resnets are all 1.
"""
dataset_reference_classifiers = {
    'MNIST':                  [CLS.MNIST_VGG,         CLS.MNIST_Resnet],
    'FashionMNIST':           [CLS.MNIST_VGG,         CLS.MNIST_Resnet],
    'CIFAR10':                [CLS.CIFAR10_VGG,       CLS.CIFAR10_Resnet],
    'CIFAR100':               [CLS.CIFAR100_VGG,      CLS.CIFAR100_Resnet],
    'STL10':                  [CLS.STL10_VGG,         CLS.STL10_Resnet],
    'TinyImagenet':           [CLS.TinyImagenet_VGG,  CLS.TinyImagenet_Resnet],
    'NIHCC':                    [CLS.NIHDenseBinary, CLS.NIHChestVGG],
    'PADChest':                 [CLS.PADDense],
    'PCAM':                     [CLS.PCAMDense],
    'DRD':                      [CLS.DRDDense],
}



dataset_reference_autoencoders = {
    'MNIST':              [ModelFactory(AES.Generic_AE, dims=(1, 28, 28), max_channels=256, depth=8, n_hidden=96)],
    'FashionMNIST':       [ModelFactory(AES.Generic_AE, dims=(1, 28, 28), max_channels=256, depth=8, n_hidden=96)],
    'CIFAR10':            [ModelFactory(AES.Generic_AE, dims=(3, 32, 32), max_channels=512, depth=10, n_hidden=256)],
    'CIFAR100':           [ModelFactory(AES.Generic_AE, dims=(3, 32, 32), max_channels=512, depth=10, n_hidden=256)],
    'STL10':              [ModelFactory(AES.Generic_AE, dims=(3, 96, 96), max_channels=512, depth=12, n_hidden=512)],
    'TinyImagenet':       [ModelFactory(AES.Generic_AE, dims=(3, 64, 64), max_channels=512, depth=12, n_hidden=512)],
    'NIHCC':                [ModelFactory(AES.Generic_AE, dims=(1, 64, 64), max_channels=512, depth=12, n_hidden=512),
                              ModelFactory(AES.ALILikeAE, dims=(1, 64, 64)),
                              ModelFactory(AES.Residual_AE, dims=(1, 64, 64)),
                             ModelFactory(AES.ALILikeResAE, dims=(1, 64, 64)),
                             ],
    'PADChest': [ModelFactory(AES.Generic_AE, dims=(1, 64, 64), max_channels=512, depth=12, n_hidden=512),
                 ModelFactory(AES.ALILikeAE, dims=(1, 64, 64)),
                 ],
    'PCAM':     [ModelFactory(AES.Generic_AE, dims=(3, 64, 64), max_channels=512, depth=12, n_hidden=512),
                 ModelFactory(AES.ALILikeAE, dims=(3, 64, 64)),
                 ],
    'DRD':     [ModelFactory(AES.Generic_AE, dims=(3, 64, 64), max_channels=512, depth=12, n_hidden=512),
                 ModelFactory(AES.ALILikeAE, dims=(3, 64, 64)),
                 ],
}

dataset_reference_vaes = {
    'MNIST': [ModelFactory(AES.Generic_VAE, dims=(1, 28, 28), max_channels=256, depth=8, n_hidden=96)],
    'FashionMNIST': [ModelFactory(AES.Generic_VAE, dims=(1, 28, 28), max_channels=256, depth=8, n_hidden=96)],
    'CIFAR10': [ModelFactory(AES.Generic_VAE, dims=(3, 32, 32), max_channels=512, depth=10, n_hidden=256)],
    'CIFAR100': [ModelFactory(AES.Generic_VAE, dims=(3, 32, 32), max_channels=512, depth=10, n_hidden=256)],
    'STL10': [ModelFactory(AES.Generic_VAE, dims=(3, 96, 96), max_channels=512, depth=12, n_hidden=512)],
    'TinyImagenet': [ModelFactory(AES.Generic_VAE, dims=(3, 64, 64), max_channels=512, depth=12, n_hidden=512)],
    'NIHCC': [ModelFactory(AES.Generic_VAE, dims=(1, 64, 64), max_channels=512, depth=12, n_hidden=512),
              ModelFactory(AES.ALILikeVAE, dims=(1, 64, 64)),
              ModelFactory(AES.ALILikeResVAE, dims=(1, 64, 64)),
              ],
    'PADChest': [ModelFactory(AES.Generic_VAE, dims=(1, 64, 64), max_channels=512, depth=12, n_hidden=512),
                 ModelFactory(AES.ALILikeVAE, dims=(1, 64, 64)),
                 ],
    'PCAM':     [ModelFactory(AES.Generic_VAE, dims=(3, 64, 64), max_channels=512, depth=12, n_hidden=512),
                 ModelFactory(AES.ALILikeVAE, dims=(3, 64, 64)),
                 ],
    'DRD': [ModelFactory(AES.Generic_VAE, dims=(3, 64, 64), max_channels=512, depth=12, n_hidden=512),
             ModelFactory(AES.ALILikeVAE, dims=(3, 64, 64)),
             ],
}

dataset_reference_ALI = {
                         'NIHCC': [ModelFactory(ALI.ALIModel, dims=(1, 64, 64), n_hidden=512)],
}

dataset_reference_pcnns = {
    'MNIST':              [ModelFactory(PCNN.PixelCNN, nr_resnet=5, nr_filters=32, input_channels=1, nr_logistic_mix=5)],
    'FashionMNIST':       [ModelFactory(PCNN.PixelCNN, nr_resnet=5, nr_filters=64, input_channels=1, nr_logistic_mix=5)],
    'CIFAR10':            [ModelFactory(PCNN.PixelCNN, nr_resnet=5, nr_filters=160, input_channels=3, nr_logistic_mix=10)],
    'CIFAR100':           [ModelFactory(PCNN.PixelCNN, nr_resnet=5, nr_filters=160, input_channels=3, nr_logistic_mix=10)],
    'TinyImagenetd32':    [ModelFactory(PCNN.PixelCNN, nr_resnet=5, nr_filters=160, input_channels=3, nr_logistic_mix=10)],
    'STL10d32':           [ModelFactory(PCNN.PixelCNN, nr_resnet=5, nr_filters=160, input_channels=3, nr_logistic_mix=10)],
}

"""
    This is where we keep a reference to all the methods.
"""

import methods.base_threshold as BT
import methods.score_svm as SSVM
import methods.logistic_threshold as KL
import methods.mcdropout as MCD
import methods.nearest_neighbor as KNN
import methods.binary_classifier as BinClass
import methods.deep_ensemble as DE
import methods.odin as ODIN
import methods.reconstruction_error as RE
import methods.pixelcnn as PCNN
import methods.openmax as OM
import methods.ALI as ALI
import methods.mahalanobis as MAHA

all_methods = {
    'prob_threshold':   BT.ProbabilityThreshold,
    'score_svm':        SSVM.ScoreSVM,
    'logistic_svm':     KL.LogisticSVM,
    'mcdropout':        MCD.MCDropout,
    'knn':              KNN.KNNSVM,
    'bceaeknn':         KNN.BCEKNNSVM,
    'mseaeknn':         KNN.MSEKNNSVM,
    'vaebceaeknn':         KNN.VAEBCEKNNSVM,
    'vaemseaeknn':         KNN.VAEMSEKNNSVM,
    'alibceaeknn':         KNN.ALIBCEKNNSVM,
    'alimseaeknn':         KNN.ALIMSEKNNSVM,
    'alivaebceaeknn':         KNN.ALIVAEBCEKNNSVM,
    'alivaemseaeknn':         KNN.ALIVAEMSEKNNSVM,
    'aliknnsvm':           KNN.ALIKNNSVM,
    'svknn':            KNN.SVKNNSVM,
    'binclass':         BinClass.BinaryClassifier,
    'deep_ensemble':    DE.DeepEnsemble,
    'odin':             ODIN.ODIN,
    'reconst_thresh':   RE.ReconstructionThreshold,
    'pixelcnn':         PCNN.PixelCNN,
    'openmax':          OM.OpenMax,
    'ALI_reconst':      ALI.ALIReconstruction,
    'Maha':             MAHA.MahalanobisDetector,
    'Maha1layer':       MAHA.MahalanobisDetectorOneLayer,
}

##################################################################
# Do not change anything below, unless you know what you are doing.
"""
    all_datasets is automatically generated
    all_datasets = {
        'MNIST' : MNIST,
        ...
    }
    
"""
all_datasets = {}
for dscls in all_dataset_classes:
    all_datasets[dscls.__name__] = dscls

def get_ref_classifier(dataset):
    if dataset in dataset_reference_classifiers:
        return dataset_reference_classifiers[dataset]
    raise NotImplementedError()

def get_ref_autoencoder(dataset):
    if dataset in dataset_reference_autoencoders:
        return dataset_reference_autoencoders[dataset]
    raise NotImplementedError()

def get_ref_vae(dataset):
    if dataset in dataset_reference_vaes:
        return dataset_reference_vaes[dataset]
    raise NotImplementedError()

def get_ref_ali(dataset):
    if dataset in dataset_reference_ALI:
        return dataset_reference_ALI[dataset]
    raise NotImplementedError()

def get_ref_pixelcnn(dataset):
    if dataset in dataset_reference_pcnns:
        return dataset_reference_pcnns[dataset]
    raise NotImplementedError()

def get_method(name, args):
    elements = name.split('/')
    instance = all_methods[elements[0]](args)
    if len(elements) > 1:
        instance.default_model = int(elements[1])
    return instance
    