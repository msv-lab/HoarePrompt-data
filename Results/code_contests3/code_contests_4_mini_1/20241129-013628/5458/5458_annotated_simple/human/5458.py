mod=100000
while 1:
    n,m,s=map(int,raw_input().split())
    if n==m==s==0:break
    dp=[[[0]*(s+1) for _ in xrange(m+2)] for _ in xrange(2)]
    for i in xrange(n**2):
        for j in xrange(1,m+1):
            for k in xrange(1,s+1):
                if i==0:
                    if j>=k:
                        dp[(i+1)&1][j+1][k]=1
                else:
                    if j>k:
                        dp[(i+1)&1][j+1][k]=dp[(i+1)&1][j][k]
                        continue
                    dp[(i+1)&1][j+1][k]=(dp[(i+1)&1][j][k])%mod
                    dp[(i+1)&1][j+1][k]+=(dp[i&1][j][k-j])%mod
    print(dp[(n**2)&1][m+1][s]%mod)