t = int(input())
for steps in range(t):
    (a, b) = map(int, input().split())
    (c, d) = map(int, input().split())
    (e, f) = map(int, input().split())
    (g, h) = map(int, input().split())
    n = (a - e) * (a - e) + (b - f) * (b - f)
    x = (c - g) * (c - g) + (d - h) * (d - h)
    if x > n:
        print(n)
    else:
        print(x)