#State of the program right berfore the function call: nodes is a dictionary representing the tree structure where keys are node indices and values are lists of neighboring nodes; start is an integer representing the index of the starting node for the current round; parent is an integer representing the index of the parent node of the current node (default is None).
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return False
        #The program returns False
    #State: nodes is a dictionary representing the tree structure where keys are node indices and values are lists of neighboring nodes; start is an integer representing the index of the starting node for the current round; parent is an integer representing the index of the parent node of the current node (default is None). The length of nodes[start] is not 1 or nodes[start][0] is not equal to parent
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.append(not func_1(nodes, node, start))
        
    #State: Output State: `distances` is a list containing `not func_1(nodes, node, start)` for each node in `nodes[start]` that is not equal to `parent`, `nodes` is a dictionary representing the tree structure, `start` is an integer representing the index of the starting node, `parent` is an integer representing the index of the parent node (default is `None`), and `node` iterates through each neighbor of `start` in `nodes[start]` that is not equal to `parent`.
    #
    #In simpler terms, after the loop has executed all its iterations, `distances` will contain the result of `not func_1(nodes, node, start)` for every direct child node of the starting node (`start`), excluding the parent node. The `nodes` dictionary and the `start` and `parent` variables retain their original structure and values from the initial state, and `node` represents each child node of `start` that was processed by the loop.
    return any(distances)
    #The program returns a boolean value indicating whether any of the distances calculated as `not func_1(nodes, node, start)` for the direct child nodes of the starting node (`start`), excluding the parent node, is True.
#Overall this is what the function does:The function accepts a dictionary `nodes` representing a tree structure, an integer `start` representing the starting node index, and an integer `parent` representing the parent node index (default is None). It checks if any direct child nodes of the starting node have a distance that is not True when passed through the function. If no such child nodes exist, it returns False; otherwise, it returns True.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, edges is a list of tuples representing the edges of the tree, where each tuple (u, v) indicates an edge between nodes u and v, and start is an integer such that 1 ≤ start ≤ n, representing the initial node where the stone is placed.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: The loop will execute `n-1` times, where `n` is the number of nodes in the graph. After all iterations, `i` will be `n-2`, `n` remains an integer such that \(2 \leq n \leq 2 \times 10^5\), `t` is 1, `edges` is a list containing all pairs of integers \((u, v)\) that were input during the loop, `start` is an integer such that \(1 \leq start \leq n\), `empty` is `True`, and `nodes` is a `defaultdict` where for each node `u`, `nodes[u]` contains a list of all nodes `v` that are connected to `u` via an edge, and vice versa.
    #
    #In simpler terms, after the loop completes, the variable `i` will be `n-2`, meaning the loop has processed all but one of the possible edges in the graph (since the graph is undirected, we only need `n-1` edges to connect all `n` nodes). The `nodes` dictionary will represent the adjacency list of the graph, with each node pointing to all its adjacent nodes, and vice versa.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: After all iterations of the loop, the `leaves` deque will contain all the leaf nodes (nodes with exactly one connection) in the graph.
    start = int(input())
    moves = func_1(nodes, start)
    if moves :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `start` is an input integer, `moves` is the result of `func_1(nodes, start)`. If `moves` is truthy, the function continues based on the logic within the if block. Otherwise, `moves` is set to False.
#Overall this is what the function does:The function accepts the number of nodes \(n\) in a tree, the number of moves \(t\) (which is always 1), a list of edges representing the tree structure, and the starting node. It then identifies all leaf nodes in the tree and checks if the starting node can reach any other node in one move using the `func_1` function. If a move is possible, it prints 'Ron'; otherwise, it prints 'Hermione'.

