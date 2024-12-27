#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys, os, re, math

n = int(raw_input())

a = [int(x) for x in raw_input().split(' ')][::-1]

i = n-1
while i > 0 and a[i] > a[i-1]:
    i -= 1


print(n-i-1)
