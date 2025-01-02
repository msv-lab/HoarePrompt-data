class BIT():
    def __init__(self,size):
        self.size=size
        self.node=[0]*(size+1)

    def sum(self,idx):
        ret=0
        while idx>0:
            ret+=self.node[idx]
            idx-=idx&(-idx)
        return ret

    def add(self,idx,x):
        while idx<=self.size:
            self.node[idx]+=x
            idx+=idx&(-idx)

n,m=map(int,raw_input().split())
L=[[] for _ in xrange(m+1)]
for i in xrange(n):
    l,r=map(int,raw_input().split())
    r+=1
    L[r-l].append(l)
bit=BIT(m+1)
total=0
for d in xrange(1,m+1):
    for l in L[d]:
        r=l+d
        bit.add(l,1)
        bit.add(r,-1)
    total+=len(L[d])
    ans=n-total
    now=0
    while now<=m:
        ans+=bit.sum(now)
        now+=d
    print(ans)