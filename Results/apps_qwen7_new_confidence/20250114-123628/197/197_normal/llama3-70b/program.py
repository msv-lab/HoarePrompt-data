MOD = 10**9 + 7
x, k = map(int, input().split())
ans = x
for _ in range(k):
    ans = (ans * 2) % MOD
    ans = (ans + ans) // 2 % MOD
print(ans)
