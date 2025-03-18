#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2*10^5, edges is a list of tuples where each tuple contains two integers u and v such that 1 <= u, v <= n, and start is an integer such that 1 <= start <= n.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `tree` is a defaultdict with list as the default factory, where each key is a node (integer from 1 to n) and each value is a list of adjacent nodes, representing the connections between nodes as specified by the `edges` list. The values of `n`, `edges`, and `start` remain unchanged.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 1 or dist2 % 2 == 1) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function `func_1` takes an integer `n` representing the number of nodes, a list of tuples `edges` representing the connections between the nodes, and an integer `start` representing the starting node. It determines the shortest paths from the starting node to two leaf nodes and returns 'Ron' if at least one of these paths has an odd length, otherwise it returns 'Hermione'.

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
        
    #State: The function returns the shortest distance from `start` to `target`.
    return -1
    #The program returns -1.
#Overall this is what the function does:The function `bfs` calculates the shortest distance from a starting node to a target node in a tree represented by an adjacency list. If the target node is reachable from the starting node, it returns the shortest distance; otherwise, it returns -1.

