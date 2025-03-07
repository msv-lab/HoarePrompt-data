for _ in range(int(input())):
    (n, a, b) = map(int, input().split())
    k = min(n, b - a)
    if b <= a:
        print(a * n)
    else:
        print(b * k - k * (k - 1) // 2 + (n - k) * a)