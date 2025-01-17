n, a, b, p, q = map(int, input().split())
lcm = a * b // math.gcd(a, b)
red = n // a * p
blue = n // b * q
both = n // lcm * min(p, q)
print(red + blue - both)
