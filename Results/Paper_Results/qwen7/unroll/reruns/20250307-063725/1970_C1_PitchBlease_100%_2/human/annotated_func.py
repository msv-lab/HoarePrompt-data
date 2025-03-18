#State of the program right berfore the function call: n is an integer representing the number of nodes in the tree, edges is a list of tuples representing the edges of the tree, and start is an integer representing the starting node where the stone is initially placed. It is guaranteed that the tree has exactly two leaves.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: Output State: `tree` is a defaultdict where each key is a node and its value is a list of its adjacent nodes, with all edges from `edges` added bidirectionally. The state of `n` and `start` remains unchanged.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 1 or dist2 % 2 == 1) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns the string 'Hermione'
#Overall this is what the function does:The function `func_1` constructs an adjacency list representation of a tree using the given number of nodes `n`, edges, and a starting node `start`. It then identifies the two leaves of the tree, calculates the shortest distances from the starting node to these leaves, and determines whether either of these distances is odd. If any distance is odd, the function returns 'Ron'; otherwise, it returns 'Hermione'.

#State of the program right berfore the function call: start is an integer representing the starting node where the stone is initially placed, target is an integer representing one of the leaves of the tree, and tree is a dictionary representing the adjacency list of the tree where keys are node indices and values are lists of neighboring nodes.
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
        
    #State: Output State: The output state will be a tuple consisting of the node index `target` and its shortest distance from the starting node `start`.
    #
    #Natural Language Description: After the loop executes all its iterations, the `current` node will be equal to the `target` node, and the `dist` variable will hold the shortest distance from the `start` node to the `target` node. This is because the loop continues to process nodes level by level (BFS), updating the distance until it finds the `target` node, at which point it returns the distance.
    return -1
    #(-1, -1)
#Overall this is what the function does:The function `bfs` accepts two parameters: `start` (an integer representing the starting node) and `target` (an integer representing one of the leaves of the tree). It also accepts a dictionary named `tree` which represents the adjacency list of the tree. The function performs a breadth-first search to find the shortest path from the `start` node to the `target` node. If the `target` node is found, it returns a tuple containing the `target` node and its shortest distance from the `start` node. If the `target` node is not found, it returns `(-1, -1)`.

