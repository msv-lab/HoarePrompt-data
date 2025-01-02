from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

for line in stdin:
    L = [int(s) for s in line.split(',')]
    cross_over = L[10] * sum(L[:10]) / (L[10] + L[11])
    d = 0
    for i, xi in enumerate(L[:10]):
        d += xi
        if cross_over <= d:
            break
    print(i+1)