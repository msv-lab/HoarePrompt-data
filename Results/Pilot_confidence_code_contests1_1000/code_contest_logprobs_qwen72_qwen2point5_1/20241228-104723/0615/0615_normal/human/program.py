from sys import stdin
from collections import *

rints = lambda: [int(x) for x in stdin.readline().split()]
rints_2d = lambda n: [rints() for _ in range(n)]
get_col = lambda arr, i: [row[i] for row in arr]

n = int(input()) * 4 + 1
a, memx, memy = rints_2d(n), [float('inf'), -1], [float('inf'), -1]
xs, ys = Counter(get_col(a, 0)), Counter(get_col(a, 1))

for x, y in a:
    if xs[x] >= (n - 1) >> 2:
        memx = [min(memx[0], x), max(memx[1], x)]
    if ys[y] >= (n - 1) >> 2:
        memy = [min(memy[0], y), max(memy[1], y)]

for x, y in a:
    if not ((memx[0] < x < memx[1] and y in memy) or (x in memx and memy[0] <= y <= memy[1])):
        print('%d %d' % (x, y))
        exit()
