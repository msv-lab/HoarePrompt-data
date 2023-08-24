MOD = 10**9 + 7

def dfs(v, p, G):
  result = 1
  for u in G[v]:
    if u == p:
      continue
    result *= dfs(u, v, G)
    result %= MOD
  return (result + 1) % MOD

N = int(input())

G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  x, y = map(int, input().split())
  G[x].append(y)
  G[y].append(x)

answer = dfs(1, -1, G)
answer -= 1
answer = (answer + MOD) % MOD

print(answer)
