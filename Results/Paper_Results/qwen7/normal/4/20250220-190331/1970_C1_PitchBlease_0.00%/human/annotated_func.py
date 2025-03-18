#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, edges is a list of tuples representing the edges of the tree, and start is an integer such that 1 ≤ start ≤ n. The tree is represented such that it has exactly two leaves, and the function returns either "Ron" or "Hermione" based on the optimal play of the game.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: Output State: The `tree` is fully constructed as an undirected graph where each node `u` has a list of all nodes `v` it is connected to via an edge in the `edges` list.
    #
    #In this final state, for every edge `(u, v)` in the `edges` list, both `tree[u]` and `tree[v]` will contain each other, meaning `u` will be in `tree[v]` and `v` will be in `tree[u]`. This process continues for all edges in the `edges` list, ensuring that the `tree` represents a complete undirected graph based on the given edges.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 0 or dist2 % 2 == 0) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function accepts an integer `n`, a list of tuples `edges` representing the edges of a tree with exactly two leaves, and an integer `start` as the starting node. It constructs an undirected graph representation of the tree, identifies the two leaves, calculates the shortest path distances from the start node to each leaf using Breadth-First Search (BFS), and determines the winner of the game based on these distances. If either distance is even, the function returns "Ron"; otherwise, it returns "Hermione".

#State of the program right berfore the function call: start is an integer representing the starting node where the stone is initially placed, and target is an integer representing one of the two leaves of the tree. The variable tree is an adjacency list representation of the tree, where tree[i] is a list of integers representing the neighbors of node i.
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
        
    #State: Output State: The `queue` is an empty deque, indicating that all nodes have been processed. The `current` variable holds the last node that was processed, which is likely the target node if the algorithm found it. The `visited` set contains all nodes that are reachable from the `start` node, ensuring no node is visited more than once. The `dist` value represents the shortest distance from the `start` node to the `current` node, which is the final distance to the target node if found, or the distance to the furthest reachable node otherwise.
    #
    #In simpler terms, after all iterations of the loop, the `queue` is empty, meaning no nodes are left to process. The `visited` set includes all reachable nodes, and `current` holds the last node processed, which could be the target node or the furthest node reachable from the start. The `dist` value gives the shortest distance to the `current` node, which is the final distance to the target if found.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `bfs` accepts two parameters: `start` (an integer representing the starting node) and `target` (an integer representing one of the two leaves of the tree). It performs a breadth-first search to find the shortest path from the `start` node to the `target` node. If the `target` node is found, it returns the shortest distance; otherwise, it returns -1.

