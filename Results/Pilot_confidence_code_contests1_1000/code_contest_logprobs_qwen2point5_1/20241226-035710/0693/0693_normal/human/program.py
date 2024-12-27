#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin
a, b = (int(s) for s in stdin.readline().split())
while b:
    a, b = b, a % b
print(a)