mod=998244353

c=[[0]*2000 for i in range(2000)]
c[0][0]=1
for i in range(1,1005):
    c[i][0] = 1
    c[i][i] = 1
    for j in range(1, i):
        c[i][j] = c[i-1][j] + c[i-1][j-1]
        c[i][j]%=mod

def getc(n, k):
    if k>n:
        return 0
    return c[n][k]

n = int(raw_input())
src=map(int, raw_input().split())
# n=3
# src=[2,1,1]
# n=4
# src=[1,1,1,1]

dp=[0]*(n+1)
dp[n] = 1

for i in range(n-1, -1, -1):
    if src[i] < 1:
        continue
    for j in range(i+1, n+1):
        dp[i] += dp[j] * getc(j-i-1, src[i])
        dp[i]%=mod

print (sum(dp)-1)%mod
