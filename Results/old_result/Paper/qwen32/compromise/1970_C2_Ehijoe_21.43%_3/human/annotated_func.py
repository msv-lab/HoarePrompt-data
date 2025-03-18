#State of the program right berfore the function call: nodes is a dictionary where each key is a node (integer) and its value is a list of integers representing the neighboring nodes; start is an integer representing the starting node; parent is an optional integer representing the parent node of the current node.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns [0]
    #State: nodes is a dictionary where each key is a node (integer) and its value is a list of integers representing the neighboring nodes; start is an integer representing the starting node; parent is an optional integer representing the parent node of the current node. The length of the list of neighbors for the start node is not equal to 1, or if it is equal to 1, the single neighbor is not the parent node.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: 
    return distances
    #The program returns the variable `distances`.
#Overall this is what the function does:The function `func_1` computes distances from a starting node to all other reachable nodes in a graph represented by a dictionary of nodes and their neighbors, excluding paths that revisit the parent node. It returns `[0]` if the starting node has no neighbors other than its parent, otherwise, it returns a list of distances to all reachable nodes.

#State of the program right berfore the function call: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighbors of the node, start is an integer representing the starting node such that 1 <= start <= n, where n is the total number of nodes in the tree.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `nodes` is a defaultdict where keys are integers from 1 to n representing nodes, and values are lists containing the neighboring nodes connected by edges; `start` is an integer representing the starting node such that 1 <= start <= n; `n` is the first integer read from the input; `t` is the second integer read from the input; `edges` is an empty list; `empty` is True.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: `nodes` is a defaultdict where keys are integers from 1 to n representing nodes, and values are lists containing the neighboring nodes connected by edges; `start` is an integer representing the starting node such that 1 <= start <= n; `n` is the first integer read from the input; `t` is the second integer read from the input; `edges` is an empty list; `empty` is True; `leaves` is a deque containing all nodes that have exactly one neighbor (leaf nodes).
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `nodes` is a defaultdict where keys are integers from 1 to n representing nodes, and values are lists containing the neighboring nodes connected by edges; `start` is the integer read from the input; `n` is the first integer read from the input; `t` is the second integer read from the input; `edges` is an empty list; `empty` is True; `leaves` is a deque containing all nodes that have exactly one neighbor (leaf nodes); `moves` is the value returned by `func_1(nodes, start)`. If `moves` contains at least one odd number, then `moves` contains at least one odd number. Otherwise, all elements in `moves` are even numbers.
#Overall this is what the function does:The function reads input values representing a tree structure and a starting node. It then determines if there is at least one node in the tree that can be reached from the starting node in an odd number of moves. If such a node exists, it prints "Ron"; otherwise, it prints "Hermione".

