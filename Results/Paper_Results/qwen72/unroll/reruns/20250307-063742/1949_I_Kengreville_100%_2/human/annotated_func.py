#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers of length n, where for each i (0 <= i < n), -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9. visited is a list of boolean values of length n, initially all set to False. coef is a list of None values of length n.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: n is an input integer, 1 <= n <= 1000; x is a list of integers of length n; y is a list of integers of length n; r is a list of integers of length n; visited is a list of False values of length n; coef is a list of None values of length n.
    tot = 0
    bipartite = True
    ok = False
    for i in range(n):
        if not visited[i]:
            coef[i] = 1
            tot = 0
            bipartite = True
            dfs(i)
            ok = ok or bipartite and tot != 0
        
    #State: Output State: `n` is an input integer, 1 <= n <= 1000; `x` is a list of integers of length n; `y` is a list of integers of length n; `r` is a list of integers of length n; `visited` is a list where each element is True if the corresponding index was visited during the DFS, otherwise False; `coef` is a list where each element is 1 if the corresponding index was visited during the DFS, otherwise None; `tot` is the total number of nodes visited during the last DFS call; `bipartite` is the result of the last DFS call indicating whether the graph is bipartite; `ok` is True if any DFS call found the graph to be bipartite and visited at least one node, otherwise False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`n` is an input integer, 1 <= n <= 1000; `x` is a list of integers of length n; `y` is a list of integers of length n; `r` is a list of integers of length n; `visited` is a list where each element is True if the corresponding index was visited during the DFS, otherwise False; `coef` is a list where each element is 1 if the corresponding index was visited during the DFS, otherwise None; `tot` is the total number of nodes visited during the last DFS call; `bipartite` is the result of the last DFS call indicating whether the graph is bipartite; `ok` is True if any DFS call found the graph to be bipartite and visited at least one node, otherwise False.
#Overall this is what the function does:The function `func_1` reads an integer `n` and `n` sets of integers (x, y, r) from the input. It then processes these sets using a depth-first search (DFS) algorithm to determine if the graph represented by these sets is bipartite and if at least one node was visited. If any DFS call finds the graph to be bipartite and visits at least one node, the function prints 'YES'. Otherwise, it prints 'NO'. After the function concludes, `n` remains the same, `x`, `y`, and `r` are lists of integers of length `n`, `visited` is a list where each element is `True` if the corresponding index was visited during the DFS, otherwise `False`, `coef` is a list where each element is `1` if the corresponding index was visited during the DFS, otherwise `None`, `tot` is the total number of nodes visited during the last DFS call, `bipartite` is the result of the last DFS call indicating whether the graph is bipartite, and `ok` is `True` if any DFS call found the graph to be bipartite and visited at least one node, otherwise `False`.

