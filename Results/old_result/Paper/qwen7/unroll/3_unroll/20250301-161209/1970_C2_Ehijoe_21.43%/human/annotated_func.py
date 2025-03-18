#State of the program right berfore the function call: nodes is a dictionary where each key is a node (integer) and the value is a list of its neighbors (integers), start is an integer representing the starting node, and parent is an optional integer representing the parent node (used recursively to avoid revisiting the parent node).
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns a list containing the integer 0
    #State: nodes is a dictionary where each key is a node (integer) and the value is a list of its neighbors (integers), start is an integer representing the starting node, and parent is an optional integer representing the parent node (used recursively to avoid revisiting the parent node). The length of the neighbors list for the start node is not 1 or the first neighbor of the start node is not equal to the parent node.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: distances is a list containing 1 plus the distances from each node connected to `nodes[start]` and not equal to `parent`, as calculated by `func_1(nodes, node, start)` for each node.
    return distances
    #The program returns a list containing 1 plus the distances from each node connected to `nodes[start]` and not equal to `parent`, as calculated by `func_1(nodes, node, start)` for each node.
#Overall this is what the function does:The function accepts a dictionary `nodes` where each key is a node (integer) and its value is a list of its neighbors (integers), an integer `start` representing the starting node, and an optional integer `parent` representing the parent node (used recursively to avoid revisiting the parent node). It returns a list containing either 0 or 1 plus the distances from each node connected to `nodes[start]` and not equal to `parent`, as calculated by itself for each node. If the starting node has only one neighbor which is the parent, it returns a list containing 0. Otherwise, it calculates the distances from each connected node to the starting node, excluding the parent, and returns these distances in a list.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, edges is a list of tuples representing the edges of the tree, where each tuple (u, v) indicates an edge between nodes u and v, and start is an integer such that 1 ≤ start ≤ n, representing the starting node for the first round of the game.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `edges` is a list containing (u, v) pairs for each edge entered during the loop, `start` is an integer such that 1 ≤ start ≤ n, `empty` is True, `nodes` is a defaultdict where the default factory is list, and each key in `nodes` corresponds to a node and its value is a list of its adjacent nodes based on the edges provided.
    #
    #This output state describes how the `nodes` dictionary will represent the graph after reading `n-1` edges from the input. Each node will have a list of its adjacent nodes.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: Output State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `edges` is a list containing (u, v) pairs for each edge entered during the loop, `start` is an integer such that 1 ≤ start ≤ n, `empty` is True, `nodes` is a defaultdict where the default factory is list, and each key in `nodes` corresponds to a node and its value is a list of its adjacent nodes based on the edges provided, `leaves` is a deque() instance containing all the leaf nodes (nodes with exactly one adjacent node) from the graph.
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `moves` is the result of the function call `func_1(nodes, start)`, `t` is 1, `edges` is a list containing (u, v) pairs for each edge entered during the loop, `start` is an integer equal to the input integer, `empty` is True, `nodes` is a defaultdict where the default factory is list, and each key in `nodes` corresponds to a node and its value is a list of its adjacent nodes based on the edges provided, `leaves` is a deque() instance containing all the leaf nodes (nodes with exactly one adjacent node) from the graph. At least one move in `moves` is an odd number, or all moves in `moves` are even numbers.
#Overall this is what the function does:The function reads the number of nodes \( n \), the number of edges \( t \) (which is fixed at 1), the edges of a tree, and a starting node. It then constructs a graph representation using a dictionary where each node points to its adjacent nodes. Next, it identifies all leaf nodes (nodes with exactly one adjacent node) and stores them in a deque. After that, it calls another function `func_1` to determine a sequence of moves starting from the specified node. Based on whether any move in the sequence is odd, it prints either "Ron" or "Hermione". The function does not return any value.

