(n, k, t) = map(int, input().split())
print(min(t, k) if t <= n else k - (t - n) % k)