n, s = map(int, input().split())
v = list(map(int, input().split()))

v.sort()

low, high = 0, min(v)

while low < high:
    mid = (low + high + 1) // 2
    total = sum(min(mid, x) for x in v)
    if total < s:
        low = mid
    else:
        high = mid - 1

if sum(min(low, x) for x in v) != s:
    print(-1)
else:
    print(low)
