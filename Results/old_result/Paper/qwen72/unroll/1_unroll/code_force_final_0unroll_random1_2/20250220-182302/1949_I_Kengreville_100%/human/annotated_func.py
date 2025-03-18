#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers of length n, where for each i, -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9. visited is a list of booleans of length n, initially all set to False. coef is a list of integers of length n, initially all set to None.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of `False` of length `n`, `coef` is a list of `None` of length `n`.
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
        
    #State: `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list where each element is `True` or `False` depending on whether the corresponding index was visited during the DFS, `coef` is a list where each element is `1` if the corresponding index was visited during the DFS, otherwise `None`, `tot` is the total number of nodes visited during the last DFS call, `bipartite` is `True` if the last DFS call found the graph to be bipartite, otherwise `False`, `ok` is `True` if any DFS call found the graph to be bipartite and `tot` is not zero, otherwise `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list where each element is `True` or `False` depending on whether the corresponding index was visited during the DFS, `coef` is a list where each element is `1` if the corresponding index was visited during the DFS, otherwise `None`, `tot` is the total number of nodes visited during the last DFS call, `bipartite` is `True` if the last DFS call found the graph to be bipartite, otherwise `False`. If `ok` is `True` and `tot` is not zero, then at least one DFS call found the graph to be bipartite. Otherwise, `ok` is `False` or `tot` is zero, or both, indicating that no DFS call found the graph to be bipartite or no nodes were visited in the last DFS call.
#Overall this is what the function does:The function `func_1` reads an integer `n` and then reads `n` lines of input, each containing three integers `x[i]`, `y[i]`, and `r[i]`. It then performs a series of depth-first search (DFS) operations on a graph represented by these inputs. After processing, the function prints 'YES' if at least one DFS call found the graph to be bipartite and visited at least one node, otherwise it prints 'NO'. The function modifies the `visited` and `coef` lists: `visited[i]` is set to `True` for each node `i` visited during the DFS, and `coef[i]` is set to `1` for each visited node. The final state of the program includes `x`, `y`, and `r` lists unchanged, `visited` and `coef` lists updated based on the DFS results, and the variables `tot` and `bipartite` reflecting the last DFS call.

