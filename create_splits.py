import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /mnt/data
    """
    # TODO: Implement function
    os.makedirs(data_dir+"/train", exist_ok=True)
    os.makedirs(data_dir+"/val", exist_ok=True)
    os.makedirs(data_dir+"/test", exist_ok=True)

    fnames = os.listdir(data_dir+"/processed/")
    random.shuffle(fnames)

    for i, fname in enumerate(fnames):
        if i < 70:
            folder = 'train'
        elif i < 85:
            folder = 'val'
        else:
            folder = 'test'

        os.rename(data_dir+"/processed/"+fname, data_dir+"/"+folder+"/"+fname)
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)