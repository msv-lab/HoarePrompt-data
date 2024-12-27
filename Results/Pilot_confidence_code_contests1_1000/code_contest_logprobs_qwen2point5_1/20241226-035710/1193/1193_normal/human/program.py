from __future__ import division, print_function

DEBUG = 0
INF = float('inf')

import os, sys
from atexit import register
from io import BytesIO
import itertools

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

if DEBUG:
    debug_print = print
else:
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))

    input = lambda: sys.stdin.readline().rstrip('\r\n')
    debug_print = lambda *x, **y: None


def input_as_list():
    return list(map(int, input().split()))


def array_of(f, *dim):
    return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()


def main():
    N = 2**10

    n, m = input_as_list()

    human = array_of(int, N)
    pizza = array_of(lambda: INF, N)
    pizza_idx = array_of(int, N)

    for _ in range(n):
        res = 0
        for e in input_as_list()[1:]:
            res += 1 << e
        human[res] += 1

    debug_print(human)

    raw_pizza = [(input_as_list(), i) for i in range(m)]
    raw_pizza.sort()

    pizza2 = array_of(lambda: INF, N)
    pizza2_idx = array_of(lambda: (0, 0), N)

    for a, i in raw_pizza:
        res = 0
        for e in a[2:]:
            res += 1 << e
        if pizza[res] == INF:
            pizza[res] = a[0]
            pizza_idx[res] = i
        elif pizza2[res] == INF:
            pizza2[res] = pizza[res] + a[0]
            pizza2_idx[res] = (pizza_idx[res], i)

    debug_print(pizza)

    for i in range(1, N):
        for j in range(i+1, N):
            if pizza[i] + pizza[j] < pizza2[i|j]:
                pizza2[i|j] = pizza[i] + pizza[j]
                pizza2_idx[i|j] = (pizza_idx[i], pizza_idx[j])

    maxhuman = 0
    mincost = INF
    minindex = (0, 1)
    debug_print(pizza2_idx)

    for i in range(1, N):
        if pizza2[i] == INF:
            continue

        thishuman = 0

        for j in range(1, N):

            if i|j == i:
                thishuman += human[j]

        if thishuman > maxhuman:
            maxhuman = thishuman
            mincost = pizza2[i]
            minindex = pizza2_idx[i]
        elif thishuman == maxhuman and pizza2[i] < mincost:
            mincost = pizza2[i]
            minindex = pizza2_idx[i]

    print(minindex[0]+1, minindex[1]+1)

main()