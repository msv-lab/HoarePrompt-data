def solve_test_case(n, edges):
    # Create an adjacency list to represent the tree
    tree = [[] for _ in range(n + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    results = []
    
    for v in range(1, n + 1):
        # Simulate the removal of vertex v
        # Find the minimum cost to restore the tree
        min_cost = float('inf')
        added_edges = []
        
        # Check each pair of vertices to see if adding an edge is necessary
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if i != v and j != v:
                    # Check if adding an edge between i and j is necessary
                    if not is_connected(tree, i, j, v):
                        cost = abs(i - j)
                        if cost < min_cost:
                            min_cost = cost
                            added_edges = [(i, j)]
                        elif cost == min_cost:
                            added_edges.append((i, j))
        
        results.append((min_cost, len(added_edges), added_edges))
    
    return results

def is_connected(tree, i, j, v):
    # Check if vertices i and j are connected in the tree without using vertex v
    visited = [False] * (len(tree) + 1)
    visited[v] = True
    
    def dfs(node):
        if node == j:
            return True
        visited[node] = True
        for neighbor in tree[node]:
            if not visited[neighbor] and dfs(neighbor):
                return True
        return False
    
    return dfs(i)

def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    t = int(data[0])
    test_cases = []
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        edges = [tuple(map(int, data[idx + i + 1].split())) for i in range(n - 1)]
        test_cases.append((n, edges))
        idx += n
    
    for case_num, (n, edges) in enumerate(test_cases):
        results = solve_test_case(n, edges)
        for v, (min_cost, num_edges, added_edges) in enumerate(results, start=1):
            print(min_cost, num_edges)
            for a, b in added_edges:
                print(a, b)

if __name__ == "__main__":
    main()