def func_1(a, b):
    if b == 0:
        return (1, 0)
    if a < b:
        (c, d) = func_1(b, a)
        return (d, c)
    if a % b == 0:
        return (1, -(a // b - 1))
    (c, d) = func_1(b, a % b)
    return (d, c - a // b * d)

def func_2(a, b):
    (c, d) = func_1(b, 1000000007)
    return c * a % 1000000007
facts = [1]
ch = 1
for i in range(1, 200002):
    ch *= i
    ch %= 1000000007
    facts.append(ch)
for _ in range(int(input())):
    (n, m1, m2) = map(int, input().split())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))
    if p[-1] != s[0] or p[0] != 1 or s[-1] != n:
        print(0)
    else:
        ans = 1
        kol = n
        for x in s:
            cnk = func_2(facts[kol - 1], facts[n - x] * facts[kol - 1 + x - n])
            ans *= cnk
            ans %= 1000000007
            kol = n - x
        kol = s[0] - 1
        p2 = []
        for i in range(m1 - 2, -1, -1):
            p2.append(p[i])
        for x in p2:
            cnk = func_2(facts[kol - 1], facts[x - 1] * facts[kol - x])
            ans *= cnk
            ans %= 1000000007
            kol = x - 1
        print(ans)