#State of the program right berfore the function call: nodes is a list of lists representing a tree where each inner list contains the neighbors of the corresponding node, start is an integer representing the starting node (1 ≤ start ≤ n), and parent is an integer or None representing the parent node of the current node in the tree (if applicable).
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns a list containing the single element 0.
    #State: nodes is a list of lists representing a tree where each inner list contains the neighbors of the corresponding node, start is an integer representing the starting node (1 ≤ start ≤ n), and parent is an integer or None representing the parent node of the current node in the tree (if applicable). Additionally, either the length of nodes[start] is not 1, or nodes[start][0] is not equal to parent.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: `distances` is a list containing the distances from the starting node to all its children and their respective descendants, incremented by 1. The `nodes`, `start`, and `parent` variables remain unchanged.
    return distances
    #The program returns the list `distances` which contains the distances from the starting node to all its children and their respective descendants, incremented by 1. The `nodes`, `start`, and `parent` variables remain unchanged.
#Overall this is what the function does:The function `func_1` accepts a tree represented as a list of lists `nodes`, an integer `start` (1 ≤ start ≤ n) representing the starting node, and an integer or None `parent` representing the parent node. It returns a list of distances from the starting node to all its descendants in the tree, where each distance is incremented by 1. If the starting node is a leaf node (i.e., it has only one neighbor, which is its parent), the function returns a list containing the single element 0. The `nodes`, `start`, and `parent` variables remain unchanged.

#State of the program right berfore the function call: n and t are integers where 2 <= n <= 2 * 10^5 and t = 1. The edges list is initially empty and will be populated with pairs of integers (u, v) where 1 <= u, v <= n, representing the edges of the tree. start is an integer where 1 <= start <= n, representing the starting node for the game.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: The `nodes` defaultdict is populated with the adjacency lists for each node in the graph, where each node `u` has a list of nodes `v` that are directly connected to it. The `edges` list remains empty. The `empty` variable remains True. The `start` variable remains unchanged. The loop has iterated `n-1` times, and `t` remains 1.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: Output State: The `leaves` deque is now populated with all the nodes that have exactly one connection (i.e., nodes with a degree of 1) in the graph. The `nodes` defaultdict remains unchanged. The `edges` list remains empty. The `empty` variable remains True. The `start` variable remains unchanged. The loop has iterated `n-1` times, and `t` remains 1.
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *The `leaves` deque is populated with all the nodes that have exactly one connection in the graph. The `nodes` defaultdict remains unchanged. The `edges` list remains empty. The `empty` variable remains True. The `start` variable is an input integer. The loop has iterated `n-1` times, and `t` remains 1. `moves` is the result of `func_1(nodes, start)`. If at least one element in `moves` is an odd number, then that condition is retained. Otherwise, all elements in `moves` are even.
#Overall this is what the function does:The function reads the number of nodes `n` and a fixed integer `t` (set to 1) from input. It then reads `n-1` pairs of integers representing the edges of a tree and constructs an adjacency list `nodes` for the tree. The function identifies all leaf nodes (nodes with exactly one connection) and stores them in a deque `leaves`. It reads a starting node `start` from input and calls another function `func_1` with the adjacency list `nodes` and the starting node `start`. The function prints 'Ron' if at least one move in the result of `func_1` is an odd number, otherwise, it prints 'Hermione'. The function does not return any value.

