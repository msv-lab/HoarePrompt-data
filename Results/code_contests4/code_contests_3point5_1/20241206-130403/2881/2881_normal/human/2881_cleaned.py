def func_1(be, en):
    while be < en:
        mid = (be + en + 1) // 2
        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1
    print(be * x, be * y)
rints = lambda : [int(x) for x in stdin.readline().split()]
(a, b, x, y) = rints()
g = gcd(x, y)
x //= g
y //= g
mi = min(a // x, b // y)
print(mi * x, mi * y)