import sys
from collections import deque, defaultdict

# Fast input reading
input = lambda: sys.stdin.readline().rstrip()

def ii():
    return int(input())

def mi():
    return map(int, input().split())

def li():
    return list(map(int, input().split()))

def si():
    return input()

def lsi():
    return input().split()

# Read number of test cases
t = ii()
for _ in range(t):
    # Read number of stations (nodes) and routes (edges)
    n, m = mi()

    # Initialize graph and color nodes mapping
    graph = [[] for i in range(n + 1)]
    conodes = defaultdict(set)
    
    # Read each edge and populate the graph and color nodes
    for line in range(m):
        u, v, c = mi()
        graph[u].append((v, c))
        graph[v].append((u, c))
        conodes[c].add(u)
        conodes[c].add(v)
    
    # Read departure and destination stations
    b, e = mi()
    
    # Initialize BFS
    queue = deque([b])
    visited = [0] * (n + 1)
    visited[b] = 1
    colvis = set()
    lines = 0
    
    # Perform BFS
    while queue:
        if e in queue:
            break

        for i in range(len(queue)):
            cur = queue.popleft()

            for neigh, col in graph[cur]:
                if col in colvis:
                    continue
                colvis.add(col)
                for con in conodes[col]:
                    if not visited[con]:
                        visited[con] = 1
                        queue.append(con)
        
        lines += 1

    # Output the minimum number of lines
    print(lines)