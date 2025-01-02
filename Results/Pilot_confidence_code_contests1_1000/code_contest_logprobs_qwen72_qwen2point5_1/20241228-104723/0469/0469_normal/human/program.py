#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, exit


def main(readline=stdin.readline):
    for _ in range(int(readline())):
        print(readline().replace('Hoshino', 'Hoshina'), end='')
    exit()


if __name__ == '__main__':
    main()