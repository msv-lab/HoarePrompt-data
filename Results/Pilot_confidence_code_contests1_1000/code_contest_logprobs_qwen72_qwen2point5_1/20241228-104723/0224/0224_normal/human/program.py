from __future__ import division, print_function

import sys
from atexit import register

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream


sys.stdin = stream(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')

sys.stdout = stream()
register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split(' ')))


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def solve():
    N = read_int()
    A = read_ints()
    if N == 1:
        print(1, 1)
        print(-A[0])
        print(1, 1)
        print(0)
        print(1, 1)
        print(0)
        return
    gcd, x, y = egcd(N-1, N)
    B = []
    for a in A[:N-1]:
        B.append(-a*(N-1)*x)
    B.append(0)
    print(1, N-1)
    print(*B[:N-1])
    A = [a+b for a, b in zip(A, B)]
    print(N, N)
    print(N-A[-1])
    A[-1] = N
    print(1, N)
    print(*[-a for a in A])


if __name__ == '__main__':
    solve()
