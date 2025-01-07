n, m, k = map(int, input().split())
if k == 1:
    print(min(m // n, m - (n - 1)))
else:
    print(min(m // n + 1, m - (n - k)))
