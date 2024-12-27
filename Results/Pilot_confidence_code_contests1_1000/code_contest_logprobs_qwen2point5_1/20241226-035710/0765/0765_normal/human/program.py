#!/usr/bin/python
# -*- coding: utf-8 -*-
"""One line explanation of b.py.

More explanations of b.py."""

import sys

def read_input(fin):
    l0 = fin.readline()
    l1 = fin.readline()
    return sorted([int(c) for c in l1.strip().split(' ')], reverse=True)

def solve(data):
    result = 0
    sign = 1
    for d in data:
        result += d * sign
        sign = -sign
    return result

def main(argv):
    d = read_input(sys.stdin)
    sys.stdout.write('%d\n' % solve(d))
    

if __name__ == '__main__':
    main(sys.argv)
