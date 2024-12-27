#!/usr/bin/env python
from __future__ import division, print_function

import io
import os
import sys

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from cStringIO import StringIO
    from future_builtins import ascii, filter, hex, map, oct, zip
else:
    from io import BytesIO as StringIO

sys.stdout, stream = io.IOBase(), StringIO()
sys.stdout.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
sys.stdout.write = stream.write if sys.version_info[0] < 3 else lambda s: stream.write(s.encode())

input, flush = sys.stdin.readline, sys.stdout.flush
input = StringIO(os.read(0, os.fstat(0).st_size)).readline


def main():
    n = int(input())
    nodes = [[int(i) for i in input().split()] for _ in range(n)]

    a = list(map(lambda x: x[1], nodes))

    for node in nodes:
        if node[0] != -1:
            a[node[0] - 1] &= node[1]

    sol = [node + 1 for node, _ in filter(lambda x: x[1], zip(range(n), a))]
    print(sol if sol else -1)


if __name__ == '__main__':
    main()
