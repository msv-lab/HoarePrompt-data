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
    n, k = map(int, input().split())
    songs = [[int(i) for i in input().split()] for _ in range(n)]
    songs = sorted(songs, key=lambda x: (-x[1], x[0]))

    prefix = [0]
    for i in songs:
        prefix.append(prefix[-1] + i[0])


    print(max((prefix[i + 1] - prefix[max(0, i + 1 - k)]) * songs[i][1] for i in range(n)))

    #m = 0
    #b = songs[0][1]
    #for i, song in enumerate(songs):
    #    if song[1] != b:
    #        m = max(m, (prefix[i] - prefix[max(0, i - k)]) * b)
    #    b = song[1]
    #m = max(m, (prefix[n] - prefix[max(0, n - k)]) * b)

    #print(m)


if __name__ == '__main__':
    main()
