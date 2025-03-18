#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where each x[i], y[i] satisfies -10^9 <= x[i], y[i] <= 10^9 and each r[i] satisfies 1 <= r[i] <= 10^9. visited and coef are lists of length n initialized with False and None respectively.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is an input integer such that \(1 \leq n \leq 1000\); `x` is a list of length `n` with each element being an integer input by the user; `y` is a list of length `n` with each element being an integer input by the user; `r` is a list of length `n` with each element being an integer input by the user; `visited` is a list of length `n` initialized with `False`; `coef` is a list of length `n` with each element being `None`.
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
        
    #State: `n` is an input integer such that \(1 \leq n \leq 1000\); `x` is a list of length `n` with each element being an integer input by the user; `y` is a list of length `n` with each element being an integer input by the user; `r` is a list of length `n` with each element being an integer input by the user; `visited` is a list of length `n` with all elements being `True`; `coef` is a list of length `n` with each element being `1` for indices that were initially unvisited; `tot` and `bipartite` will have values determined by the `dfs` function; `ok` will be `True` if at least one connected component is bipartite and has a non-zero `tot`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is an input integer such that \(1 \leq n \leq 1000\); `x` is a list of length `n` with each element being an integer input by the user; `y` is a list of length `n` with each element being an integer input by the user; `r` is a list of length `n` with each element being an integer input by the user; `visited` is a list of length `n` with all elements being `True`; `coef` is a list of length `n` with each element being `1` for indices that were initially unvisited; `tot` and `bipartite` have values determined by the `dfs` function; `ok` is `True` if at least one connected component is bipartite and has a non-zero `tot`, otherwise `ok` is `False`.
#Overall this is what the function does:The function `func_1` reads an integer `n` and three lists `x`, `y`, and `r` of length `n` containing integers. It then determines if there is at least one connected component in a graph defined by these lists that is bipartite and has a non-zero total sum of some computed values (`tot`). If such a component exists, it prints "YES"; otherwise, it prints "NO".

