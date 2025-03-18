#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, edges is a list of tuples where each tuple (u, v) represents an edge in the tree with 1 <= u, v <= n, and start is an integer representing the starting node of the stone such that 1 <= start <= n.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `tree` is a `defaultdict` where each key is a node (from 1 to n) and each value is a list of nodes that are directly connected to the key node, representing the adjacency list of the tree. The values of `n`, `edges`, and `start` remain unchanged.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 0 or dist2 % 2 == 0) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function `func_1` determines the winner of a game based on the structure of a tree and the starting node of a stone. It accepts three parameters: an integer `n` representing the number of nodes in the tree, a list of tuples `edges` representing the edges in the tree, and an integer `start` representing the starting node of the stone. The function returns 'Ron' if the distance from the starting node to any two leaf nodes is such that at least one of these distances is even, otherwise it returns 'Hermione'.

#State of the program right berfore the function call: start and target are integers representing nodes in the tree, where 1 <= start <= n and 1 <= target <= n. tree is an adjacency list representing the tree structure with n nodes and n-1 edges, and it is guaranteed that the tree has exactly two leaves.
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
        
    #State: the shortest distance from `start` to `target` in the tree.
    return -1
    #The program returns -1
#Overall this is what the function does:The function calculates the shortest distance between two nodes, `start` and `target`, in a tree represented by an adjacency list. If a path exists between the nodes, it returns the distance; otherwise, it returns -1.

