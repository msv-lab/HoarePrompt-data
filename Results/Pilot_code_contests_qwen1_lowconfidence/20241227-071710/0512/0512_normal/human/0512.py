import os
from io import BytesIO

input = BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, k = map(int, input().split())
a = [int(i) for i in input().split()]

dp = [False] * (k + 1)

for ai in a:
    dp[ai] = True

for i in xrange(max(a) + 1, k + 1):
    dp[i] = any(not dp[i - ai] for ai in a)

os.write(1, 'First' if dp[k] else 'Second')