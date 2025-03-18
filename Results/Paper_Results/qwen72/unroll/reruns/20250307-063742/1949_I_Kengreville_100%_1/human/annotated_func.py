#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers with length n, where -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for all 0 <= i < n. visited and coef are lists of booleans and integers, respectively, with length n, initially set to False and None.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is an integer input by the user, `x` is a list of integers with length `n`, `y` is a list of integers with length `n`, `r` is a list of integers with length `n`, `visited` is a list of booleans with length `n`, all set to `False`, `coef` is a list of `None` with length `n`.
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
        
    #State: Output State: `n` remains the same, `x` remains the same, `y` remains the same, `r` remains the same, `visited` may have some or all elements set to `True` depending on the `dfs` function, `coef` will have some or all elements set to `1` depending on the `dfs` function, `tot` will be the sum of all `tot` values calculated during the `dfs` calls, `bipartite` will be `True` if all `dfs` calls maintain bipartiteness, otherwise it will be `False`, `ok` will be `True` if at least one `dfs` call maintains bipartiteness and `tot` is not zero, otherwise it will be `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`n`, `x`, `y`, and `r` remain the same. `visited` may have some or all elements set to `True` depending on the `dfs` function. `coef` will have some or all elements set to `1` depending on the `dfs` function. `tot` will be the sum of all `tot` values calculated during the `dfs` calls. `bipartite` will be `True` if all `dfs` calls maintain bipartiteness, otherwise it will be `False`. If `ok` is `True`, it indicates that at least one `dfs` call maintains bipartiteness and `tot` is not zero. If `ok` is `False`, it indicates that no `dfs` call maintains bipartiteness or `tot` is zero.
#Overall this is what the function does:The function `func_1` reads an integer `n` and three lists `x`, `y`, and `r` of length `n` from user input. It then processes these lists to determine if a certain bipartite condition is met. The function modifies the `visited` and `coef` lists, setting some elements of `visited` to `True` and some elements of `coef` to `1`. After processing, if at least one `dfs` call maintains bipartiteness and `tot` is not zero, the function prints 'YES'. Otherwise, it prints 'NO'. The final state of the program is that `n`, `x`, `y`, and `r` remain unchanged, `visited` may have some or all elements set to `True`, `coef` may have some or all elements set to `1`, and the function does not return any value.

