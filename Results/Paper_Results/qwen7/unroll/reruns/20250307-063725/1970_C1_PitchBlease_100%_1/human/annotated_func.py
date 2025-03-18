#State of the program right berfore the function call: n is an integer representing the number of nodes in the tree, edges is a list of tuples representing the edges of the tree, and start is an integer representing the starting node where the stone is initially placed. The tree has exactly two leaves, and the function assumes that the input satisfies this condition.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: Output State: `tree` is a defaultdict where each key is a node and its value is a list of nodes it is connected to, forming an undirected graph based on the given edges. `n` is an integer representing the number of nodes in the tree, which remains unchanged. `edges` is a list of tuples representing the edges of the tree, and `start` is an integer representing the starting node where the stone is initially placed, which also remains unchanged. After the loop executes all the iterations, each node will have a list of its connected nodes bidirectionally.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 1 or dist2 % 2 == 1) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns the string 'Hermione'
#Overall this is what the function does:The function `func_1` accepts three parameters: an integer `n` representing the number of nodes in the tree, a list of tuples `edges` representing the edges of the tree, and an integer `start` representing the starting node where the stone is initially placed. It constructs an undirected graph from the given edges and identifies the two leaves of the tree. Then, it calculates the shortest distances from the starting node to each leaf using breadth-first search (BFS). Based on whether these distances are odd or even, the function returns either 'Ron' or 'Hermione'.

#State of the program right berfore the function call: start is an integer representing the starting node where the stone is initially placed, target is an integer representing one of the two leaves of the tree, and tree is a dictionary where keys are node indices and values are lists of neighboring node indices.
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
        
    #State: The function returns the shortest distance from the start node to the target node, or None if the target node is not reachable. The queue is empty, and the visited set contains all nodes that are reachable from the start node and have been checked.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `bfs` accepts two parameters, `start` and `target`, both integers. It performs a breadth-first search on a tree structure represented by the `tree` dictionary to find the shortest path distance from the `start` node to the `target` node. If the `target` node is reachable, it returns the distance; otherwise, it returns -1.

