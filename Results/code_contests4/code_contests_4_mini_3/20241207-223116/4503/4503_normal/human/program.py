#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

def draw_cross(line, end, pos, left):
    if left:
        if pos < 1 or line[pos-1]:
            return False
        elif pos > 1 and line[pos-2]:
            return False
        elif pos < end and line[pos]:
            return False
        line[pos-1] = 1
        return pos

    if pos >= end or line[pos]:
        return False
    elif pos < end-1 and line[pos+1]:
        return False
    elif pos > 0 and line[pos-1]:
        return False
    line[pos] = 1
    return pos + 1

def run(start, side, add, left):
    end = len(side[0])
    pos = start - 1
    add -= 1
    cross = 0

    for step, line in enumerate(side):
        line = line[:]
        if add == step:
            cross = draw_cross(line, end, pos, left)
            if not cross:
                return (False, False)

        if pos > 0 and line[pos-1]:
            pos -= 1
        elif pos < end and line[pos]:
            pos += 1
    return (cross, pos + 1)

while True:
    n = int(stdin.readline())
    if not n:
        break
    start = int(stdin.readline())
    hit = int(stdin.readline())
    num_step = int(stdin.readline())
    side = []
    for i in range(num_step):
        side.append([int(s) for s in stdin.readline().rstrip()])

    cross, goal = run(start, side, 0, True)
    if goal == hit:
        print(0)
        continue
    for step in range(1, num_step+1):
        cross, goal = run(start, side, step, left=True)
        if goal == hit:
            print(step, cross)
            break
        cross, goal = run(start, side, step, left=False)
        if goal == hit:
            print(step, cross)
            break
    else:
        print(1)