import sys

sys.setrecursionlimit(60000)
try:    
    def dfs(d,curr,parent):
        d[curr].remove(parent)
        for i in d[curr]:
            dfs(d,i,curr)
    
    def solve(d,curr,colors,count):
        if d[curr]!=set():
            for i in d[curr]:
                if colors[curr-1]!=colors[i-1]:
                    count[0]+=1 
                solve(d,i,colors,count)
            
    
    n=int(input())
    connections=list(map(int,input().split()))
    colors=list(map(int,input().split()))
    d={}
    for i in range(n-1):
        a=i+2
        b=connections[i]
        if a in d.keys():
            d[a].add(b)
        else:
            d[a]=set([b])
        if b in d.keys():
            d[b].add(a)
        else:
            d[b]=set([a])
    #print(d)
    d[1].add(-1)
    dfs(d,1,-1)
    #print(d)
    count=[1]
    solve(d,1,colors,count)
    print(count[0])
except:
    print(0)