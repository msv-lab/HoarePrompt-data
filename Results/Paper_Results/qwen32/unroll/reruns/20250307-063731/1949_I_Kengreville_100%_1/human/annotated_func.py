#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x and y are lists of integers where each element satisfies -10^9 <= x[i], y[i] <= 10^9, and r is a list of integers where each element satisfies 1 <= r[i] <= 10^9.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is an input integer, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` `False` values, `coef` is a list of `n` `None` values.
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
        
    #State: `n` is an input integer, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` `True` values, `coef` is a list of `n` integers (values depend on `dfs` execution), `tot` is an integer (value depends on `dfs` execution), `bipartite` is a boolean (value depends on `dfs` execution), `ok` is a boolean (True if at least one DFS finds a bipartite graph with `tot` not equal to zero).
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is an input integer, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` `True` values, `coef` is a list of `n` integers (values depend on `dfs` execution), `tot` is an integer (value depends on `dfs` execution), `bipartite` is a boolean (value depends on `dfs` execution), and `ok` is a boolean. If `ok` is `True`, it indicates that at least one DFS finds a bipartite graph with `tot` not equal to zero. If `ok` is `False`, it indicates that no DFS finds a bipartite graph with `tot` not equal to zero.
#Overall this is what the function does:The function reads an integer `n` and three lists `x`, `y`, and `r` of length `n` from the input. It then determines if there exists at least one connected component in the graph represented by these lists that is bipartite and has a non-zero total weight (where weights are derived from the `r` list). If such a component exists, it prints "YES"; otherwise, it prints "NO".

