import math


def div(n, d):
    q, r = 0, n
    while r >= d:
        q = q+1
        r = r-d
    return [q, r]


nums = [int(x) for x in raw_input().split()]  # r, h
r, h = float(nums[0]), nums[1]
# For the lower part it's to count how many times does r fit in h.
[n, d] = div(h, r)  # Post: h = n*r + d, d >= 0.
if d < r/2:
    print(2*n+1)
else:
    x = math.sqrt((r**2)-(r/2)**2)
    if x+r+n*r <= h+r:
        print(2*n+3)
    else:
        print(2*n+2)
