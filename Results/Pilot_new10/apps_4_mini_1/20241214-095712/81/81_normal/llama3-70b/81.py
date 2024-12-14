def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

l, r, x, y = map(int, input().split())

count = 0
for a in range(l, r + 1):
    for b in range(a, r + 1):
        if gcd(a, b) == x and lcm(a, b) == y:
            count += 1

print(count)
