#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
input = sys.stdin
output = sys.stdout

def solve(A):
    N = 0
    m = 1
    prev = A[0]
    for i in range(1,len(A)):
        a = A[i]
        if a == prev:
            m += 1
        else:
            N += (m+1)*(m)/2
            prev = a
            m = 1
    N += (m+1)*(m)/2
    return N

n = int(input.readline())
As = input.readline().split(' ')
A = [int(s) for s in As]
assert len(A) > 0 and len(A) == n
N = solve(A)

output.write('%s' % str(N))