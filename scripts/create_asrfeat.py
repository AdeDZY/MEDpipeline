#!/usr/bin/env python
import numpy
import os
import cPickle
import sys
import argparse
from nltk.stem import SnowballStemmer
import math

def build_vocab(vocab_file, stopwords_file):
    stemmer = SnowballStemmer('english')

    vocab = {}
    dfs = {}
    stopwords = set()
    for line in open(stopwords_file):
        word = line.strip()
        stopwords.add(word)
    stopwords.add("<#s>")

    i = 0
    for line in open(vocab_file):
        word = line.strip().lower()
        word = stemmer.stem(word)
        if word in vocab:
            dfs[vocab[word]] += 1
        if word not in stopwords and word not in vocab:
            vocab[word] = i
            dfs[i] = 1
            i += 1

    return vocab, dfs


def asr_to_bow(asr_file_path, vocab, dfs):
    stemmer = SnowballStemmer('english')
    vec = [0 for i in range(len(vocab))]
    for line in open(asr_file_path):
        word = line.split()[4]
        word = stemmer.stem(word)
        if word not in vocab:
            continue
        tid = vocab[word]
        vec[tid] += 1
    for i in range(len(vec)):
        vec[i] *= math.log(883.0/dfs[i])
    return vec


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("vocab_file", help="path to the vocabulary file")
    parser.add_argument("file_list", help="the list of videos")
    parser.add_argument("stopwords_file", help="stopwords file path")
    args = parser.parse_args()

    # get vocab
    vocab, dfs = build_vocab(args.vocab_file, args.stopwords_file)

    # output file
    output_file = open("asrfeat/all.vectors", 'w')

    # process each video
    for line in open(args.file_list):
        video_name = line.strip()
        asr_file_path = "/home/ubuntu/hw1/asr/{}.ctm".format(video_name)

        if not os.path.exists(asr_file_path):
            print "{}'s ASR features not exist! Write vector as -1".format(video_name)
            output_file.write(video_name + "\t-1\n")
            continue

        vec = asr_to_bow(asr_file_path, vocab, dfs)
        output_str = ';'.join([str(t) for t in vec])
        output_file.write(video_name + '\t')
        output_file.write(output_str + '\n')

    print "feat dimenstion: {0}!".format(len(vocab))
    print "ASR features generated successfully! Written into {0}!".format("asrfeat/all.vectors")


if __name__ == '__main__':
    main()

