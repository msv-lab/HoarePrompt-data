from __future__ import division, print_function

DEBUG = 0

INF = float('inf')
MOD = 10 ** 9 + 7

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
    from bisect import bisect_right

    def update(o, n):
        if n[0] < o[0]:
            return n
        elif n[0] == o[0]:
            return o[0], (o[1] + n[1]) % MOD
        else:
            return o

    def update2(o, n):
        if n[0] > o[0]:
            return n
        elif n[0] == o[0]:
            return o[0], (o[1] + n[1]) % MOD
        else:
            return o

    n = int(input())
    a = [input_as_list() for _ in range(n)]
    a.sort()

    eps = []
    best = []
    d = dict()
    er = []

    for ep, sp in a:
        if not eps or eps[-1] != ep:
            eps.append(ep)

        if not er or er[-1][0] != ep:
            er.append([ep, sp])
        else:
            er[-1][1] = sp

        i = bisect_right(eps, sp) - 1
        if i == -1:
            g, c = sp, 1
        else:
            g, c = sp - best[i][0], best[i][1]

        try:
            gap, count = d[ep]
        except KeyError:
            gap, count = ep, 0

        gap, count = update((gap, count), (g, c))
        d[ep] = (gap, count)

        try:
            best[len(eps)-1] = update2(best[len(eps)-1], (ep-g, c))
        except IndexError:
            if len(eps) == 1:
                best.append((ep - g, c))
            else:
                best.append(update2(best[len(eps)-2], (ep-g, c)))

    debug_print(eps)
    debug_print(d)
    debug_print(best)
    debug_print(er)

    e, sb = er.pop()
    ans = (e, 0)
    while sb < e:
        ans = update(ans, d[e])
        if er:
            e, s = er.pop()
            sb = max(sb, s)
        else:
            break

    print(ans[1])


main()