(n, a, b, p, q) = map(int, input().split())

def func_1(x, y):
    from math import gcd
    return x * y // gcd(x, y)
red_tiles = n // a
blue_tiles = n // b
both_tiles = n // func_1(a, b)
max_chocolates = red_tiles * p + blue_tiles * q - both_tiles * min(p, q)
print(max_chocolates)