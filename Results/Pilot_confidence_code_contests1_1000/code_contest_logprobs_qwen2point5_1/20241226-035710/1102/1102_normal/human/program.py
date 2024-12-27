#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, exit


def main(readline=stdin.readline):
    price_table = (
        0, 0, 380, 550, 760, 850, 1100, 1230, 1400, 1610, 1520, 1950,
        1870, 2070, 2250, 2244, 2620, 2624, 2794, 3004, 3040, 3344,
        3390, 3590, 3740, 3764, 4120, 4114, 4314, 4494, 4488, 4864,
        4868, 5038, 5248, 5284, 5588, 5634, 5834, 5984, 6008, 6364,
        6358, 6558, 6738, 6732, 7108, 7112, 7282, 7492, 7528
        )
    while 1:
        weight = int(readline())
        if not weight:
            exit()
        print(price_table[weight//100])


if __name__ == '__main__':
    main()