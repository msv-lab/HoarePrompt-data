(n, a) = map(int, input().split())
if a <= n // 2:
    print(a // 2 + a % 2)
else:
    print((n - a + 1) // 2 + (n - a + 1) % 2)