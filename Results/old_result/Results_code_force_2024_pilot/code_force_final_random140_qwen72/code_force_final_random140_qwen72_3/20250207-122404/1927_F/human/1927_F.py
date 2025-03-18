from collections import defaultdict, deque
import sys
import threading
 
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
                parent_a, parent_b = parent_b, parent_a
 
            self.size[parent_a] += self.size[parent_b]
            self.parent[parent_b] = parent_a
 
        return
    
def int_input():
    return int(sys.stdin.readline().strip())
 
def string():
    return sys.stdin.readline().strip()
 
def map_int():
    return map(int, sys.stdin.readline().strip().split())
 
def list_int_input():
    return list(map(int, sys.stdin.readline().strip().split()))
 
def list_string_input():
    return list(sys.stdin.readline().strip().split())
 
def solve():
    n,m = map_int()
    graph = defaultdict(list)
    edges = []
 
    for i in range(m):
        u,v,w = map_int()
        graph[u].append(v)
        graph[v].append(u)
 
        edges.append((w,u,v))
 
 
    edges.sort(reverse=True)
 
    
    dsu = DSU(n+1)
    _min_edge = float('inf')
    start = -1
    end = -1
 
    for w,u,v in edges:
        parent_u = dsu.find(u)
        parent_v = dsu.find(v)
        if parent_u == parent_v:
            _min_edge = w
            start = u
            end = v
        else:
            dsu.union(u,v)
 
    # path = []
    # visited = set()
 
    # def dfs(node):
    #     visited.add(node)
    #     for nei in graph[node]:
    #         if nei in visited or (node == start and nei == end):
    #             continue
    #         if nei == end or dfs(nei):
    #             path.append(node)
    #             return True
    #     return False
    
    # dfs(start)
    # path.append(end)
    # print(_min_edge,len(path))
    # print(*path)
 
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
 
    print(_min_edge,len(path))
    print(*path[::-1])
 
def main():
    test_cases = int_input()
    for _ in range(test_cases):
        solve()
 
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
 
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()