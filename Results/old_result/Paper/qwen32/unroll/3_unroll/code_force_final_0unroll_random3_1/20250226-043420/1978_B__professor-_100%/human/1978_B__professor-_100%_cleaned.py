t = int(input())
for _ in range(t):
    (n, a, b) = map(int, input().split())
    if b <= a:
        print(n * a)
    elif b - a >= n:
        print(int((2 * b - n + 1) * n // 2))
    else:
        print(int((b - a) * (b - a + 1) // 2 + a * n))