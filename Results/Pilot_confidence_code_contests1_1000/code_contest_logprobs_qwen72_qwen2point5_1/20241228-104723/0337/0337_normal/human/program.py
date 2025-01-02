n = int(input())
a = list(map(int, input().split()))

ans = 0
max_ = 0
for i in range(n):
    ans += max(max_ - a[i], 0)
    max_ = max(max_, a[i])
print(ans)