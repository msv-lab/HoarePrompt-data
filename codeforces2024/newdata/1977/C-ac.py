from math import gcd
from collections import defaultdict

def lcm(x, y):
    return x*y//gcd(x, y)

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    if any(mx%x for x in a):
        return n
    dp = defaultdict(int)
    dp[0] = 0
    for x in a:
        for y, cnt in list(dp.items()):
            l = lcm(x, y) or x
            dp[l] = max(dp[l], cnt+1)
    lookup = set(a)
    return max(cnt for x, cnt in dp.items() if x not in lookup)

for _ in range(int(input())):
    print(solution())