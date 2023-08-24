def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def find_fraction(n):
    for b in range(n-1, 0, -1):
        a = n - b
        if gcd(a, b) == 1:
            return a, b
    return -1, -1

n = int(input())
a, b = find_fraction(n)
print(a, b)