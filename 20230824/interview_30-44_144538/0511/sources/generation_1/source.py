
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

x, y = map(int, input().split())

count = 0
while y > 0:
    g = gcd(x, y)
    count += 1
    y -= g

print(count)
