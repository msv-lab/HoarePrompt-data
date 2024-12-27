h,w=map(int,raw_input().split())
c=[[1]*(w+1)]+[[1]+map(int,raw_input().split()) for _ in xrange(h)]
dp=[[0]*(w+1) for i in xrange(h+1)]
for i in xrange(h):
	for j in xrange(w):
		if c[i+1][j+1]==0:
			dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j],dp[i][j])+1
print(max(max(dp)))