from collections import defaultdict

def dfs(v, k):
    visited[v] = True
    order.append(v)

    if v in tree:
        children = tree[v]
        for child in children:
            if not visited[child]:
                dfs(child, k)
                order.append(v)

    if len(order) >= k:
        return order[k-1]
    else:
        return -1

n, q = map(int, input().split())
superiors = list(map(int, input().split()))

tree = defaultdict(list)
for i in range(1, n):
    tree[superiors[i-1]].append(i+1)

for _ in range(q):
    u, k = map(int, input().split())
    visited = [False] * (n+1)
    order = []

    result = dfs(u, k)
    print(result)
