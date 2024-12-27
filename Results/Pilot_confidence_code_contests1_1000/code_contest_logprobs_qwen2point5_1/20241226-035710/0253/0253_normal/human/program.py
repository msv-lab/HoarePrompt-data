from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

while True:
    a = stdin.readline().strip()
    if not a:
        break
    b = stdin.readline().strip()
    if a == b:
        print('4 0')
        continue
    hit = sum(int(a[i] == b[i]) for i in xrange(0, 7, 2))
    blow = sum(int(b[i] in a) for i in xrange(0, 7, 2)) - hit
    print(hit, blow)