mod = int(1000000000.0 + 7)
fac = [1]

def func_1(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def func_2(a, b):
    return (a - b) % mod

def func_3(a, b):
    return a * b % mod

def func_4(a, b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return func_3(a, func_4(a, b - 1))
    else:
        temp = func_4(a, b / 2)
        return temp * temp

def func_5(a):
    return func_4(a, mod - 2)

def func_6(n, k, fac):
    if k > n:
        return 0
    return func_3(fac[n], func_5(func_3(fac[n - k], fac[k])))

def func_7():
    (n, k) = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]
    fac = [0] * (n + 5)
    fac[0] = 1
    for i in range(1, n + 5):
        fac[i] = func_3(fac[i - 1], i)
    a.sort()
    ans = 0
    for i in range(n - 1):
        diff = func_2(a[i + 1], a[i])
        ways = func_6(n, k, fac)
        ways = func_2(ways, func_6(i + 1, k, fac))
        ways = func_2(ways, func_6(n - i - 1, k, fac))
        ans = func_1(ans, func_3(diff, ways))
    print(ans)
func_7()