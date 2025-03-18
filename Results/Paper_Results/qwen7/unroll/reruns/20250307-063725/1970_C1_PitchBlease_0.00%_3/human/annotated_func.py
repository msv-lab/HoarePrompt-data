#State of the program right berfore the function call: n is an integer representing the number of nodes in the tree, edges is a list of tuples representing the edges of the tree, and start is an integer representing the starting node for the first round. The tree has exactly two leaves, and the length of edges is n-1.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: Output State: `tree` is a defaultdict where each key is a node and its value is a list of its adjacent nodes, with all nodes connected based on the given edges. `n` remains an integer representing the number of nodes in the tree, which does not change during the loop execution. `edges` is a list of tuples representing the edges of the tree, unchanged from the initial state. The `start` integer representing the starting node for the first round remains unchanged.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 0 or dist2 % 2 == 0) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function `func_1` accepts three parameters: an integer `n` representing the number of nodes in the tree, a list of tuples `edges` representing the edges of the tree, and an integer `start` representing the starting node for the first round. It constructs a tree representation using the provided edges. Then, it identifies the two leaves of the tree and calculates the shortest distances from the starting node to each leaf using Breadth-First Search (BFS). Based on whether these distances are even or odd, the function returns either 'Ron' or 'Hermione'.

#State of the program right berfore the function call: start is an integer representing the starting node where the stone is initially placed, and target is an integer representing one of the two leaves of the tree. Both start and target are within the range 1 <= start, target <= n, where n is the number of nodes in the tree. The variable tree is an adjacency list representation of the tree, where tree[i] is a list of integers representing the neighbors of node i.
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
        
    #State: The function returns the shortest distance from the start node to the target node, or None if the target node is not reachable.
    return -1
    #The program returns -1, which indicates that the target node is not reachable from the start node.
#Overall this is what the function does:The function `bfs` accepts two parameters, `start` and `target`, both integers representing nodes in a tree. It uses Breadth-First Search (BFS) to find the shortest path from the `start` node to the `target` node. If the `target` node is reachable, it returns the shortest distance; otherwise, it returns -1 indicating the `target` node is not reachable from the `start` node.

