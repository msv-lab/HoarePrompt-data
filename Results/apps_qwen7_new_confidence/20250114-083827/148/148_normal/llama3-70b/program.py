n, c0, c1 = map(int, input().split())
ans = 0
i = 0
while (1 << i) < n:
    ans += (1 << i) * min(c0, c1)
    i += 1
if (1 << i) > n:
    ans += (n - (1 << (i - 1))) * min(c0, c1)
print(ans)
