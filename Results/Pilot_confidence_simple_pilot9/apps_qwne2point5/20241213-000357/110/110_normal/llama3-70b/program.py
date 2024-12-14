n, m, r, k = map(int, input().split())
ans = min(k, (n - r + 1) * (m - r + 1))
print(ans / ((n - r + 1) * (m - r + 1)))
