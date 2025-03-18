#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer 1 ≤ u_1 ≤ n. The tree represented by the edges has exactly two leaves.
def func_1():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: `t` is 1, `u` and `v` are integers determined by user input for each iteration of the loop, `v` is an integer such that 1 ≤ v ≤ n, `n` is an integer such that 2 ≤ n ≤ 2 × 10^5; `edges` is a list containing pairs of integers representing edges between nodes, `empty` is False since the loop has executed and `nodes` is a defaultdict where keys are integers (node IDs) and values are lists of integers (adjacent node IDs).
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: Output State: `t` is 1, `u` and `v` are integers determined by user input for each iteration of the loop, `v` is an integer such that 1 ≤ v ≤ n, `n` is an integer such that 2 ≤ n ≤ 2 × 10^5; `edges` is a list containing pairs of integers representing edges between nodes, `empty` is False, `nodes` is a defaultdict where keys are integers (node IDs) and values are lists of integers (adjacent node IDs), `ends` is a list containing all node IDs that have only one adjacent node after the loop executes all the iterations.
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
        
    #State: The variable `tree` will contain a path from node `s` to node `e` in the graph, and `prev` will be set to `curr` at the end of the loop.
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
    #State: Postcondition: `tree` contains the path from node `s` to node `e` with `e` appended, `prev` is equal to `curr`, `start` is an input integer, `idx` is the index of `start` in `tree`, and `moves` is a list containing `[idx, n - idx - 1]`. If any move in `moves` is odd, then any move in `moves` is odd. If all moves in `moves` are even, then all moves in `moves` are even.
#Overall this is what the function does:The function processes a tree structure defined by user-provided edges and determines whether a specific path within the tree leads to "Ron" or "Hermione" based on the parity of the number of moves required to traverse the path from a given starting node. The function reads the number of nodes \( n \), the number of edges \( t \), and the starting node \( u \). It then constructs the tree and identifies its leaves. After determining a path from one leaf to another, it calculates the number of moves needed to reach a specified starting node and prints either "Ron" or "Hermione" based on the parity of these moves.

