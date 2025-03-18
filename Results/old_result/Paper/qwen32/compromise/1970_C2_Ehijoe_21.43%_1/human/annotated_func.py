#State of the program right berfore the function call: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighboring nodes, start is an integer representing the starting node, and parent is an optional integer representing the parent node of the current node.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns [0]
    #State: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighboring nodes, start is an integer representing the starting node, and parent is an optional integer representing the parent node of the current node. The length of the list `nodes[start]` is not equal to 1, or if the length of `nodes[start]` is 1, then `nodes[start][0]` is not equal to `parent`.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: nodes is unchanged, start is unchanged, parent is unchanged, distances is a list of incremented distances from start to all reachable nodes, excluding the parent node.
    return distances
    #The program returns a list of incremented distances from the start node to all reachable nodes, excluding the parent node.
#Overall this is what the function does:The function `func_1` calculates and returns a list of incremented distances from a specified starting node to all reachable nodes in a graph, excluding the parent node. If the starting node has no neighbors or only the parent as a neighbor, it returns `[0]`.

#State of the program right berfore the function call: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighbors of the corresponding node, start is an integer representing the starting node of the game, and moves is a list of integers representing the number of moves required to reach each node from the starting node.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `nodes` is a defaultdict where each key is a node (integer) and each value is a list of integers representing the neighboring nodes; `start` is an integer representing the starting node of the game; `moves` is a list of integers representing the number of moves required to reach each node from the starting node; `n` is the first integer from the input; `t` is the second integer from the input; `edges` is an empty list; `empty` is True.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: `nodes` is a defaultdict where each key is a node (integer) and each value is a list of integers representing the neighboring nodes; `start` is an integer representing the starting node of the game; `moves` is a list of integers representing the number of moves required to reach each node from the starting node; `n` is the first integer from the input; `t` is the second integer from the input; `edges` is an empty list; `empty` is True; `leaves` is a deque containing all the leaf nodes (nodes with only one neighbor) from the `nodes` dictionary.
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `nodes` is a defaultdict where each key is a node (integer) and each value is a list of integers representing the neighboring nodes; `start` is the integer value provided by the input; `moves` is a list of integers representing the number of moves required to reach each node from the starting node, as calculated by `func_1(nodes, start)`, and at least one value in `moves` is odd if the if condition is true, otherwise all values in `moves` are even; `n` is the first integer from the input; `t` is the second integer from the input; `edges` is an empty list; `empty` is True; `leaves` is a deque containing all the leaf nodes (nodes with only one neighbor) from the `nodes` dictionary.
#Overall this is what the function does:The function `func_2` reads input to construct a graph represented by nodes and their connections, determines the number of moves required to reach each node from a specified starting node, and prints 'Ron' if any node is an odd number of moves away from the start, otherwise it prints 'Hermione'.

