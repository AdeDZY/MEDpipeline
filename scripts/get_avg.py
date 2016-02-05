#!/usr/bin/env python
__author__ = 'zhuyund'

import argparse
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    args = parser.parse_args()

    s = 0
    n = 0
    for line in open(args.infile):
        score = line.strip().split(' ')[-1]
        s += float(score)
        n += 1
    print 'avg: ' + str(s/n)


if __name__ == '__main__':
    main()

