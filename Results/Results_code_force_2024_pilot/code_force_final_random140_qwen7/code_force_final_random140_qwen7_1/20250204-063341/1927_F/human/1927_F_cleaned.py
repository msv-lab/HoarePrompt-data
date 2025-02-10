class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.size[parent_a] < self.size[parent_b]:
                (parent_a, parent_b) = (parent_b, parent_a)
            self.size[parent_a] += self.size[parent_b]
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
    start = -1
    end = -1
    for (w, u, v) in edges:
        parent_u = dsu.find(u)
        parent_v = dsu.find(v)
        if parent_u == parent_v:
            _min_edge = w
            start = u
            end = v
        else:
            dsu.union(u, v)
    que = deque([start])
    prev = {start: -1}
    while que:
        node = que.popleft()
        if node == end:
            break
        for nei in graph[node]:
            if node == start and nei == end:
                continue
            if nei not in prev:
                prev[nei] = node
                que.append(nei)
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        curr = prev[curr]
    print(_min_edge, len(path))
    print(*path[::-1])

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