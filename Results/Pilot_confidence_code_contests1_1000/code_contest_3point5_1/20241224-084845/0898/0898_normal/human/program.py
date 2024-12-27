#!/usr/bin/env python2
from __future__ import division, print_function

from math import trunc
import _numpypy.multiarray as np

input = raw_input

MOD = 1 << 32
MODF = float(MOD)

MAGIC = 6755399441055744.0
SHRT = 65536.0

MODF_INV = 1.0 / MODF
SHRT_INV = 1.0 / SHRT

fround = lambda x: (x + MAGIC) - MAGIC
fmod = lambda a: a - MODF * fround(MODF_INV * a)
fmul = lambda a, b, c=0.0: fmod(fmod(a * SHRT) * fround(SHRT_INV * b) + a * (b - SHRT * fround(b * SHRT_INV)) + c)


def main():
    n, a, b, c, d = map(int, input().split())
    aa = 1.0*a
    bb = 1.0*b
    cc = 1.0*c
    dd = 1.0*d
    nn = 1.0*n

    def prime_contribution(i):
        ii = 1.0*i
        f = fmul(ii, fmul(ii, fmul(ii, aa, bb), cc), dd)
        
        ii_inv = 1.0/ii
        res = 0.0
        numb = trunc(nn*ii_inv)
        while numb:
            res += numb
            numb = trunc(numb*ii_inv)
        return fmul(f,fmod(res))

    cnt = prime_contribution(2) + prime_contribution(3)
    sieve = bytearray(12500000)

    i, t = 5, 2
    while i <= n:
        if not (sieve[(i // 3) >> 3] >> ((i // 3) & 7)) & 1:
            cnt = fmod(cnt + prime_contribution(i))
            if i > (n + i - 1) // i:
                i += t
                t = 6 - t
                continue

            j = i * i
            v = t
            while j <= n:
                sieve[(j // 3) >> 3] |= 1 << ((j // 3) & 7)
                j += v * i
                v = 6 - v

        i += t
        t = 6 - t

    print(int(cnt) if cnt >= 0.0 else 4294967296 + int(cnt))


if __name__ == '__main__':
    main()