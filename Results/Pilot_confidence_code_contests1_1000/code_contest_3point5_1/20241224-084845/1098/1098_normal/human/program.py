#!/usr/bin/python
# -*- Coding: utf-8 -*-

sample = ''
sample = str(raw_input())
def main(sample):
    arr = []
    length = 0
    ans = 0
    for s in sample:
        arr.append(s)
    for t in arr:
        if t == 'A' or t == 'C' or t == 'G' or t == 'T':
            length += 1
        elif ans < length:
            ans = length
    print(ans)
    return True

main(sample)
