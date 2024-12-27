n, m = raw_input().split()
n, m = int(n), int(m)
graph = {}
for i in range(n):
    graph[i] = []
visited = set()
path = []

for i in range(m):
    u, v = raw_input().split()
    u, v = int(u)-1, int(v)-1
    graph[u].append(v)
    graph[v].append(u)

parities = raw_input().split()
for i in range(n):
    parities[i] = int(parities[i])

def add_to_path(u):
    path.append(u)
    parities[u] ^= 1 # XOR. flip parity

def dfs(u, previous):
    visited.add(u)
    add_to_path(u)
    
    for v in graph[u]:
        if (v in visited) == False:
            dfs(v, u)
            add_to_path(u) # go back to u

    if parities[u] == 1:
        if previous == -1:
            path.pop()
            parities[u] ^= 1
        else:
            add_to_path(previous)
            add_to_path(u)
        
    return visited

for i in range(n):
    if parities[i] == 1:
        dfs(i, -1)
        break
for i in range(n):
    if parities[i] == 1:
       print(-1)
print(len(path))
string = ''
for u in path:
    string += str(u+1) + ' '
print(string)
