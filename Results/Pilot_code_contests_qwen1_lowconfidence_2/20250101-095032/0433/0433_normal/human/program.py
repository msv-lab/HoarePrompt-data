import bisect
n=input()
a=[input() for i in xrange(n)]
dp=[float('inf') for _ in xrange(n)]
for i in xrange(n):
    dp[bisect.bisect_left(dp,a[i])]=a[i]
for i in xrange(n):
    if dp[i]==float('inf'):
        print(i)
        break