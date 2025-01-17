n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 360
tot = 0
for i in range(n):
    tot += a[i]
    ans = min(ans, abs(tot - (360 - tot)))
print(ans)
