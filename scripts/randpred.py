#!/usr/bin/env python
__author__ = 'zhuyund'

import argparse
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file")
    args = parser.parse_args()

    n = 234
    outfile = open(args.output_file, 'w')
    for i in range(n):
        score = random.random()
        outfile.write('{0\n'.format(score))
    outfile.close()

if __name__ == '__main__':
    main()

