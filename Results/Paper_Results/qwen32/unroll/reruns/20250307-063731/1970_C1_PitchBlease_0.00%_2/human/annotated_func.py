#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2*10^5, edges is a list of tuples where each tuple (u, v) represents an edge in the tree with 1 <= u, v <= n, and start is an integer representing the starting node where 1 <= start <= n.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `n` is an integer such that 2 <= n <= 2*10^5, `edges` is a list of tuples where each tuple (u, v) represents an edge in the tree with 1 <= u, v <= n, `start` is an integer representing the starting node where 1 <= start <= n, `tree` is a defaultdict of lists that represents an adjacency list of the tree, where each key is a node and its corresponding value is a list of adjacent nodes.`
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 0 or dist2 % 2 == 0) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function `func_1` accepts an integer `n` representing the number of nodes in a tree, a list of tuples `edges` representing the edges of the tree, and an integer `start` representing the starting node. It returns 'Ron' if the shortest distance from the starting node to at least one of the leaves in the tree is even, otherwise it returns 'Hermione'.

#State of the program right berfore the function call: start and target are integers representing nodes in the tree, where 1 <= start <= n and 1 <= target <= n. tree is an adjacency list representing the tree structure with n nodes.
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
#Overall this is what the function does:The function `bfs` calculates the shortest distance between two nodes, `start` and `target`, in a tree represented by an adjacency list `tree`. If a path exists between the nodes, it returns the distance; otherwise, it returns -1.

