class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.min_edge = [float('inf')] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b, w):
        parent_a = self.find(a)
        parent_b = self.find(b)
        self.min_edge[parent_a] = min(self.min_edge[parent_a], w)
        self.min_edge[parent_b] = min(self.min_edge[parent_b], w)
        if parent_a != parent_b:
            if self.size[parent_a] < self.size[parent_b]:
                (parent_a, parent_b) = (parent_b, parent_a)
            self.size[parent_a] += self.size[parent_b]
            self.min_edge[parent_a] = min(self.min_edge[parent_a], self.min_edge[parent_b])
            self.parent[parent_b] = parent_a
        return

def func_1():
    return int(sys.stdin.readline().strip())

def func_2():
    return sys.stdin.readline().strip()

def func_3():
    return map(int, sys.stdin.readline().strip().split())

def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))

def func_5():
    return list(sys.stdin.readline().strip().split())

def func_6():
    (n, m) = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        (u, v, w) = func_3()
        graph[u].append(v)
        graph[v].append(u)
        edges.append((w, u, v))
    edges.sort(reverse=True)
    dsu = DSU(n + 1)
    _min_edge = float('inf')
    node_u = -1
    node_v = -1
    for (w, u, v) in edges:
        parent_u = dsu.find(u)
        parent_v = dsu.find(v)
        if parent_u == parent_v:
            dsu.union(u, v, w)
            if dsu.min_edge[parent_u] < _min_edge:
                _min_edge = dsu.min_edge[parent_u]
                node_u = u
                node_v = v
        else:
            dsu.union(u, v, w)
    colors = [0] * (n + 1)

    def dfs(curr, parent, path):
        if colors[curr] == 1:
            return path
        colors[curr] = 1
        path.append(curr)
        for nei in graph[curr]:
            if colors[nei] != 2 and nei != parent:
                res = dfs(nei, curr, path)
                set_res = set(res)
                if res and node_v in set_res:
                    return res
        colors[curr] = 2
        return []
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    print(*res)

def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()