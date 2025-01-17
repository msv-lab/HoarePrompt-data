a, b, c = map(int, input().split())
if c % a == 0 or c % b == 0 or (a != b and c % gcd(a, b) == 0):
    print("Yes")
else:
    print("No")

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
