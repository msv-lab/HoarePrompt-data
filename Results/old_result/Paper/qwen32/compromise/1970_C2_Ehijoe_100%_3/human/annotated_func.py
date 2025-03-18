#State of the program right berfore the function call: nodes is a dictionary where keys are node identifiers (integers) and values are lists of integers representing the neighboring nodes, start is an integer representing the starting node, and parent is an optional integer representing the parent node of the current node.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return False
        #The program returns False
    #State: nodes is a dictionary where keys are node identifiers (integers) and values are lists of integers representing the neighboring nodes, start is an integer representing the starting node, and parent is an optional integer representing the parent node of the current node. Additionally, either the length of the list `nodes[start]` is not equal to 1, or if the length is 1, the single element in `nodes[start]` is not equal to `parent`.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.append(not func_1(nodes, node, start))
        
    #State: `nodes` is a dictionary where keys are node identifiers (integers) and values are lists of integers representing the neighboring nodes, `start` is an integer representing the starting node, `parent` is an optional integer representing the parent node of the current node, and `distances` is a list of boolean values where each value is the result of `not func_1(nodes, node, start)` for neighbors `node` of `start` that are not the `parent`.
    return any(distances)
    #The program returns `True` if any value in the `distances` list is `True`; otherwise, it returns `False`.
#Overall this is what the function does:The function `func_1` determines whether there is a cycle in a graph starting from a given node, excluding the path to its parent node. It returns `False` if the starting node is a leaf node or if all paths from the starting node do not form a cycle, and `True` if any path from the starting node forms a cycle.

#State of the program right berfore the function call: nodes is a defaultdict of lists representing the adjacency list of a tree with n nodes, start is an integer representing the starting node where the stone is initially placed, and 1 <= start <= n.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `nodes` is a defaultdict of lists where each key is a node (from 1 to n) and its value is a list of adjacent nodes as defined by the edges input, `start` remains the same integer representing the starting node, `n` remains the first integer read from the input, `t` remains the second integer read from the input, `edges` remains an empty list, `empty` remains True.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: `nodes` is a defaultdict of lists where each key is a node (from 1 to n) and its value is a list of adjacent nodes, `start` remains the same integer representing the starting node, `n` remains the first integer read from the input, `t` remains the second integer read from the input, `edges` remains an empty list, `empty` remains True, `leaves` is a deque containing all nodes that have only one adjacent node (leaf nodes).
    start = int(input())
    moves = func_1(nodes, start)
    if moves :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `nodes` is a defaultdict of lists where each key is a node (from 1 to n) and its value is a list of adjacent nodes, `start` is the integer read from the input, `n` remains the first integer read from the input, `t` remains the second integer read from the input, `edges` remains an empty list, `empty` remains True, `leaves` is a deque containing all nodes that have only one adjacent node (leaf nodes), and `moves` is the value returned by `func_1(nodes, start)`. If `moves` is truthy, then the code proceeds with the if part; otherwise, `moves` is False.
#Overall this is what the function does:The function `func_2` reads input to construct a tree structure and determines a starting node. It then uses this information to call another function `func_1`, passing the tree and the starting node. Based on the result from `func_1`, it prints either "Ron" or "Hermione".

