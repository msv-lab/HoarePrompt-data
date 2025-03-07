#State of the program right berfore the function call: nodes is a list of lists representing the adjacency list of a tree, start is an integer representing the starting node (1 <= start <= len(nodes)), and parent is an integer or None representing the parent node of the starting node.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return False
        #The program returns False.
    #State: nodes is a list of lists representing the adjacency list of a tree, start is an integer representing the starting node (1 <= start <= len(nodes)), and parent is an integer or None representing the parent node of the starting node. The length of nodes[start] is not 1, or if it is 1, nodes[start][0] is not equal to parent.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.append(not func_1(nodes, node, start))
        
    #State: `distances` is a list containing the boolean values returned by `not func_1(nodes, node, start)` for each `node` in `nodes[start]` that is not equal to `parent`. The length of `distances` will be equal to the number of nodes in `nodes[start]` that are not equal to `parent`. The values of `nodes`, `start`, and `parent` remain unchanged.
    return any(distances)
    #The program returns True if any element in the list 'distances' is True, otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts a list of lists `nodes` representing a tree, an integer `start` (1 <= start <= len(nodes)), and an integer or `None` `parent`. It returns `False` if the starting node `start` has only one adjacent node, and that adjacent node is the parent node. Otherwise, it recursively checks the subtree rooted at `start` and returns `True` if any node in the subtree has more than one adjacent node or if any node in the subtree is not directly connected to its parent.

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
        
    #State: `n` and `t` remain unchanged, `nodes` is a defaultdict(list) where each key is an integer representing a node and each value is a list of integers representing the neighbors of that node, `start` remains unchanged, `edges` remains an empty list, `empty` remains True.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: Output State: `n` and `t` remain unchanged, `nodes` remains a defaultdict(list) with the same keys and values as in the initial state, `start` remains unchanged, `edges` remains an empty list, `empty` remains True, `leaves` is a deque containing all the keys from `nodes` that have exactly one neighbor.
    start = int(input())
    moves = func_1(nodes, start)
    if moves :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `n` and `t` remain unchanged, `nodes` remains a defaultdict(list) with the same keys and values as in the initial state, `edges` remains an empty list, `empty` remains True, `leaves` is a deque containing all the keys from `nodes` that have exactly one neighbor, `start` is now an integer provided by the user, and `moves` is the result of `func_1(nodes, start)`. If `moves` evaluates to True, `moves` is not empty. Otherwise, `moves` is empty (i.e., `moves` is `False`).
#Overall this is what the function does:The function `func_2` reads an integer `n` and an integer `t` (which is always 1) from the input, and then constructs a graph represented by a dictionary `nodes` where each key is a node and each value is a list of its neighbors. It identifies all leaf nodes (nodes with exactly one neighbor) and stores them in a deque `leaves`. The function then reads a `start` node from the input and calls another function `func_1` with `nodes` and `start` as arguments. If `func_1` returns a non-empty result, it prints "Ron"; otherwise, it prints "Hermione". The function does not return any value. After the function concludes, `n` and `t` remain unchanged, `nodes` is a defaultdict(list) with the same keys and values as in the initial state, `edges` remains an empty list, `empty` remains True, `leaves` contains all the leaf nodes, and `start` is the integer provided by the user.

