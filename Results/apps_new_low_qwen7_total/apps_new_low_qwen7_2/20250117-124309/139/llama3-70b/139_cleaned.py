(n, a, b, c) = map(int, input().split())
k = 4 - n % 4
if k == 4:
    k = 0
ans = float('inf')
for i in range(k // 3 + 1):
    j = (k - 3 * i) // 2
    if 3 * i + 2 * j <= k:
        ans = min(ans, 3 * i * c + j * b + (k - 3 * i - 2 * j) * a)
print(ans)