from __future__ import division, print_function
from sys import stdin
from fractions import gcd


def bs(be, en):
    while be < en:
        mid = (be + en + 1) // 2

        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1

    print(be * x, be * y)


rints = lambda: [int(x) for x in stdin.readline().split()]
a, b, x, y = rints()
g = gcd(x, y)
x //= g
y //= g

# solution 1
# bs(0, (2 * 10 ** 9) + 1)
# solution 2
mi = min(a // x, b // y)
print(mi * x, mi * y)
