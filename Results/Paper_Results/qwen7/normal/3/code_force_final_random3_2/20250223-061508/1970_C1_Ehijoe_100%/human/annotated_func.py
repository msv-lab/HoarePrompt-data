#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element.
def func_1():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: `i` is equal to `n-1`, `n` must be greater than or equal to `n` (the value provided as input), `u` is an input integer, `v` is an input integer, `nodes[v]` now contains all integers `u` that are connected to `v` through the edges added during the loop iterations.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will be equal to `n-1`, indicating that the loop has completed all `n-1` iterations. The variable `n` will still hold the value it was initialized with, which must be at least 2 for the loop to run even once. The variables `u` and `v` will continue to be the most recently input integers used in the last iteration of the loop. The `nodes` dictionary will contain lists of all nodes connected to each node, reflecting all the edges added during the loop's execution.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: The `ends` list contains all keys from `nodes` where the length of the list associated with each key is exactly 1.
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
        
    #State: Output State: The final state of the loop will be such that `prev` is equal to `curr`, `s` is the first element from the `ends` list, `e` is the second element from the `ends` list, `tree` is a list containing all the nodes traversed from `s` to `e`, and `curr` is equal to `e`.
    #
    #In this final state, the variable `tree` will contain a complete path from the starting node `s` to the ending node `e` as defined by the `nodes` structure. The `prev` and `curr` variables will both point to the last node in this path, which is `e`. The variables `s` and `e` will retain their initial values from the `ends` list, and no changes will have been made to them during the loop's execution.
    tree.append(e)
    start = int(input())
    idx = tree.index(start)
    moves = [idx, n - idx - 1]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: 'Hermione'
    #State: Postcondition: `prev` is equal to `curr`, `s` is the first element from the `ends` list, `e` is the second element from the `ends` list, `tree` is a list containing all the nodes traversed from `s` to `e`, `curr` is equal to `e`, `moves` is a list containing `[idx, n - idx - 1]`, `idx` is the index of `start` in the `tree` list, and either there exists at least one move in `moves` that is odd or all moves in the `moves` list are even numbers.
#Overall this is what the function does:The function constructs a tree from given edge connections and determines whether a specified node traversal path requires an odd or even number of moves. If the total number of moves is odd, it prints 'Ron'; otherwise, it prints 'Hermione'.

