MOD = 10**9 + 7
a, b, k, t = map(int, input().split())
ans = 0
for i in range(-k, k+1):
    if a + i > b:
        ans += (2*k + 1)**(t-1)
ans %= MOD
print(ans)
