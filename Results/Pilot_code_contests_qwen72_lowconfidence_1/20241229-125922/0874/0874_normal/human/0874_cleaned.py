def func_1():
    (be, en, ans) = (l, 10 ** 7, -1)
    while be <= en:
        md = be + en >> 1
        all = a * (md - l + 1) + b * (sum_n(md - 1) - sum_n(max(l - 2, 0)))
        val = max(ceil1(all, m), a + (md - 1) * b)
        if val <= t:
            be = md + 1
            ans = md
        else:
            en = md - 1
    return ans
ceil1 = lambda a, b: (a + b - 1) // b
sum_n = lambda n: n * (n + 1) // 2
rints = lambda : [int(x) for x in stdin.readline().split()]
(a, b, n) = rints()
(qur, out) = ([rints() for _ in range(n)], [])
for (l, t, m) in qur:
    out.append(func_1())
print('\n'.join(map(str, out)))