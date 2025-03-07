#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2*10^5, edges is a list of tuples where each tuple (u, v) represents an edge in the tree with 1 <= u, v <= n, and start is an integer such that 1 <= start <= n.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `tree` is a defaultdict where each key `u` is associated with a list of vertices `v` that are directly connected to `u` by an edge in the tree, representing the adjacency list of the tree.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 0 or dist2 % 2 == 0) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function `func_1` accepts an integer `n` representing the number of nodes in a tree, a list of tuples `edges` representing the edges in the tree, and an integer `start` representing the starting node. It returns 'Ron' if the shortest distance from the starting node to at least one of the leaves in the tree is even, and 'Hermione' if the shortest distance to both leaves is odd.

#State of the program right berfore the function call: start and target are integers representing nodes in the tree such that 1 <= start <= n and 1 <= target <= n, where n is the number of nodes in the tree. tree is a dictionary (or list of lists) where tree[i] contains the neighbors of node i.
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
        
    #State: `start` and `target` remain unchanged, `tree` remains unchanged, `queue` is empty, `visited` contains all nodes that are reachable from `start`, `current` is the last node processed, and `dist` is the shortest distance from `start` to `target` if `target` is reachable; otherwise, `dist` reflects the distance to the last node processed.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `bfs` determines the shortest distance from a starting node to a target node in a tree. It accepts two integer parameters, `start` and `target`, representing the nodes, and a `tree` which is a dictionary or list of lists representing the tree structure. If the `start` node is the same as the `target` node, it returns `0`. If the `target` is reachable from the `start`, it returns the shortest distance. If the `target` is not reachable, it returns `-1`.

