#State of the program right berfore the function call: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighboring nodes. start is an integer representing the starting node, and parent is an optional integer representing the parent node of the current node.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns the list [0]
    #State: `nodes` is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighboring nodes. `start` is an integer representing the starting node, and `parent` is an optional integer representing the parent node of the current node. The length of `nodes[start]` is not 1, or if it is 1, the single element in `nodes[start]` is not equal to `parent`.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: `nodes` is unchanged, `start` is unchanged, `parent` is unchanged, and `distances` is a list containing the incremented distances from the recursive calls to `func_1` for each valid node in `nodes[start]`.
    return distances
    #The program returns the list `distances` which contains the incremented distances from the recursive calls to `func_1` for each valid node in `nodes[start]`.
#Overall this is what the function does:The function `func_1` calculates and returns a list of distances from a starting node to all other nodes in a graph, represented as a dictionary where keys are nodes and values are lists of neighboring nodes. If a node has only one neighbor which is its parent, it returns `[0]`. Otherwise, it recursively calculates the distances for all valid neighboring nodes and returns a list of these incremented distances.

#State of the program right berfore the function call: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing neighboring nodes; start is an integer representing the starting node of the game, which is a key in the nodes dictionary.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `nodes` is a defaultdict where each key `u` has a list of connected nodes `v`; `start` is an integer representing the starting node of the game, which is a key in the `nodes` dictionary; `n` and `t` are integers provided by the input; `edges` is an empty list; `empty` is True; the loop has executed `n - 1` times, with each iteration adding an edge between two nodes `u` and `v` read from the input.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: `nodes` is a defaultdict where each key `u` has a list of connected nodes `v` and must have at least one key-value pair. `leaves` is a deque that includes all keys from `nodes` that have exactly one element in their list of connected nodes.
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `nodes` is a defaultdict where each key `u` has a list of connected nodes `v` and must have at least one key-value pair; `leaves` is a deque that includes all keys from `nodes` that have exactly one element in their list of connected nodes; `start` is an input integer; `moves` is the value returned by `func_1(nodes, start)`. If `moves` includes at least one odd number, then `moves` contains at least one odd number. Otherwise, none of the elements in `moves` are odd numbers.
#Overall this is what the function does:The function reads input to construct a graph represented by a dictionary of nodes and their neighbors. It identifies leaf nodes (nodes with only one connection) and a starting node. It then processes the graph starting from the given node and determines if any of the resulting moves are odd. Based on this, it prints either "Ron" or "Hermione".

