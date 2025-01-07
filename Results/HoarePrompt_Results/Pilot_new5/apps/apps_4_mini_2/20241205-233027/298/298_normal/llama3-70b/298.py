import math

n, m, k = map(int, input().split())

if (n*m) % k:
    print("NO")
    exit()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euk(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = euk(b, a % b)
        return y, x - (a // b) * y

def bezout(a, b):
    x, y = euk(a, b)
    return x, y, x*a + y*b

n1, m1, g = bezout(n, m)
if abs(n1*m) >= g:
    print("YES")
    print(0, 0)
    print(0, n1*m//g)
    print(m1*m//g, 0)
else:
    print("NO")