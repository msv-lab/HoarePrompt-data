n, k, m = map(int, input().split())
ans = pow(10, n - 1, m)
ans = (ans * (k - (ans - 1) % k)) % m
print(ans)
