from sys import stdin, stdout
from collections import Counter, defaultdict
pr=stdout.write
raw_input  = stdin.readline
def ni():
    return int(raw_input())


def li():
    return list(map(int,raw_input().split()))


def pn(n):
    stdout.write(str(n)+'\n')


def pa(arr):
    pr(' '.join(map(str,arr))+'\n')

# fast read function for total integer input

def inp():
    # this function returns whole input of
    # space/line seperated integers 
    # Use Ctrl+D to flush stdin.
    return (map(int,stdin.read().split()))
    
range = xrange # not for python 3.0+

# main code
n,m=li()
d=[[] for i in range(n+1)]
for i in range(m):
    u,v=li()
    d[u].append(v)
    d[v].append(u)
arr=[]
vis=[0]*(n+1)
for i in range(1,n+1):
    if not vis[i]:
        vis[i]=1
        q=[i]
        mn=i
        mx=i
        
        while q:
            x=q.pop()
            mn=min(mn,x)
            mx=max(mx,x)
            for j in d[x]:
                if not vis[j]:
                    vis[j]=1
                    q.append(j)
        arr.append((mn,mx))
ans=0
px,py=arr[0]
n1=len(arr)
for i in range(1,n1):
    x,y=arr[i]
    if x<=py:
        ans+=1
        
    px=min(x,px)
    py=max(y,py)
pn(ans)
