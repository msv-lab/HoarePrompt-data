#State of the program right berfore the function call: nodes is a dictionary where each key represents a node (an integer between 1 and n) and its value is a list of integers representing its neighbors, excluding the parent node. start is an integer representing the starting node for the current recursive call, and parent is an integer representing the parent node of the current node (default is None).
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return False
        #The program returns False
    #State: nodes is a dictionary where each key represents a node (an integer between 1 and n) and its value is a list of integers representing its neighbors, excluding the parent node. start is an integer representing the starting node for the current recursive call, and parent is an integer representing the parent node of the current node (default is None). The length of `nodes[start]` is not 1 or the first element of `nodes[start]` is not equal to `parent`.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.append(not func_1(nodes, node, start))
        
    #State: `distances` is a list containing boolean values. Each boolean value is the result of `not func_1(nodes, node, start)` for each node in `nodes[start]` that is not equal to `parent`.
    return any(distances)
    #The program returns True if any element in the list `distances` is True, otherwise it returns False.
#Overall this is what the function does:The function accepts a dictionary `nodes`, an integer `start`, and an integer `parent` (with a default value of None). It checks if the starting node has only one neighbor which is its parent, in which case it returns False. Otherwise, it recursively calls itself for each neighbor of the starting node (excluding the parent), collecting the results in a list `distances`. Finally, it returns True if any element in `distances` is True, otherwise it returns False.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, edges is a list of tuples representing the edges of the tree, each tuple (u, v) indicates an undirected edge between nodes u and v, leaves is a deque containing the leaf nodes of the tree, start is an integer such that 1 ≤ start ≤ n, and moves is a boolean value indicating whether Ron can make a move.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: `empty` is False, `t` is 1, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `edges` is a list of length `n-1` containing pairs of integers representing the edges of the tree, `leaves` is a deque, `start` is an integer such that 1 ≤ start ≤ n, `moves` is a boolean value indicating whether Ron can make a move, `nodes` is a defaultdict where the keys are integers from 1 to n and the values are lists of integers representing the neighbors of each node.
    #
    #In this output state, the `nodes` dictionary is constructed such that for each node `u` from 1 to `n`, its list of neighbors (i.e., the nodes it is directly connected to) is populated based on the input provided within the loop. The `edges` list contains all the edges of the tree as pairs of integers `(u, v)` indicating an edge between nodes `u` and `v`. All other variables remain in their initial or unchanged states.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: Output State: `empty` is False, `t` is 1, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `edges` is a list of length `n-1` containing pairs of integers representing the edges of the tree, `leaves` is a deque containing all the leaf nodes (nodes with only one neighbor) of the tree, `start` is an integer such that 1 ≤ start ≤ n, `moves` is a boolean value indicating whether Ron can make a move, `nodes` is a defaultdict where the keys are integers from 1 to n and the values are lists of integers representing the neighbors of each node.
    start = int(input())
    moves = func_1(nodes, start)
    if moves :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `empty` is False, `t` is 1, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `edges` is a list of length `n-1` containing pairs of integers representing the edges of the tree, `leaves` is a deque containing all the leaf nodes (nodes with only one neighbor) of the tree, `start` is an integer equal to the input integer such that 1 ≤ start ≤ n, `moves` is a boolean value, `nodes` is a defaultdict where the keys are integers from 1 to n and the values are lists of integers representing the neighbors of each node. If `moves` is True, then the function has performed some operation related to the `moves` value being True; if `moves` is not True, then the function has performed some operation related to the `moves` value not being True.
#Overall this is what the function does:The function constructs a tree from input data, identifies all leaf nodes, and determines whether Ron can make a move starting from a specified node. Based on this determination, it prints either 'Ron' or 'Hermione'.

