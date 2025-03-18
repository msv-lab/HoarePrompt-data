#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, edges is a list of tuples (u, v) where 1 <= u, v <= n and each tuple represents an edge in the tree, start is an integer such that 1 <= start <= n and represents the starting node for the game.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `tree` is a defaultdict of lists where each key is a node (from 1 to n) and the value is a list of nodes that are directly connected to the key node by an edge. The lists contain the neighbors of each node as defined by the edges. The variables `n`, `edges`, and `start` remain unchanged.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 0 or dist2 % 2 == 0) :
        return 'Ron'
        #The program returns the string 'Ron'.
    else :
        return 'Hermione'
        #The program returns the string 'Hermione'.
#Overall this is what the function does:The function `func_1` accepts three parameters: `n` (an integer such that 2 <= n <= 2 * 10^5), `edges` (a list of tuples representing edges in a tree), and `start` (an integer representing the starting node for the game). It constructs a tree from the edges, identifies the leaves of the tree, and performs breadth-first searches (BFS) from the starting node to the first two leaves. The function returns 'Ron' if the distance from the starting node to either of the first two leaves is even, and 'Hermione' otherwise. The input parameters `n`, `edges`, and `start` remain unchanged after the function execution.

#State of the program right berfore the function call: start and target are integers representing node indices in the tree, where 1 <= start, target <= n, and tree is a dictionary or list of lists representing the adjacency list of the tree, with each node having at least one neighbor and the tree having exactly two leaves.
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
        
    #State: The `queue` is empty, `visited` contains all the nodes that were visited during the search, and the loop returns the shortest distance `dist` from the `start` node to the `target` node.
    return -1
    #The program returns -1.
#Overall this is what the function does:The function `bfs` accepts two integers `start` and `target`, representing node indices in a tree. It performs a breadth-first search to find the shortest path from the `start` node to the `target` node. If the `target` node is found, the function returns the distance (number of edges) between the `start` and `target` nodes. If the `target` node is not found, the function returns -1. The function does not modify the input tree.

