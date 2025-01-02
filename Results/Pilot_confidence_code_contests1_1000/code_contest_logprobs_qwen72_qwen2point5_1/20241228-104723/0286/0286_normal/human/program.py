
import sys,heapq
#sys.stdin=open("data.txt")
input=sys.stdin.readline

# heap
avail=[]

n,m=map(int,input().split())
indeg=[0]*n

g=[[] for _ in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    indeg[v-1]+=1
    g[u-1].append(v-1)

for i in range(n):
    if indeg[i]==0:
        heapq.heappush(avail,i)

# label nodes
ans=[0]*n
label=1

while avail:
    u=heapq.heappop(avail)
    ans[u]=label
    label+=1
    for v in g[u]:
        indeg[v]-=1
        if indeg[v]==0:
            heapq.heappush(avail,v)

print(" ".join(map(str,ans)))
