q = []
for i in range(int(input())):
    (n, k) = map(int, input().split(' '))
    edges = []
    for _ in range(n - 1):
        (a, b) = map(int, input().split(' '))
        edges.append((a, b))
    if i == 325:
        print(n, k, edges)
    func_1(n, k, edges)
for (n, k, edges) in q:
    func_1(n, k, edges)

def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        g[b].append(a)
    c = 0
    visited = set()


    l = 1
    r = n // k + 1
    while l <= r:
        mid = l + (r - l) // 2
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
    print(r)

def dfs(x, y):
    c = 1
    r = 0
    visited.add(x)
    for node in g[x]:
        if node not in visited:
            (ans, rn) = dfs(node, y)
            r += rn
            if ans >= y:
                r += 1
            else:
                c += ans
    return (c, r)

def check(x):
    visited.clear()
    (ans, r) = dfs(1, x)
    if ans >= x and r >= k:
        return True
    return False

