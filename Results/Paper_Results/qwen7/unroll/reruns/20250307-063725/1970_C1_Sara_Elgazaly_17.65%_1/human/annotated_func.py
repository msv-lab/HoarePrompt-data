#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer such that 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: x is an integer obtained from the first input split, y is an integer obtained from the second input split, n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer such that 1 ≤ u_1 ≤ n; lst is a defaultdict where each key is an integer between 1 and n, and the corresponding value is a list of integers representing the nodes connected to the key node by an edge. The loop constructs an undirected graph using the input edges.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: s is False, x is the last node in the path traced by the loop, y is undefined.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Hermione
#Overall this is what the function does:The function reads input to construct an undirected graph and then traverses it to determine whether to print "Hermione" or "Ron". It does not accept any parameters but uses variables `x`, `y`, `lst`, and implicitly `n`, `t`, `u`, `v` from the global scope. After constructing the graph, it starts from node `x` and follows a specific traversal pattern, flipping a boolean `s` at each step. If `s` is `False` after the traversal, it prints "Hermione"; otherwise, it prints "Ron".

