#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function
import sys


def main():
    h, w = map(int, sys.stdin.readline().strip().split(" "))
    aa = ""
    for _ in range(h):
        aa += sys.stdin.readline().strip()
    d = {}
    for c in aa:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    # print(d)
    fours = 0
    evens = 0
    odds = 0

    for c, count in d.items():
        fours += count // 4
        evens += (count % 4) // 2
        odds += count % 2

    # print(fours, evens, odds)
    if h % 2 == 0 and w % 2 == 0:
        print("Yes" if odds == 0 and evens == 0 else "No")
    elif h % 2 == 0 and w % 2 == 1:
        print("Yes" if odds == 0 and evens * 2 == h else "No")
    elif h % 2 == 1 and w % 2 == 0:
        print("Yes" if odds == 0 and evens * 2 == w else "No")
    else:
        print("Yes" if odds == 1 and evens * 2 == w + h - 2 else "No")


if __name__ == '__main__':
    main()
