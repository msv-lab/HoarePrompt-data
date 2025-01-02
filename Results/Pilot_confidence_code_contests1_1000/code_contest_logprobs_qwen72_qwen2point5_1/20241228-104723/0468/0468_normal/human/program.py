import bisect

n=int(raw_input())
x=map(int,raw_input().split())+[float('inf')]
l=int(raw_input())
q=int(raw_input())
r=[[0]*20 for _ in xrange(n)]

for i in xrange(n):
    if x[i]+l==x[bisect.bisect_left(x,x[i]+l)]:
        r[i][0]=bisect.bisect_left(x,x[i]+l)
    else:
        r[i][0]=bisect.bisect_left(x,x[i]+l)-1

for k in xrange(19):
    for i in xrange(n):
        r[i][k+1]=r[r[i][k]][k]
        
for i in xrange(q):
    a,b=map(int,raw_input().split())
    a-=1
    b-=1
    ans=0
    if a>b:
        a,b=b,a
    while 1:
        if bisect.bisect_left(r[a],b)>=1:
            ans+=1<<(bisect.bisect_left(r[a],b)-1)
            a=r[a][bisect.bisect_left(r[a],b)-1]
        else :
            ans+=1<<bisect.bisect_left(r[a],b)
            break
    print(ans)