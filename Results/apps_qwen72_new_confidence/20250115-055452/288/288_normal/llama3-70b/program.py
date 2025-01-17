n, k = map(int, input().split())

min_good = max(0, k-1)
max_good = min(k, n-k)

print(min_good, max_good)
