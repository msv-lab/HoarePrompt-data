from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

dp = [0] * (N + 1)
dp[N] = 1

q = deque([N])
while q:
    v = q.popleft()
    for u in graph:
        if v in graph[u]:
            dp[u] += dp[v] / len(graph[u])
            q.append(u)

print(dp[1])
