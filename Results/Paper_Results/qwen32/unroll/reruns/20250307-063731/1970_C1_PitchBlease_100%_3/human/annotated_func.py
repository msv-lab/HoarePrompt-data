#State of the program right berfore the function call: n is an integer representing the number of nodes in the tree (2 ≤ n ≤ 2×10^5), edges is a list of tuples representing the edges of the tree, and start is an integer representing the node where the stone is initially placed (1 ≤ start ≤ n).
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `tree` is a defaultdict with lists as the default factory, where each key is a node from 1 to n, and the corresponding value is a list of all nodes that are directly connected to the key node via an edge in the `edges` list. The values of `n`, `edges`, and `start` remain unchanged.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 1 or dist2 % 2 == 1) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function `func_1` determines the winner of a game played on a tree structure. It takes three parameters: the number of nodes `n`, a list of edges `edges`, and the starting node `start`. The function returns 'Ron' if Ron wins and 'Hermione' if Hermione wins, based on the distances from the starting node to two leaf nodes.

#State of the program right berfore the function call: start and target are integers representing node indices in the tree, where 1 <= start <= n and 1 <= target <= n. tree is an adjacency list representing the tree structure with n nodes.
def bfs(start, target):
    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        current, dist = queue.popleft()
        
        if current == target:
            return dist
        
        for neighbor in tree[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
        
    #State: the shortest distance from `start` to `target`.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `bfs` calculates the shortest distance from a starting node to a target node in a tree represented by an adjacency list. If there is no path from the start node to the target node, it returns -1.

