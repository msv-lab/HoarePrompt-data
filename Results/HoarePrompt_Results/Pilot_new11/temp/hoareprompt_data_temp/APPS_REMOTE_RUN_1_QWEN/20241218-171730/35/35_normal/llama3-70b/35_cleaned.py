(n, a, b) = map(int, input().split())
x = min(n, a, b)
while True:
    if a >= x and b >= x and (a - x + (b - x) >= x):
        break
    x -= 1
print(x)