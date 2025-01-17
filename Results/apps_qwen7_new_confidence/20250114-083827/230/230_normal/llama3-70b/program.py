n = int(input())
a = list(map(int, input().split()))
a.sort()
mid = a[n // 2]
res = 0
for x in a:
    res += abs(x - mid)
if res % 2 == 0:
    print("YES")
else:
    print("NO")
