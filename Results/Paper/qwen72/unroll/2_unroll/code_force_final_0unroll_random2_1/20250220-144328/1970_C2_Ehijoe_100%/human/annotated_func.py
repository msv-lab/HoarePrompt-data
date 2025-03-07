#State of the program right berfore the function call: nodes is a list of lists representing the adjacency list of a tree with n nodes, start is an integer such that 1 <= start <= n, and parent is an integer or None such that if parent is not None, 1 <= parent <= n.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return False
        #The program returns False.
    #State: nodes is a list of lists representing the adjacency list of a tree with n nodes, start is an integer such that 1 <= start <= n, and parent is an integer or None such that if parent is not None, 1 <= parent <= n. The length of nodes[start] is not 1, or if the length of nodes[start] is 1, then nodes[start][0] is not equal to parent.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.append(not func_1(nodes, node, start))
        
    #State: `distances` is a list containing the results of `not func_1(nodes, node, start)` for each `node` in `nodes[start]` that is not equal to `parent`. The length of `distances` is equal to the number of nodes in `nodes[start]` that are not equal to `parent`. The values of `nodes`, `start`, and `parent` remain unchanged.
    return any(distances)
    #The program returns True if any element in the list `distances` is True, otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts a list of lists `nodes` representing the adjacency list of a tree, an integer `start` within the range of the tree's nodes, and an optional integer `parent` also within the range of the tree's nodes. It returns `False` if the node at `start` has only one adjacent node and that node is `parent`. Otherwise, it recursively checks the distance of each adjacent node (excluding `parent`) from the current node. The function returns `True` if any of these recursive checks return `False`, indicating that there is at least one path from the `start` node to a leaf node that does not include `parent`. If all recursive checks return `True`, the function returns `False`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, t is an integer and always equals 1, nodes is a dictionary where each key is an integer representing a node and each value is a list of integers representing the neighbors of that node, and start is an integer such that 1 <= start <= n.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `n` and `t` retain their initial values, `edges` remains an empty list, `nodes` is now a defaultdict with list as the default factory, where each key is an integer representing a node and each value is a list of integers representing the neighbors of that node, populated with the edges provided by the input, `start` retains its initial value, `empty` remains True.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: `n` and `t` retain their initial values, `edges` remains an empty list, `nodes` retains its initial state as a defaultdict with list as the default factory, where each key is an integer representing a node and each value is a list of integers representing the neighbors of that node, `start` retains its initial value, `empty` remains True, `leaves` is now a deque containing all the nodes that have exactly one neighbor.
    start = int(input())
    moves = func_1(nodes, start)
    if moves :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *`n` and `t` retain their initial values, `edges` remains an empty list, `nodes` retains its initial state as a defaultdict with list as the default factory, `start` is now the integer value provided by the user, `empty` remains True, `leaves` is now a deque containing all the nodes that have exactly one neighbor, and `moves` is the value returned by `func_1(nodes, start)`. If `moves` is truthy, `moves` is not None or False. If `moves` is falsy, `moves` is False.
#Overall this is what the function does:The function `func_2` reads an integer `n` and an integer `t` (which is always 1) from the input. It then reads `n-1` pairs of integers representing edges between nodes and constructs a `defaultdict` called `nodes` where each key is a node and each value is a list of its neighbors. The function identifies all nodes with exactly one neighbor and stores them in a `deque` called `leaves`. It reads another integer `start` from the input, which is a node, and calls `func_1` with `nodes` and `start`. If `func_1` returns a truthy value, it prints "Ron"; otherwise, it prints "Hermione". After the function concludes, `n` and `t` retain their initial values, `edges` remains an empty list, `nodes` is a populated `defaultdict` of node neighbors, `start` is the integer value provided by the user, `empty` remains True, and `leaves` contains all nodes with exactly one neighbor.

