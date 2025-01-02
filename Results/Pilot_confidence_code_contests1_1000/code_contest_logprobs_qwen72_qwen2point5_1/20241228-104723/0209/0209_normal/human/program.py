#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, exit
from collections import Counter


def main(readline=stdin.readline):
    count = Counter()
    member = []

    while 1:
        n = int(readline())
        if not n:
            exit()

        count.clear()
        del member[:]

        for _ in range(n):
            i, price, num = (int(s) for s in readline().split())
            count[i] += price * num
            if i not in member:
                member.append(i)

        member = [i for i in member if count[i] >= 1000000]

        if member:
            print(*member, sep='\n')
        else:
            print('NA')


if __name__ == '__main__':
    main()