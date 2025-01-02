from __future__ import print_function

m = int(raw_input())

def recurse(m):
    if m == 0:
        return 0, 0
    l = 0
    h = m + 1
    while l + 1 != h:
        mid = (l + h) / 2
        if mid ** 3 <= m:
            l = mid
        else:
            h = mid
    a = l
    one = m - a ** 3
    two = a ** 3 - 1 - (a - 1) ** 3
    if one >= two:
        return map(sum, zip(recurse(one), (1, a ** 3)))
    else:
        return map(sum, zip(recurse(two), (1, (a - 1) ** 3)))

print(*recurse(m))
