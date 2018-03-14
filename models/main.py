import sys, os

import numpy
import scipy
import torch
import sklearn
import pandas

import pickle

import datetime

import argparse


parser = argparse.ArgumentParser(description='Sequence Tagger')

# learning
parser.add_argument('--dropout', type=float, default=0.1, help='Dropout zero probability [default: 0.1]')

# model configuration

# data loading

# options

# task




args = parser.parse_args()
#args.filter_sizes = [int(K) for K in args.filter_sizes.split(',')]


if __name__ == '__main__':
    print("\nParameters:")

    for attr, value in sorted(args.__dict__.items()):
        print("\t{}={}".format(attr.upper(), value))
