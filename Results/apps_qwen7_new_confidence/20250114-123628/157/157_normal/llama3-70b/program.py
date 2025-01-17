import math

X = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for a in range(1, X + 1):
    b = X // a
    if a * b == X and gcd(a, b) == 1:
        print(a, b)
        break
