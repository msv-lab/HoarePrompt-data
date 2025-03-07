#State of the program right berfore the function call: nodes is a dictionary or list where each key or index represents a node in the tree and the value is a list of adjacent nodes (neighbors). start is an integer representing the starting node, and parent is an integer representing the parent node of the starting node or None if the starting node has no parent.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns a list containing a single element, which is 0.
    #State: nodes is a dictionary or list where each key or index represents a node in the tree and the value is a list of adjacent nodes (neighbors). start is an integer representing the starting node, and parent is an integer representing the parent node of the starting node or None if the starting node has no parent. The length of the list of adjacent nodes for the starting node is not 1, or if it is 1, the single adjacent node is not the parent.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: `nodes` remains unchanged. `start` remains unchanged. `parent` remains unchanged. `distances` is a list containing the distances from the starting node to its adjacent nodes (excluding the parent node), each incremented by 1.
    return distances
    #The program returns the list `distances`, which contains the distances from the starting node to its adjacent nodes (excluding the parent node), each incremented by 1.
#Overall this is what the function does:The function `func_1` accepts parameters `nodes`, `start`, and `parent`. It returns a list of distances from the starting node to all other nodes in the tree, excluding the parent node. If the starting node has no adjacent nodes (or all adjacent nodes are the parent node), it returns a list containing a single element, which is 0. Otherwise, it returns a list of distances, each incremented by 1, representing the distances from the starting node to its adjacent nodes and their descendants. The input `nodes` dictionary or list remains unchanged.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, t is an integer and always equals 1, nodes is a dictionary where each key is an integer representing a node and each value is a list of integers representing the neighbors of that node, start is an integer such that 1 <= start <= n.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `n` and `t` remain unchanged. `nodes` is a defaultdict with list as the default factory, where each key from 1 to n (inclusive) has a list of integers representing the nodes it is connected to. `start` remains unchanged. `edges` is an empty list. `empty` is False.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: Output State: `n` and `t` remain unchanged. `nodes` remains a defaultdict with list as the default factory, where each key from 1 to n (inclusive) has a list of integers representing the nodes it is connected to. `start` remains unchanged. `edges` is an empty list. `empty` is False. `leaves` is a deque containing all the keys from `nodes` that have exactly one connection (i.e., their list has a length of 1).
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *`n` and `t` remain unchanged. `nodes` remains a defaultdict with list as the default factory, where each key from 1 to n (inclusive) has a list of integers representing the nodes it is connected to. `start` is now an input integer. `edges` is an empty list. `empty` is False. `leaves` is a deque containing all the keys from `nodes` that have exactly one connection (i.e., their list has a length of 1). `moves` is the result of the function `func_1(nodes, start)`. If any element in `moves` is an odd number, then at least one element in `moves` is odd. Otherwise, all elements in `moves` are even.
#Overall this is what the function does:The function `func_2` reads an integer `n` and an integer `t` from input, where `2 <= n <= 2 * 10^5` and `t` is always 1. It then reads `n-1` pairs of integers representing edges and constructs a `nodes` dictionary where each key is a node and each value is a list of its neighbors. The function initializes a deque `leaves` with all nodes that have exactly one connection. It reads another integer `start` from input, which is a node in the range `1 <= start <= n`. The function calls `func_1` with `nodes` and `start`, and based on the result, prints either 'Ron' if any move is odd or 'Hermione' if all moves are even. After the function concludes, `n` and `t` remain unchanged, `nodes` is a dictionary of nodes and their neighbors, `start` is the input node, `edges` is an empty list, `empty` is False, `leaves` contains all nodes with exactly one connection, and `moves` is the result of `func_1(nodes, start)`.

