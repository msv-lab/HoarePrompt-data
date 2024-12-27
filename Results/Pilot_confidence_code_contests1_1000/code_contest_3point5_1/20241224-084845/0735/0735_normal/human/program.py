n=int(raw_input())
ab=[map(int,raw_input().split()) for _ in xrange(n)]
cnt=0
for i in xrange(n-1,-1,-1):
    a,b=ab[i][0],ab[i][1]
    if (a+cnt)%b==0:continue
    cnt+=b-(a+cnt)%b
print(cnt)