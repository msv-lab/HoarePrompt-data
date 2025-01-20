(n, m, a, b) = map(int, input().split())
r = n % m
if r == 0:
    print(0)
elif m - r <= n:
    print(min((m - r) * a, r * b))
else:
    print((m - r) * a)