from collections import defaultdict

n, k = map(int, raw_input().split())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
dp1 = defaultdict(lambda: 0, {0 : 0})
pos = 0
for a, b in zip(A, B):
    cur = a - b * k
    dp2 = dp1.copy()
    for x, y in dp1.iteritems():
        dp2[x + cur] = max(dp2[x + cur], y + a)
    dp1 = dp2
if dp1[0] > 0:
    print(dp1[0])
else:
    print(-1)