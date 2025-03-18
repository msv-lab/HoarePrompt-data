#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer 1 ≤ u_1 ≤ n.
def func_1():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: `empty` is False, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `u` and `v` are integers such that 1 ≤ u, v ≤ n, the list of integers for the starting node(s) contains exactly one integer 1 ≤ u_1 ≤ n, `edges` is a list of n-1 edges represented as pairs (u, v), `nodes` is a defaultdict where the default factory is list, and each key in `nodes` corresponds to a node and its value is a list of its adjacent nodes.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: Output State: `empty` is False, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `u` and `v` are integers such that 1 ≤ u, v ≤ n, the list of integers for the starting node(s) contains exactly one integer 1 ≤ u_1 ≤ n, `edges` is a list of n-1 edges represented as pairs (u, v), `nodes` is a defaultdict where the default factory is list, and each key in `nodes` corresponds to a node and its value is a list of its adjacent nodes, `ends` is a list containing all the leaf nodes (nodes with only one adjacent node) in the graph.
    s, e = list(ends)
    tree = [s]
    prev = s
    curr = nodes[s][0]
    while curr != e:
        tree.append(curr)
        
        if nodes[curr][0] == prev:
            prev = curr
            curr = nodes[curr][1]
        else:
            prev = curr
            curr = nodes[curr][0]
        
    #State: The variable `tree` will contain all the leaf nodes from `s` to `e` in the order they are visited during the traversal.
    tree.append(e)
    start = int(input())
    idx = tree.index(start)
    moves = [idx, n - idx - 1]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: 'Ron'
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `tree` contains all the leaf nodes from `s` to `e` in the order they are visited during the traversal, with the additional element `e` appended to it; `start` is an input integer; `idx` is the index of `start` in `tree`; `moves` is a list containing `[idx, n - idx - 1]`. If at least one move in `moves` is odd, the postcondition remains as described in the if part. If all elements in `moves` are even numbers, the postcondition remains as described in the else part.
#Overall this is what the function does:The function processes a tree structure defined by a series of edges and determines whether Ron or Hermione wins based on the parity of certain moves. It first constructs a tree by traversing from a start node to an end node, then calculates the number of moves required to reach the end node from the start node. If at least one of these moves is odd, it prints 'Ron'; otherwise, it prints 'Hermione'.

