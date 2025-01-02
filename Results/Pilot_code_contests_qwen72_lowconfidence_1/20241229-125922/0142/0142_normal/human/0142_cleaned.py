(a, b) = (int(s) for s in raw_input().split())
g = gcd(a, b)
a /= g
b /= g

def func_1(n):
    res = 0
    div = [2, 3, 5]
    for d in div:
        while n % d == 0:
            n /= d
            res += 1
    return (n, res)
(a, x) = func_1(a)
(b, y) = func_1(b)
if a != b:
    print(-1)
else:
    print(x + y)