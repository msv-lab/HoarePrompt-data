n, k = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    if i != k:
        ans += 2 * abs(i - k) + 2
    else:
        ans += 2
print(ans)
