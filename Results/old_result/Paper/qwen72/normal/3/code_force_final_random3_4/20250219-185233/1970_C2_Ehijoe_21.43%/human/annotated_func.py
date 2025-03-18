#State of the program right berfore the function call: nodes is a list of lists representing the adjacency list of a tree, start is an integer representing the starting node (1 <= start <= len(nodes)), and parent is an integer representing the parent node of the current node (or None if the current node has no parent).
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns a list containing the single element 0.
    #State: nodes is a list of lists representing the adjacency list of a tree, start is an integer representing the starting node (1 <= start <= len(nodes)), and parent is an integer representing the parent node of the current node (or None if the current node has no parent). The length of nodes[start] is not 1, or if it is 1, then nodes[start][0] is not equal to parent.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: `nodes[start]` has been fully iterated. `distances` is extended with a list of values, each value being `1 + dist` for each `dist` in the list returned by `func_1(nodes, node, start)` for every `node` in `nodes[start]` that is not equal to `parent`. The length of `distances` is the sum of the lengths of all lists returned by `func_1` for valid `node` values.
    return distances
    #The program returns the `distances` list, which has been extended with values calculated as `1 + dist` for each `dist` in the lists returned by `func_1(nodes, node, start)` for every `node` in `nodes[start]` that is not equal to `parent`. The length of `distances` is the sum of the lengths of all these lists.
#Overall this is what the function does:The function `func_1` accepts three parameters: `nodes` (a list of lists representing the adjacency list of a tree), `start` (an integer representing the starting node, where 1 <= start <= len(nodes)), and `parent` (an integer representing the parent node of the current node, or None if the current node has no parent). The function returns a list of distances from the starting node to its descendant nodes, excluding the parent node. If the starting node is a leaf node (i.e., it has only one neighbor, which is its parent), the function returns a list containing the single element 0. Otherwise, it returns a list of distances, where each distance is incremented by 1 to account for the additional step from the starting node to its children.

#State of the program right berfore the function call: n and t are integers where 2 <= n <= 2 * 10^5 and t = 1. The edges list is initially empty and will be populated with pairs of integers (u, v) where 1 <= u, v <= n. start is an integer representing the starting node, where 1 <= start <= n.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `n` must be greater than or equal to 2, `i` is `n - 2`, `nodes` is a defaultdict where each key is an integer from 1 to `n` and each value is a list containing the integers that are connected to the key. Each connection is bidirectional, meaning if `u` is connected to `v`, then `u` will be in `nodes[v]` and `v` will be in `nodes[u]`. The `edges` list remains empty, `start` is an integer between 1 and `n`, and `empty` is True.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: `n` is greater than or equal to 2, `i` is `n - 2`, `nodes` is a defaultdict where each key is an integer from 1 to `n` and each value is a list containing the integers connected to the key, `edges` list remains empty, `start` is an integer between 1 and `n`, `empty` is True, and `leaves` is a deque containing all the integers from 1 to `n` that have exactly one connection in `nodes`.
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *`n` is greater than or equal to 2, `i` is `n - 2`, `nodes` is a defaultdict where each key is an integer from 1 to `n` and each value is a list containing the integers connected to the key, `edges` list remains empty, `start` is an input integer between 1 and `n`, `empty` is True, `leaves` is a deque containing all the integers from 1 to `n` that have exactly one connection in `nodes`, `moves` is the result of `func_1(nodes, start)`. If at least one element in `moves` is an odd number, the function proceeds accordingly. If all elements in `moves` are even, the function proceeds accordingly.
#Overall this is what the function does:The function `func_2` reads an integer `n` and an integer `t` from input, where `2 <= n <= 2 * 10^5` and `t = 1`. It then reads `n - 1` pairs of integers (u, v) representing edges in a graph, constructs a bidirectional adjacency list `nodes` from these edges, and identifies all leaf nodes (nodes with exactly one connection) in a deque `leaves`. The function reads an integer `start` from input, representing the starting node, and calls another function `func_1` with `nodes` and `start` to get a list of moves. If any move in the list is odd, it prints 'Ron'; otherwise, it prints 'Hermione'. The function does not return any value. After the function concludes, `nodes` contains the adjacency list of the graph, `leaves` contains all leaf nodes, and `start` is the input starting node.

