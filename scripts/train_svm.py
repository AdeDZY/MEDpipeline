#!/usr/bin/env python
__author__ = 'zhuyund'

import numpy
import os
from sklearn import svm
import cPickle
import sys
import argparse


def load_training_data(event_name, feat_file_path):
    """
    Load training data and labels for a event
    :param event_name: str. e.g. P001
    :param feat_file_path: the file that contains all features.
    Each line represents a video. Line starts with video_name, than a '\t', than the feature vector
    :return: X, y.
    X is the training feature vectors. shape=(n_sample, n_feat)
    y is the training labels. shape=(1, n_sample)
    """
    event_train_list = open("/home/ubuntu/hw1/list/{0}_train".format(event_name))
    video2label = {}
    for line in event_train_list:
        video, label = line.split()
        video2label[video] = label
    event_train_list.close()

    X = []
    y = []
    for line in open(feat_file_path):
        line = line.strip()
        if line == '-1':
            continue
        video, feats = line.split('\t')
        if video not in video2label:
            continue

        x = [float(t) for t in feats.split(';')]
        X.append(x)

        y.append(video2label[video])

    return X, y


# Performs K-means clustering and save the model to a local file
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("event_name", help="name of the event (P001, P002 or P003 in Homework 1)")
    parser.add_argument("feat_dir", help="dir of feature files")
    parser.add_argument("feat_dim", help="dimension of features")
    parser.add_argument("output_file", help="path to save the svm model")
    parser.add_argument("--kernel", "-k", help="kernel for the svm",
                        choices=["linear", "poly", "rbf"], default='linear')
    args = parser.parse_args()

    # load training data
    feat_file_path = args.feat_dir + '/all.vectors'
    X, y = load_training_data(args.event_name, feat_file_path)

    # train SVM
    print ">> training SVM with {0} kernel on {1} samples".format(args.kernel, len(y))
    clf = svm.SVC(kernel=args.kernel)
    clf.fit(X, y)

    # save the trained model
    outfile = open(args.output_file, 'wb')
    cPickle.dump(clf,outfile)
    print ">> model saved to {0}!".format(args.output_file)

if __name__ == '__main__':
    main()
