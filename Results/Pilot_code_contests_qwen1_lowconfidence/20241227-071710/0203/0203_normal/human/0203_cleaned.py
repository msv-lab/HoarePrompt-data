MOD = 10 ** 9 + 7

def func_1(a, b):
    if a % b == 0:
        return b
    return func_1(b, a % b)
n = int(raw_input())
ns = []
d = defaultdict(int)
for i in xrange(n):
    (a, b) = map(int, raw_input().split())
    ns.append((a, b))
    if a and b:
        s = 1 if a * b >= 0 else -1
        g = func_1(abs(a), abs(b))
        m1 = (s * abs(a) / g, abs(b) / g)
        m2 = (-s * abs(b) / g, abs(a) / g)
    elif a == 0 and b == 0:
        continue
    elif a == 0:
        m1 = (1, 0)
        m2 = (0, 1)
    elif b == 0:
        m1 = (0, 1)
        m2 = (1, 0)
    d[m1] += 1
    d[m2] += 0
pre = 1
for k in d.keys():
    if k[0] < 0:
        assert (k[1], -k[0]) in d
        continue
    elif k[0] == 0:
        pre = pre * d[k] % MOD
    else:
        k1 = k
        k2 = (-k[1], k[0])
        tot = pow(2, d[k1], MOD) + pow(2, d[k2], MOD) - 1
        pre = pre * tot % MOD
print(pre - 1 + MOD) % MOD