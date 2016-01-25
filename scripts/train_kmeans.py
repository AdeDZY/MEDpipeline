#!/usr/bin/env python

import numpy
import os
from sklearn.cluster import KMeans
import cPickle
import argparse


def load_mfcc(mfcc_csv_file):
    """
    load sampled MFCC features into a matrix X
    :param mfcc_csv_file: path to the mfcc csv file
    :return: X. shape=(n_samples, n_features)
    """
    X = []
    i = 0
    for line in open(mfcc_csv_file):
        i += 1
        #if i % 10 != 0:
        #    continue
        x = [float(val) for val in line.split(';')]
        X.append(x)
    return X


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mfcc_csv_file", help="path to the mfcc csv file")
    parser.add_argument("cluster_num", type=int, help="number of cluster")
    parser.add_argument("output_file", help="path to save the k-means model")
    args = parser.parse_args()

    # load MFCC features
    print ">> loading MFCC..."
    X = load_mfcc(args.mfcc_csv_file)
    print ">> load {0} vectors for clustering. ".format(len(X))

    # perform kmeans
    print ">> training K-means..."
    km = KMeans(args.cluster_num)
    km.fit(X)

    # save model
    print ">> saving model..."
    outfile = open(args.output_file, 'wb')
    cPickle.dump(km, outfile)
    print "K-means model saved at {0}!".format(args.output_file)


# Performs K-means clustering and save the model to a local file
if __name__ == '__main__':
    main()
