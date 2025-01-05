def func_1(be, en):
    res = [1]
    for i in range(be, en + 1):
        res.append(mult(res[-1], i))
    return res

def func_2(n, r):
    if n < r:
        return 0
    return div(facs[n], facs[n - r])

def func_3(arr):
    tem = [0]
    for i in range(len(arr)):
        tem.append(tem[i] + arr[i])
    return tem

def func_4():
    import os, sys, atexit
    from cStringIO import StringIO as BytesIO
    sys.stdout = BytesIO()
    atexit.register(lambda : os.write(1, sys.stdout.getvalue()))
    return BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = func_4()
add = lambda a, b: (a + b) % mod
mult = lambda a, b: a * b % mod
div = lambda a, b: mult(a, inv(b))
inv = lambda a: pow(a, mod - 2, mod)
rints = lambda : [int(x) for x in input().split()]
mod = 998244353
(n, k) = rints()
a = [rints() for _ in range(n)]
(disbe, disen, ans) = (set(), set(), 0)
facs = func_1(1, 3 * 10 ** 5)
for (l, r) in a:
    disbe.add(l)
    disbe.add(r)
disbe = sorted(disbe)
ordbe = defaultdict(int, {disbe[i]: i for i in range(len(disbe))})
(cumbe, cumen) = ([0] * len(disbe), [0] * len(disbe))
for (l, r) in a:
    cumbe[ordbe[l]] += 1
    cumen[ordbe[r]] += 1
(cumbe, cumen) = (func_3(cumbe), func_3(cumen))
for i in disbe[1:-1]:
    cur = cumbe[ordbe[i] + 1] - cumbe[ordbe[i]]
    val = cumbe[-1] - cumbe[ordbe[i] + 1]
    val += cumen[ordbe[i]]
    all = n - val
    ans = add(ans, add(func_2(all, k), -func_2(all - cur, k)))
print(div(ans, facs[k]))