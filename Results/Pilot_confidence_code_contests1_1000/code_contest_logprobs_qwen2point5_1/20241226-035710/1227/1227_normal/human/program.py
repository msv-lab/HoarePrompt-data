#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin


def main():
    num_mat = int(stdin.readline())
    data = [int(s) for s in stdin.readline().split()]
    for _ in range(num_mat-1):
        _, row = (int(s) for s in stdin.readline().split())
        data.append(row)
    num_dat = len(data)

    bin_op = tuple(data[i]*data[i+1]*data[i+2] for i in range(num_dat-2))
    parts = [(data[0]*data[1], data[-2]*data[-1]), bin_op]

    for j in range(3, num_mat):
        part = parts[-1]
        new_part = []
        for i in range(num_dat-j):
            a = data[i]
            b = data[i+1]
            c = data[i+j-1]
            d = data[i+j]
            new_part.append(min(part[i] + a*c*d, part[i+1] + a*b*d))
        parts.append(new_part)

    L = data
    if num_mat > 1:
        print(min(parts[i][0] + parts[-(i+1)][-1] +
                  L[0]*L[i+1]*L[-1] for i in range(len(parts))))
    else:
        print(0)


main()