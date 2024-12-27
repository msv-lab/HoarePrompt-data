n,x=map(int,raw_input().split())
a=map(int,raw_input().split())
ans=float('inf')
b=[[float('inf')]*n for _ in xrange(n)]
for i in xrange(n):
    b[i][0]=a[i]
for i in xrange(n):
    for j in xrange(1,n):
        b[i][j]=min(b[i][j-1],a[(i-j)%n])
for j in xrange(n):
    tmp=0
    for i in xrange(n):
        tmp+=b[i][j]
    ans=min(ans,tmp+j*x)
print(ans)