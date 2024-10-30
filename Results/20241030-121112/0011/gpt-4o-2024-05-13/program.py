n, a, b, p, q = map(int, input().split())

def lcm(x, y):
    from math import gcd
    return x * y // gcd(x, y)

red_tiles = n // a
blue_tiles = n // b
both_tiles = n // lcm(a, b)

# Since the tiles that can be painted both Red or Blue can only be counted once, we need to subtract them once
max_chocolates = red_tiles * p + blue_tiles * q - both_tiles * min(p, q)

print(max_chocolates)
