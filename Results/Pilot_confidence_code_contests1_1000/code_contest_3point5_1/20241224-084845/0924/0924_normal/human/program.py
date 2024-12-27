from sys import stdin


def fact(be, en):
    res, res2 = [1], [1]
    for i in range(be, en + 1):
        res.append(mult(res[-1], i))
        res2.append(inv(res[-1]))
    return res, res2


def ncr_rep(n, r):
    return mult(mult(facs[n], invs[n - r]), invs[r])


add = lambda a, b: (a + b) % mod
mult = lambda a, b: (a * b) % mod
div = lambda a, b: mult(a, inv(b))
inv = lambda a: pow(a, mod - 2, mod)

n, c = map(int, stdin.readline().split())
mod = 10 ** 6 + 3
facs, invs = fact(1, n + c)
print(add(ncr_rep(n + c, n), -1))
