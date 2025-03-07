#State of the program right berfore the function call: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighboring nodes. start is an integer representing the starting node. parent is an optional integer representing the parent node, initially set to None.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return False
        #The program returns False
    #State: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighboring nodes. start is an integer representing the starting node. parent is an optional integer representing the parent node, initially set to None. Either the length of the list of neighbors for `start` is not equal to 1, or the first element of the list of neighbors for `start` is not equal to `parent`.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.append(not func_1(nodes, node, start))
        
    #State: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighboring nodes; start is an integer representing the starting node; parent is an optional integer representing the parent node, initially set to None; distances is a list of boolean values, each value being the logical NOT of the result of func_1(nodes, node, start) for each neighbor node of start that is not equal to parent.
    return any(distances)
    #The program returns True if any of the values in the list 'distances' is True; otherwise, it returns False.
#Overall this is what the function does:The function `func_1` determines whether there is a cycle in a graph starting from a given node, excluding the path to its parent node. It returns `False` if the starting node is a leaf node (has only one neighbor, which is the parent) or if no cycles are detected in the subtree rooted at the starting node. It returns `True` if a cycle is detected in the subtree.

#State of the program right berfore the function call: nodes is a dictionary where keys are integers representing nodes and values are lists of integers representing the neighboring nodes, start is an integer representing the starting node such that 1 <= start <= n, where n is the number of nodes in the tree.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `nodes` is a defaultdict where keys are integers representing nodes and values are lists of integers representing the neighboring nodes, populated with the edges provided as input, `start` is an integer representing the starting node such that 1 <= `start` <= n, where n is the number of nodes in the tree, `n` is the first input integer, `t` is the second input integer, `edges` is an empty list, `empty` is `True`.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: nodes is a defaultdict where keys are integers representing nodes and values are lists of integers representing the neighboring nodes, start is an integer representing the starting node such that 1 <= start <= n, where n is the number of nodes in the tree, n is the first input integer, t is the second input integer, edges is an empty list, empty is True, leaves is a deque containing all the leaf nodes from the nodes dictionary.
    start = int(input())
    moves = func_1(nodes, start)
    if moves :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `nodes` is a defaultdict where keys are integers representing nodes and values are lists of integers representing the neighboring nodes, `start` is the integer value provided by the user input such that `1 <= start <= n`, `n` is the first input integer, `t` is the second input integer, `edges` is an empty list, `empty` is True, `leaves` is a deque containing all the leaf nodes from the `nodes` dictionary, and `moves` is the return value of `func_1(nodes, start)`. If `moves` is not empty, it indicates that there are some moves available. Otherwise, `moves` is False, indicating no moves are available.
#Overall this is what the function does:The function reads input to construct a tree represented by a dictionary of nodes and their neighbors, identifies the leaf nodes, and then determines the starting node from user input. It uses an auxiliary function `func_1` to compute some moves starting from the given node. Based on the result from `func_1`, it prints either 'Ron' or 'Hermione'.

