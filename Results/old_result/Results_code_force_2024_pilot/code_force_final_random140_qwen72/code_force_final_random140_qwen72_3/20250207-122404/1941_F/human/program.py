import bisect
import heapq
from math import inf
 
for _ in range(int(input())):
    n, m, k = [*map(int, input().split())]
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    f = [*map(int, input().split())]
    gap = [(y - x, x, y) for y, x in zip(a[1:], a)]
    gap.sort(reverse=True)
    start = gap[0][1]
    end = gap[0][2]
    mid = (start + end) // 2
    # print(start,end,mid)
    nd = 0 if len(gap) == 1 else gap[1][0]
    b.sort()
    f.sort()
    # print(b, f)
    res = inf
    for i in range(m):
        remain = mid - b[i]
        j = bisect.bisect_left(f, remain)
        if j == k:
            s = f[j - 1] + b[i]
            if start < s < end:
                res = min(res, max(end - s, s - start, nd))
        else:
            s = f[j] + b[i]
            if start < s < end:
                res = min(res, max(end - s, s - start, nd))
            if j >= 1:
                s = f[j - 1] + b[i]
                if start < s < end:
                    res = min(res, max(end - s, s - start, nd))
 
    # print(num_in_range)
    if res == inf:
        print(gap[0][0])
    else:
        print(res)