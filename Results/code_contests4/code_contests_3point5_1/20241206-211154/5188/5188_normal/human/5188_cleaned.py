(n, m, l, r) = map(int, raw_input().split())

def func_1(a, b):
    if a > b:
        return a - b
    return b - a
if l % 2 and r % 2:
    o = (r - l) / 2 + 1
    e = o - 1
elif l % 2 + r % 2:
    o = (r - l) / 2 + 1
    e = o
else:
    e = (r - l) / 2 + 1
    o = e - 1
mod = 998244353
s = pow(o + e, m * n) + pow(e - o, m * n)
s %= mod
p = pow(2, mod - 2, mod)
print(s * p) % mod