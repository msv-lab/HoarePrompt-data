#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, exit, maxsize


def main(readline=stdin.readline):
    value = -1
    number = maxsize
    for _ in range(int(readline())):
        a, v = (int(s) for s in readline().split())
        if v > value or v == value and a < number:
            number = a
            value = v
    print(number, value)
    exit()


main()