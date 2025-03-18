#State of the program right berfore the function call: nodes is a dictionary where each key is a node (an integer between 1 and n) and its value is a list of its neighbors (excluding the parent node if provided); start is an integer representing the starting node (between 1 and n); parent is an integer representing the parent node (optional, default is None).
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns a list containing the single element 0.
    #State: nodes is a dictionary where each key is a node (an integer between 1 and n) and its value is a list of its neighbors (excluding the parent node if provided); start is an integer representing the starting node (between 1 and n); parent is an integer representing the parent node (optional, default is None). The length of nodes[start] is not 1 or nodes[start][0] is not equal to parent
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: The `distances` list will contain tuples where each tuple consists of the distance from the start node (this distance is calculated as 1 plus the distance obtained from `func_1(nodes, node, start)` for every node in the `nodes[start]` list, excluding the `parent` node if provided). The `nodes`, `start`, and `parent` variables remain unchanged.
    return distances
    #The program returns a list named 'distances' which contains tuples. Each tuple consists of the distance from the start node, calculated as 1 plus the distance obtained from `func_1(nodes, node, start)` for every node in the `nodes[start]` list, excluding the `parent` node if provided.
#Overall this is what the function does:The function `func_1` accepts a dictionary `nodes`, an integer `start`, and an optional integer `parent`. It processes the `nodes` dictionary to calculate distances from the `start` node to other nodes in the graph. If the `start` node has only one neighbor which is the `parent`, it returns a list containing the single element 0. Otherwise, it recursively calculates the distances to all other neighbors of the `start` node, excluding the `parent` node, and returns a list of tuples. Each tuple contains the distance from the `start` node to a neighboring node, calculated as 1 plus the distance obtained from recursive calls to `func_1`.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, edges is a list of tuples representing the edges of the tree, where each tuple (u, v) indicates an undirected edge between nodes u and v, and start is an integer such that 1 ≤ start ≤ n, representing the initial node where the stone is placed.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: The loop will have executed `n-1` times since `n` is the number of nodes and a tree with `n` nodes has exactly `n-1` edges. Therefore, `i` will be `n-2`. For each edge `(u, v)` read from input, both `u` and `v` are added to each other's adjacency lists in `nodes`. After all iterations, `nodes` will be a dictionary where each key is a node and its value is a list of all nodes it is connected to, forming the complete adjacency list representation of the tree.
    #
    #In natural language: After the loop completes all its iterations, `i` will be `n-2`, indicating that all `n-1` edges have been processed. The variable `nodes` will contain the full adjacency list representation of a tree with `n` nodes, where each node's list of neighbors includes all other nodes it is directly connected to through the edges specified in the input.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: All nodes that have only one neighbor in the tree are added to the `leaves` deque.
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `leaves` is a deque containing all nodes that have only one neighbor in the tree, `moves` is the result of calling `func_1(nodes, start)`, `start` is an input integer, and if there exists at least one move in `moves` which is an odd number, the postcondition remains the same as the precondition. Otherwise, all elements in `moves` are even numbers.
#Overall this is what the function does:The function processes a tree represented by its edges and determines whether a series of moves starting from a given node will result in an odd or even number of steps. If there is at least one odd-numbered move, it prints 'Ron'; otherwise, it prints 'Hermione'. The function accepts four parameters: the number of nodes `n`, the number of edges `t` (which is always 1), a list of edges `edges`, and a starting node `start`. It returns nothing but prints either 'Ron' or 'Hermione' based on the parity of the moves.

