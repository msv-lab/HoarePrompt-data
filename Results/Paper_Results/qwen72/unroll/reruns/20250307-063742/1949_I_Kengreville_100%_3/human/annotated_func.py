#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers with length n, where for each i, -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9. visited and coef are lists of length n, initially all elements of visited are False and all elements of coef are None.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `x` is a list of length `n` with all elements being integers, `y` is a list of length `n` with all elements being integers, `r` is a list of length `n` with all elements being integers, `visited` is a list of length `n` with all elements being `False`, `coef` is a list of length `n` with all elements being `None`.
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
        
    #State: `x` is a list of length `n` with all elements being integers, `y` is a list of length `n` with all elements being integers, `r` is a list of length `n` with all elements being integers, `visited` is a list of length `n` with all elements being `True`, `coef` is a list of length `n` with all elements being `1` or `None`, `tot` is 0, `bipartite` is `True` or `False`, `ok` is `True` if any `bipartite` is `True` and `tot` is not `0` for any `i` in the loop, otherwise `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`x` is a list of length `n` with all elements being integers, `y` is a list of length `n` with all elements being integers, `r` is a list of length `n` with all elements being integers, `visited` is a list of length `n` with all elements being `True`, `coef` is a list of length `n` with all elements being `1` or `None`, `tot` is 0, `bipartite` is `True` or `False`. If `ok` is `True`, there exists at least one index `i` in the loop where `bipartite[i]` is `True` and `tot[i]` is not `0`. If `ok` is `False`, no such index exists.
#Overall this is what the function does:The function reads an integer `n` and three lists of integers `x`, `y`, and `r` of length `n` from user input. It then processes these lists to determine if there exists at least one index `i` such that a depth-first search (DFS) starting from `i` results in a bipartite graph with a non-zero total count. If such an index exists, the function prints 'YES'; otherwise, it prints 'NO'. The function also modifies the `visited` list to mark all indices as `True` and updates the `coef` list with `1` for the starting indices of the DFS. The final state of the program includes `x`, `y`, and `r` as lists of integers, `visited` as a list of `True` values, and `coef` as a list where some elements may be `1` and others remain `None`.

