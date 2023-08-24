N = int(1e5 + 7)
g = [[] for _ in range(N)]
topo = []
Main = []
vis = [False for _ in range(N)]

def DFS(node):
    vis[node] = True
    for child in g[node]:
        if not vis[child]:
            DFS(child)
    topo.append(node)

if __name__ == "__main__":
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    Main.extend(x)
    
    for i in range(1, n+1):
        v = list(map(int, input().split()))[1:]
        g[i].extend(v)
    
    for i in range(k):
        if not vis[Main[i]]:
            DFS(Main[i])

    idx = [0 for _ in range(n+2)]
    
    for i in range(len(topo)):
        idx[topo[i]] = i
    
    for i in range(len(topo)):
        for child in g[topo[i]]:
            if idx[topo[i]] < idx[child]:
                print(-1)
                exit()
    print(len(topo))
    print(" ".join(map(str, topo))+' ')

