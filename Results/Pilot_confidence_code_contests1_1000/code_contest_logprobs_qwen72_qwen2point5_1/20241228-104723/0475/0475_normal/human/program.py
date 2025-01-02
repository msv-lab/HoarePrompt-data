import sys,math
from fractions import gcd
from bisect import bisect_left, bisect
from collections import defaultdict
from io import BytesIO
sys.stdin = BytesIO(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')
n = int(input())
#arr = [int(_) for _ in input().split()]

dv = defaultdict(set)
dp = defaultdict(int)

for i in range(n-1):
    s,f = [int(_) for _ in input().split()]
    dv[s].add(f)
    dp[f] = s
arr = [0] * (n+1)
lv = set()
for i in range(1,n+1):
    if i not in dv:
        lv.add(i)
    if i not in dp:
        head = i
mlt = 1
mod = 998244353
while len(lv):
    cur = lv.pop()
    if cur == head:
        break
    arr[dp[cur]] += 1
    dv[dp[cur]].remove(cur)
    if len(dv[dp[cur]]) == 0:
        lv.add(dp[cur])
    while arr[cur] > 0:
        mlt = mlt * (arr[cur] + 1)
        arr[cur] -= 1
        mlt %= mod

while arr[cur] > 1:
    mlt = mlt * (arr[cur])
    arr[cur] -= 1
    mlt %= mod
mlt *= n
print(mlt % mod)