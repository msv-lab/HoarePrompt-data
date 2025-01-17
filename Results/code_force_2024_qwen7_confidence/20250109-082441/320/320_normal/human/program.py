import sys
sys.setrecursionlimit(10**6)

def f(b):
    prefix_max = []
    current_max = float('-inf')
    for num in b:
        if num > current_max:
            current_max = num
            prefix_max.append(num)
    return prefix_max

def generate_pre_orders(node, tree, visited, current_order):
    visited[node] = True
    current_order.append(node)
    for child in tree[node]:
        if not visited[child]:
            generate_pre_orders(child, tree, visited, current_order)

def count_distinct_prefix_max(n, edges):
    tree = [[] for _ in range(n + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    pre_orders = []
    for root in range(1, n + 1):
        visited = [False] * (n + 1)
        current_order = []
        generate_pre_orders(root, tree, visited, current_order)
        pre_orders.append(current_order)
    
    distinct_prefix_max = set()
    for order in pre_orders:
        prefix_max = tuple(f(order))
        distinct_prefix_max.add(prefix_max)
    
    return len(distinct_prefix_max) % 998244353

# Input reading
t = int(input())
for _ in range(t):
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    print(count_distinct_prefix_max(n, edges))