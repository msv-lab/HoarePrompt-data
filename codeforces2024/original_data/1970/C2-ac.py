import collections

for _ in range(1):
    n,t = map(int,input().split())
    d = collections.defaultdict(list)
    for i in range(n-1):
        x,y = map(int,input().split())
        d[x].append(y)
        d[y].append(x)
    st = int(input())
    q = collections.deque()
    q.append([st,0])
    vis = {st:1}
    ans = "Hermione"
    def dfs(node,name,par):
        ans = False
        for x in d[node]:
            if x not in vis:
                vis[x] = name
                dfs(x,1-name,node)
        
        for x in d[node]:
            if vis[x] == name and x!= par:
                ans = True
        # print(node,name,vis)
        if  ans:
            vis[node] = name
        
            
        return vis[node]
    dfs(st,0,-1)
    # print(vis)
    if vis[st]:
        print("Hermione")
    else:
        print("Ron")