from collections import defaultdict
import sys
input=sys.stdin.readline

def find(x):
    while p[x]!=x:
        x=p[p[x]]
    return(x)
def union(u,v):
    a=find(u)
    b=find(v)
    if (sz[a]>sz[b]):
            p[b]=a
            special[a]+=special[b]
            if special[a]==k:
                return(1)
    elif (sz[a]<sz[b]):
            p[a]=b
            special[b]+=special[a]
            if special[b]==k:
                return(1)
    else:
        p[b]=a
        sz[a]+=1
        special[a]+=special[b]
        if special[a]==k:
            return(1)
    
    return(0)

n,m,k=map(int,input().split())
ind=[int(i) for i in input().split() if i!='\n']
special=[0]*(n)
for i in range(k):
    special[ind[i]-1]=1
p=[i for i in range(n)]
store=[]
sz=[0]*(n)
for i in range(m):
    x,y,w=map(int,input().split())
    store.append([w,x-1,y-1])
store.sort()
i=0
while True:
    g=find(store[i][1])
    h=find(store[i][2])
    if g!=h:
        t=union(store[i][1],store[i][2])
        if t==1:
            x=store[i][0]
            break
    i+=1
ans=[x for i in range(k)]
ans=' '.join(map(str,ans))
sys.stdout.write(ans)
        
    
    
           
                
    

    
