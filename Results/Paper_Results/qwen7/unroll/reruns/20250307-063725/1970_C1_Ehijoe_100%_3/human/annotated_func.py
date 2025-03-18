#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the next line contains t integers u_1, ..., u_t such that 1 ≤ u_i ≤ n.
def func_1():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: `empty` is False, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `u` and `v` are integers such that they were input within the range 1 ≤ u, v ≤ n during the loop, `edges` is an empty list, `nodes` is a defaultdict where the default factory is list, and for each node `i` in the range 1 to `n`, `nodes[i]` contains a list of all nodes directly connected to node `i`.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: Output State: `empty` is False, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `u` and `v` are integers such that they were input within the range 1 ≤ u, v ≤ n during the loop, `edges` is an empty list, `nodes` is a defaultdict where the default factory is list, and for each node `i` in the range 1 to `n`, `nodes[i]` contains a list of all nodes directly connected to node `i`; `ends` is a list containing all nodes that have exactly one connection (degree of 1).
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
        
    #State: The variable `tree` will contain a path from node `s` to node `e` in the graph, and all other variables (`empty`, `n`, `t`, `u`, `v`, `edges`, `nodes`, `ends`, `prev`, and `curr`) will retain their initial states or be unaffected by the loop.
    tree.append(e)
    start = int(input())
    idx = tree.index(start)
    moves = [idx, n - idx - 1]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `tree` now contains the path from node `s` to node `e` with the additional node `e` appended, `start` is an input integer, `idx` is the index of `start` in `tree`, `moves` is a list containing `[idx, n - idx - 1]`. If there exists at least one odd number in the `moves` list, the postcondition remains as initially described. If all moves in the `moves` list are even numbers, the postcondition also remains as initially described.
#Overall this is what the function does:The function processes a graph represented by nodes and their connections. It first constructs the graph from input data, identifies leaf nodes (nodes with only one connection), and then finds a path from one leaf node to another. After determining the starting node for the path, it calculates the number of moves required to reach the end of the path and prints 'Ron' if the total number of moves is odd, otherwise it prints 'Hermione'.

