N,M = map(int,raw_input().split())
es = [[] for i in range(N)]
for i in range(M):
  a,b = map(int,raw_input().split())
  a,b = a-1,b-1
  es[a].append(b)
  es[b].append(a)

colors = [0 for i in range(N)]

def dfs(v,color):
  colors[v] = color
  for to in es[v]:
    if colors[to] == color:
      return False
    if colors[to] == 0 and not dfs(to, -color):
      return False
  return True

def is_bipartite():
  return dfs(0,1)

if is_bipartite():
  b = (sum(colors) + N) // 2
  w = N-b
  print(b*w - M)
else:
  all = N*(N-1) // 2
  print(all - M)