def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())

count = 1  # Initialize count to 1
while b > 0:
    g = gcd(a, b)
    b -= g
    count += 1

print(count - 1)  # Subtract 1 from count to correct the output