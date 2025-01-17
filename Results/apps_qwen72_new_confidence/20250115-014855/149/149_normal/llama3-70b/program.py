n, a, x, b, y = map(int, input().split())
if (x - a) % (n - 1) == (y - b) % (n - 1):
    print("YES")
else:
    print("NO")
