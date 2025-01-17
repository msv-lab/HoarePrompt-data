n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()
res = float('inf')
l, r = 1, max(h)

while l <= r:
    mid = (l + r) // 2
    cnt = sum(max(0, hi - mid) for hi in h)
    if cnt <= k:
        res = min(res, len(h) - h.index(mid) - (h.count(mid) - 1))
        r = mid - 1
    else:
        l = mid + 1

print(res)
