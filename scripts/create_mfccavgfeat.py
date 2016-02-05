#!/usr/bin/env python
__author__ = 'zhuyund'

import numpy
import os
import cPickle
import sys
import argparse


def avg_mfcc(mfcc_file_path):
    """
    Generate the average of MFCC features
    :param mfcc_file_path
    :return: vec
    """
    vec = []
    n = 0
    for line in open(mfcc_file_path):
        vals = line.split(';')
        for i, v in enumerate(vals):
            v = float(v)
            if len(vec) <= i:
                vec.append(v)
            else:
                vec[i] += v
        n += 1

    for i in range(len(vec)):
        vec[i] /= n

    return vec


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_list", help="the list of videos")
    args = parser.parse_args()


    # output file

    output_file = open("mfccavg_feat/all.vectors", 'w')

    # process each video
    for line in open(args.file_list):
        video_name = line.strip()
        mfcc_file_path = "/home/ubuntu/hw1/mfcc/{}.mfcc.csv".format(video_name)

        vec = avg_mfcc(mfcc_file_path)
        output_str = ';'.join([str(t) for t in vec])
        output_file.write(video_name + '\t')
        output_file.write(output_str + '\n')

    print "MFCC_avg features generated successfully! Written into {0}!".format("mfccavg_feat/all.vectors")


if __name__ == '__main__':
    main()

