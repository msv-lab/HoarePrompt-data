#State of the program right berfore the function call: n is an integer representing the number of nodes in the tree such that 2 <= n <= 2*10^5, edges is a list of tuples where each tuple (u, v) represents an edge between nodes u and v with 1 <= u, v <= n, and start is an integer representing the starting node where the stone is initially put such that 1 <= start <= n.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `n` is an integer representing the number of nodes in the tree such that 2 <= n <= 2*10^5; `edges` is a list of tuples where each tuple (u, v) represents an edge between nodes u and v with 1 <= u, v <= n, and all elements in `edges` have been processed; `start` is an integer representing the starting node where the stone is initially put such that 1 <= start <= n; `tree` is a defaultdict of lists where for each edge (u, v), `v` has been appended to the list associated with key `u` and `u` has been appended to the list associated with key `v`, thus representing an adjacency list of the tree.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 0 or dist2 % 2 == 0) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function accepts an integer `n` representing the number of nodes in a tree, a list of tuples `edges` representing the edges between nodes, and an integer `start` representing the starting node. It returns 'Ron' if at least one of the distances from the starting node to any two leaf nodes is even, otherwise it returns 'Hermione'.

#State of the program right berfore the function call: start is an integer representing the starting node of the BFS, target is an integer representing the target node in the tree, tree is an adjacency list representation of the tree where each key is a node and its value is a list of its neighbors.
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
        
    #State: The function either returns the distance from `start` to `target` if `target` is found, or it returns nothing (implicitly `None`) if `target` is not reachable from `start`. The `queue` is empty, and `visited` contains all nodes reachable from `start`.
    return -1
    #The program returns -1
#Overall this is what the function does:The function performs a Breadth-First Search (BFS) to find the shortest path distance from a starting node to a target node in a tree represented as an adjacency list. If the target node is reachable from the start node, it returns the shortest path distance. If the target node is not reachable, it returns -1.

