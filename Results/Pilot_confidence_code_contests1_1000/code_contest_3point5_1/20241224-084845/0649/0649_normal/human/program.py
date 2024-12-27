from collections import deque
import sys
sys.setrecursionlimit(10**6)

def bfs1(c):
    visited[c]=1
    q=deque([c])
    while len(q)>0:
        p=q.popleft()
        for i in v[p]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1
                d[c][i]=d[c][p]+1

def bfs2(c1,c2):
    visited[c2]=1
    bfs1(c1)
    bfs1(c2)

n,k=map(int,raw_input().split())
d=[[0]*n for _ in xrange(n)]
v=[[] for _ in xrange(n)]
e=[]
for i in xrange(n-1):
    a,b=map(int,raw_input().split())
    a-=1
    b-=1
    v[a].append(b)
    v[b].append(a)
    e.append([a,b])
if k%2==0:
    min_del=1000000
    for i in xrange(n):
        cnt=0
        visited=[0]*n
        bfs1(i)
        for j in xrange(n):
            if d[i][j]>k/2:
                cnt+=1
        min_del=min(min_del,cnt)
    print(min_del)
else:
    min_del=1000000
    for i,j in e:
        cnt=0
        visited=[0]*n
        d=[[0]*n for _ in xrange(n)]
        bfs2(i,j)
        for l in xrange(n):
            if d[i][l]>(k-1)/2 or d[j][l]>(k-1)/2:
                cnt+=1
        min_del=min(min_del,cnt)
    print(min_del)