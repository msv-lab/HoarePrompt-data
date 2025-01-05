from audioop import reverse

test=int(input())
while test:
    test-=1
    n=int(input())
    arr=list(map(int,input().split()))
    def construct(temp):
        res=[0]*n
        p=[]
        q=[]
        for i in range(n-1):
            if i&1:
                p.append((temp[i],i))
            else:
                q.append((temp[i],i))
        q.append((temp[-1],n-1))
        p.sort()
        q.sort()
        p=p+q
        val=n
        for _,st in p:
            res[st]=val
            val-=1
        for i in range(1,n-1,2):
            if res[i]+temp[i]<=max(res[i-1]+temp[i-1],res[i+1]+temp[i+1]):
                return 0
        return res
    t=construct(arr)
    if t==0:
        t=construct(arr[::-1])
        t=t[::-1]
    print(' '.join(map(str,t)))
