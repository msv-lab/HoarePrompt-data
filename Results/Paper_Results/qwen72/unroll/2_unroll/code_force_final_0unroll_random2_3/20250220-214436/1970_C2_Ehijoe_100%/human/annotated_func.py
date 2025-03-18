#State of the program right berfore the function call: nodes is a list of lists representing the adjacency list of a tree, start is an integer representing the starting node (1 <= start <= len(nodes)), and parent is an integer representing the parent node of the starting node or None if there is no parent.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return False
        #The program returns False.
    #State: nodes is a list of lists representing the adjacency list of a tree, start is an integer representing the starting node (1 <= start <= len(nodes)), and parent is an integer representing the parent node of the starting node or None if there is no parent. The length of nodes[start] is not 1, or if it is 1, nodes[start][0] is not equal to parent.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.append(not func_1(nodes, node, start))
        
    #State: `distances` is a list containing the results of `not func_1(nodes, node, start)` for each `node` in `nodes[start]` that is not equal to `parent`. The length of `distances` is equal to the number of children of `start` in the tree, excluding the `parent` node. The values in `distances` depend on the return values of `func_1`. The `nodes`, `start`, and `parent` variables remain unchanged.
    return any(distances)
    #The program returns True if any value in the list `distances` is True, otherwise it returns False.
#Overall this is what the function does:The function `func_1` takes three parameters: `nodes` (a list of lists representing the adjacency list of a tree), `start` (an integer representing the starting node, where 1 <= start <= len(nodes)), and `parent` (an integer representing the parent node of the starting node or None if there is no parent). The function returns `False` if the starting node has only one adjacent node, and that node is the parent. Otherwise, it recursively checks the children of the starting node (excluding the parent node) and returns `True` if any of these recursive calls return `False`, otherwise it returns `False`. The function does not modify the `nodes`, `start`, or `parent` parameters.

#State of the program right berfore the function call: n and t are integers where 2 ≤ n ≤ 2×10^5 and t = 1. nodes is a dictionary where each key is an integer representing a node, and the value is a list of integers representing the neighbors of that node. start is an integer representing the starting node, where 1 ≤ start ≤ n.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `n` and `t` remain unchanged, `nodes` is a defaultdict with list as the default factory and contains `n-1` edges added to the graph, `start` remains unchanged, `edges` remains an empty list, `empty` remains True.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: Output State: `n` and `t` remain unchanged, `nodes` is a defaultdict with list as the default factory and contains `n-1` edges added to the graph, `start` remains unchanged, `edges` remains an empty list, `empty` remains True, `leaves` is a deque containing all nodes that have exactly one edge connected to them.
    start = int(input())
    moves = func_1(nodes, start)
    if moves :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *`n` and `t` remain unchanged, `nodes` is a defaultdict with list as the default factory and contains `n-1` edges added to the graph, `start` is the input integer, `edges` remains an empty list, `empty` remains True, `leaves` is a deque containing all nodes that have exactly one edge connected to them, `moves` is the result of `func_1(nodes, start)`. If `moves` is not empty, `moves` is not empty. Otherwise, `moves` is empty or False.
#Overall this is what the function does:The function `func_2` reads an integer `n` and an integer `t` from input, where `2 ≤ n ≤ 2×10^5` and `t = 1`. It then reads `n-1` edges to construct a graph represented as a dictionary `nodes`, where each key is a node and the value is a list of its neighbors. The function identifies all leaf nodes (nodes with exactly one edge) and stores them in a deque `leaves`. It reads an integer `start` from input, representing the starting node. The function calls another function `func_1` with the graph `nodes` and the `start` node, and based on the result of `func_1`, it prints either 'Ron' or 'Hermione'. After the function concludes, `n` and `t` remain unchanged, `nodes` contains the graph with `n-1` edges, `start` is the input integer, `edges` remains an empty list, `empty` remains True, `leaves` contains all leaf nodes, and `moves` is the result of `func_1(nodes, start)`.

