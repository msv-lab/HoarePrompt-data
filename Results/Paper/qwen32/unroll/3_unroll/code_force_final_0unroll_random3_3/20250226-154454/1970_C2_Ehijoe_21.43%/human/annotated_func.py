#State of the program right berfore the function call: nodes is a dictionary where each key is a node (integer) and the value is a list of integers representing its neighbors in the tree, start is an integer representing the starting node, and parent is an optional integer representing the parent node of the current node in the recursive call.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns [0]
    #State: nodes is a dictionary where each key is a node (integer) and the value is a list of integers representing its neighbors in the tree, start is an integer representing the starting node, and parent is an optional integer representing the parent node of the current node in the recursive call. The length of the list `nodes[start]` is not equal to 1, or if it is equal to 1, the single element in `nodes[start]` is not equal to `parent`.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: `nodes` is a dictionary where each key is a node (integer) and the value is a list of integers representing its neighbors in the tree, `start` is an integer representing the starting node, `parent` is an optional integer representing the parent node of the current node in the recursive call, and `distances` is a list containing the distances from the original `start` node to all other reachable nodes, each incremented by 1 for each step taken in the recursive calls.
    return distances
    #The program returns a list `distances` containing the distances from the original `start` node to all other reachable nodes, with each distance incremented by 1 for each step taken in the recursive calls.
#Overall this is what the function does:The function `func_1` calculates the distances from a starting node to all other reachable nodes in a tree represented by a dictionary. It returns a list of distances, each incremented by 1 for each step taken. If the starting node has no other neighbors except its parent, it returns `[0]`.

#State of the program right berfore the function call: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing neighboring nodes, start is an integer representing the starting node such that 1 <= start <= n, where n is the total number of nodes in the tree.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `nodes` is a defaultdict where the default value for each key is an empty list; `start` is an integer representing the starting node such that 1 <= start <= n; `n` is 5; `t` is 3; `edges` is an empty list; `empty` is True.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: nodes is a defaultdict where the default value for each key is an empty list; start is an integer representing the starting node such that 1 <= start <= n; n is 5; t is 3; edges is an empty list; empty is True; leaves is an empty deque.
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `nodes` is a defaultdict where the default value for each key is an empty list; `start` is an integer such that 1 <= `start` <= 5; `n` is 5; `t` is 3; `edges` is an empty list; `empty` is True; `leaves` is an empty deque; `moves` is the result of `func_1(nodes, start)`. If there exists at least one element in `moves` that is an odd number, then such an element exists. Otherwise, none of the elements in `moves` are odd numbers.
#Overall this is what the function does:The function reads input to construct a tree represented by a dictionary of nodes and their neighbors. It identifies the leaf nodes and then, using a helper function `func_1`, performs some traversal starting from a specified node. Based on the result of this traversal, it determines whether any of the traversal values are odd. If there is at least one odd value, it prints 'Ron'; otherwise, it prints 'Hermione'.

