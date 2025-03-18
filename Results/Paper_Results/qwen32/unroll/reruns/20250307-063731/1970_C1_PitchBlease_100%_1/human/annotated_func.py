#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, edges is a list of tuples of integers where each tuple (u, v) represents an edge in the tree with 1 <= u, v <= n, and start is an integer representing the starting node where the stone is initially put such that 1 <= start <= n.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `tree` is a defaultdict of lists where each key `u` (from 1 to n) maps to a list of integers representing all nodes directly connected to `u` by an edge in the tree. The values of `n`, `edges`, and `start` remain unchanged.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 1 or dist2 % 2 == 1) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function `func_1` determines the winner of a game based on the distances from a starting node to two leaf nodes in a tree. It accepts three parameters: `n`, the number of nodes in the tree; `edges`, a list of tuples representing the edges of the tree; and `start`, the starting node. The function returns 'Ron' if at least one of the distances from the starting node to the two leaf nodes is odd, and 'Hermione' if both distances are even.

#State of the program right berfore the function call: start is an integer representing the starting node in the tree, and target is an integer representing the target node in the tree. The tree is an adjacency list where each node points to its neighbors, and both start and target are valid nodes within this tree.
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
        
    #State: the shortest distance from `start` to `target` if reachable, otherwise `None`. The `queue` will be empty, and the `visited` set will contain all nodes reachable from `start`.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `bfs` performs a breadth-first search on a tree represented as an adjacency list to find the shortest distance from a starting node to a target node. It returns the shortest distance if the target is reachable from the start node, otherwise, it returns -1.

