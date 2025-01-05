#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, exit
from collections import defaultdict


def main():
    index = defaultdict(list)

    for line in stdin:
        word, page = line.split()
        index[word].append(int(page))

    for word in sorted(index):
        print(word)
        print(*sorted(index[word]))
    exit()


if __name__ == '__main__':
    main()