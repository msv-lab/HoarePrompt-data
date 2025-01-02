from sys import stdin
from collections import Counter


def count_prime(n):
    prim, ans = [0] * (n + 1), 0

    for i in range(2, n):
        if not prim[i]:
            prim[i] = a[i]
            for j in range(i << 1, n, i):
                prim[j] = i
                prim[i] += a[j]

            ans = max(ans, prim[i])

    print(max(ans, 1))


n, a = int(input()), Counter([int(x) for x in stdin.readline().split()])
count_prime(10 ** 5 + 1)
