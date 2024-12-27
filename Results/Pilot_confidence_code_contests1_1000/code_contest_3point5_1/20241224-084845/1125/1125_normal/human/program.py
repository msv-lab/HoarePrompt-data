def gcd(a, b):
    c = a % b
    return gcd(b, c) if c else b
h = {j: i for i, j in enumerate('abcdefghijklmnopqrstuvwxyz')}
n, m = map(int, raw_input().split())
x, y = raw_input(), raw_input()
a, b = len(x), len(y)
s, c = 0, gcd(a, b)
u, v = range(0, a, c), range(0, b, c)
if a == c:
    if b == c:
        for i in range(c): s += int(y[i] == x[i])
    else:
        for i in range(c):
            for j in v: s += int(y[j + i] == x[i])
if b == c:
    for i in range(c):
        for j in u: s += int(x[j + i] == y[i])
else:
    t, d = [0] * (26 * c), 0
    for i in range(c):
        for j in u: t[d + h[x[j + i]]] += 1
        for j in v: s += t[d + h[y[j + i]]]
        d += 26
print(n * a - (m * c * s) // a)