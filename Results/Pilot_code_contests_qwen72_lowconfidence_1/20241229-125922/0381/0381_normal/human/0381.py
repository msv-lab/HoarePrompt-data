n,k=map(int,raw_input().split())
a=map(int,raw_input().split())
total=[0]*(n+1)
asum=[0]*(n+1)
for i in xrange(n):
    asum[i+1]=asum[i]+a[i]
    if a[i]>0:
        total[i+1]=total[i]+a[i]
    else:
        total[i+1]=total[i]
ans=0
for i in xrange(n-k+1):
    tmp=asum[i+k]-asum[i]
    ans=max(ans,tmp+total[i]+total[n]-total[i+k],total[i]+total[n]-total[i+k])

print(ans)
