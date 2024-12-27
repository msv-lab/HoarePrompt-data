from sys import stdin

period_pow = lambda r1, r2, n, x: div(add(pow(r2, (x + 1) * n, mod), -pow(r1, (x + 1) * n, mod)),
                                      add(mult(pow(r2, n, mod), pow(r1, x * n, mod)), - pow(r1, n * (x + 1), mod)))
add = lambda a, b: (a + b) % mod
mult = lambda a, b: (a * b) % mod
div = lambda a, b: mult(a, inv(b))
inv = lambda a: pow(a, mod - 2, mod)
mod = 10 ** 9 + 9

n, a, b, k = map(int, stdin.readline().split())
s, su = stdin.readline().strip(), 0
for i, j in enumerate(s):
    cur = mult(pow(a, n - i, mod), pow(b, i, mod))
    if j == '-':
        cur *= -1
    su = add(su, cur)

geo = period_pow(a, b, k, (n + 1) // k - 1)
print(mult(su, geo))
