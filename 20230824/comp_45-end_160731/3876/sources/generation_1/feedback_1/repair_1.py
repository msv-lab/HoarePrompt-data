MOD = 10**9 + 7

def dfs(v, parent, G, dp):
    result = 1
    for u in G[v]:
        if u == parent:
            continue
        result *= dfs(u, v, G, dp)
        result %= MOD
    dp[v] = result
    return (result + 1) % MOD

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    G[x-1].append(y-1)
    G[y-1].append(x-1)

dp = [0] * N
answer = dfs(0, -1, G, dp)
answer -= 1
answer = (answer + MOD) % MOD

print(answer)