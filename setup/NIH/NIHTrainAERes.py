from __future__ import print_function
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

from utils.args import args

import setup.categories.ae_setup as AESetup
from models.autoencoders import Generic_VAE, Generic_AE, Residual_AE
from datasets.NIH_Chest import NIHChestBinaryTrainSplit

if __name__ == "__main__":
    dataset = NIHChestBinaryTrainSplit(root_path=os.path.join(args.root_path, "NIHCC"), binary=True, expand_channels=False, downsample=64)
    model = Residual_AE(dims=(1, 64, 64))
    AESetup.train_autoencoder(args, model=model, dataset=dataset.get_D1_train(), BCE_Loss=False)

