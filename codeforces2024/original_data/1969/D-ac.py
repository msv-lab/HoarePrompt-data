import heapq
t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    arr_a=list(map(int,input().split()))
    arr_b=list(map(int,input().split()))
    ans=0
    tot=0
    stc=[]
    for a,b in zip(arr_a,arr_b):
        if b-a>=0:
            tot+=b-a
            heapq.heappush(stc,(-1*b,-1*a))
    tot_cut=0
    d=[]
    while len(d)<k and len(stc):
        b,a=heapq.heappop(stc)
        b,a=-b,-a
        tot_cut+=b
        heapq.heappush(d,(-1*a,-1*b))
    ans=max(ans,tot-tot_cut)
    while len(stc)>k and len(d):
        a,b=heapq.heappop(d)
        a,b=-a,-b
        tot-=b-a
        tot_cut-=b
        b,a=heapq.heappop(stc)
        b,a=-b,-a
        tot_cut+=b
        heapq.heappush(d,(-1*a,-1*b))
        ans=max(ans,tot-tot_cut)
    print(ans)