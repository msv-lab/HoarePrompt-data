#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, exit


def main(readline=stdin.readline):
    leap_year = [not y % 4 and y % 100 or not y % 400 for y in range(3001)]
    separator = ''
    while 1:
        a, b = (int(s) for s in readline().split())
        if not a and not b:
            exit()

        print(separator, end='')

        result = 'NA\n'
        for year, leap in enumerate(leap_year[a:b+1], a):
            if leap:
                print(year)
                result = ''

        print(result, end='')
        separator = '\n'


main()