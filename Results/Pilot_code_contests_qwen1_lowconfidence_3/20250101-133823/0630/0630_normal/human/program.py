#!/usr/bin/env python
from __future__ import division, print_function

import io
import os
import sys
from collections import defaultdict

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
    rounds = [input().split() for _ in range(n)]
    rounds = [(name, int(score)) for name, score in rounds]

    final_scores = defaultdict(int)
    for name, score in rounds:
        final_scores[name] += score

    m = max(final_scores.values())
    winner_candidates = {player for player, score in final_scores.items() if score == m}

    curr_scores = defaultdict(int)
    for name, score in rounds:
        curr_scores[name] += score
        if (curr_scores[name] >= m) and (name in winner_candidates):
            print(name)
            break


if __name__ == '__main__':
    main()
