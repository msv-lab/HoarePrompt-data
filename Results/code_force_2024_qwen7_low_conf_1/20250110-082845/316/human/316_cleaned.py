t = int(input())
for _ in range(t):
    (n, a, b) = map(int, input().split())
    if n == 1:
        e = a
    else:
        c = a * n
        d = b + (n - 2) * a
        e = min(c, d)
    print(e)