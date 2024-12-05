import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())

k = 0
min_lcm = lcm(a, b)

while True:
    if lcm(a + k, b + k) < min_lcm:
        min_lcm = lcm(a + k, b + k)
    else:
        break
    k += 1

print(k - 1)
