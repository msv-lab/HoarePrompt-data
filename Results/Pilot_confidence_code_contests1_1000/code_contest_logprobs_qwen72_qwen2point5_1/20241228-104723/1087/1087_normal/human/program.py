#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
input = sys.stdin
output = sys.stdout

from itertools import combinations

def compose_geom(t):
    a,b,c = t
    D2 = [a+b,a+c,b+c]
    for d2 in D2:
        for d in t:
            if d2 == d:
                return 'SEGMENT'
            elif d2 < d:
                return None
    return 'TRIANGLE'

def solve(D):
    for t in combinations(D,3):
        r = compose_geom(t)
        if r is not None:
            return r
    return 'IMPOSSIBLE'

def numbers_from_line(d=' '):
    return [int(s) for s in input.readline().strip().split(d) if len(s.strip())>0]

D = numbers_from_line()

a = solve(D)
output.write('%s\n' % a)
