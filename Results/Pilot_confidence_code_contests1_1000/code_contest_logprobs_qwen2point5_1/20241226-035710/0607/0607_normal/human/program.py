#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, exit


def main(readline=stdin.readline):
    n, q = (int(s) for s in readline().split())

    base = [0] * n
    midway = [0] * (n//100 + 1)
    last = [0] * (n//10000 + 1)

    for _ in range(q):
        a, v = (int(s) for s in readline().split())

        a -= 1
        base[a] += v

        b = a - a % 100

        index = b
        value = base[b]
        end = b + 100 if b + 100 < n else n
        for i in range(b, end):
            if value < base[i]:
                value = base[i]
                index = i
        midway[b//100] = index

        c = a - a % 10000
        cc = c // 100

        index = c
        value = base[c]
        for i in midway[cc:cc+100]:
            if value < base[i]:
                value = base[i]
                index = i
        last[c//10000] = index

        index = last[0]
        value = base[index]
        for i in last:
            if value < base[i]:
                value = base[i]
                index = i

        print(index+1, value)
    exit()


if __name__ == '__main__':
    main()