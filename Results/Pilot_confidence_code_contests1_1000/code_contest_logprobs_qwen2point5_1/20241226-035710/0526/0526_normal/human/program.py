n,m=map(int,raw_input().split())

mod=(10**9)+7
dp=[0]*100005

if n>m:
	n,m=m,n

dp[0],dp[1],dp[2]=0,2,4

for i in xrange(3, m+1):
	dp[i]=dp[i-1]+dp[i-2]
	dp[i]%=mod
print (dp[n]+dp[m]-2+mod)%mod