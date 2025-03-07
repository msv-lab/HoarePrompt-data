def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        g[b].append(a)
    c = 0

    def check(A):
        stack = [(1, 1)]
        visited = set()
        d = {1: 1}
        r = 0
        while True:
            (x, p) = stack[-1]
            if x not in visited:
                visited.add(x)
                d[x] = 1
                for node in g[x]:
                    if node != p:
                        stack.append((node, x))
            else:
                if x == 1:
                    break
                if d[x] >= A:
                    r += 1
                else:
                    d[p] += d[x]
                stack.pop()
                visited.remove(x)
                del d[x]
        if r > k or (d[1] >= A and r == k):
            return True
        return False
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
    print(r)
q = []
for i in range(int(input())):
    (n, k) = map(int, input().split(' '))
    edges = []
    for _ in range(n - 1):
        (a, b) = map(int, input().split(' '))
        edges.append((a, b))
    func_1(n, k, edges)
for (n, k, edges) in q:
    func_1(n, k, edges)