(n, m, k) = map(int, input().split())
k %= n * 2 - 2
if k < n - 1:
    print(k + 1, 1)
elif k < n * 2 - 2:
    print(n - (k - n + 1) % (n - 1) - 1, (k - n + 1) // (n - 1) + 1)
else:
    print(1, 2)