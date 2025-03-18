#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers, each of length n, where -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for all 0 <= i < n. visited and coef are lists of length n, initialized to False and None respectively.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` must be greater than 0, `i` is `n-1`, `x`, `y`, and `r` are lists of length `n` where each element at index `i` (0 ≤ `i` < `n`) is assigned the integer values from the corresponding input. `visited` remains a list of length `n` initialized to `False`, and `coef` remains a list of length `n` initialized to `None`.
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
        
    #State: `n` must be greater than 0, `i` is `n-1`, `x`, `y`, and `r` are lists of length `n` with integer values from corresponding inputs, `visited` is a list of length `n` where all elements are `True`, `coef` is a list of length `n` where each element at index `i` (0 ≤ `i` < `n`) is 1 if `visited[i]` was `False` before the loop, `tot` is the number of times `dfs(i)` was called with `i` where `visited[i]` was `False` before the loop, `bipartite` is `True` if all calls to `dfs(i)` kept it `True`, and `ok` is `True` if `bipartite` is `True` and `tot` is not 0.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`n` must be greater than 0, `i` is `n-1`, `x`, `y`, and `r` are lists of length `n` with integer values from corresponding inputs, `visited` is a list of length `n` where all elements are `True`, `coef` is a list of length `n` where each element at index `i` (0 ≤ `i` < `n`) is 1 if `visited[i]` was `False` before the loop, `tot` is the number of times `dfs(i)` was called with `i` where `visited[i]` was `False` before the loop, `bipartite` is `True` if all calls to `dfs(i)` kept it `True`. If `ok` is `True`, then `bipartite` is `True` and `tot` is not 0. If `ok` is `False`, then either `bipartite` is `False` or `tot` is 0.
#Overall this is what the function does:The function `func_1` reads an integer `n` and three lists `x`, `y`, and `r` of integers, each of length `n`. It then processes these lists using a depth-first search (DFS) algorithm to determine if a certain condition (bipartite and non-zero total) is met. If the condition is satisfied, the function prints 'YES'; otherwise, it prints 'NO'. After the function concludes, `n` remains greater than 0, `x`, `y`, and `r` retain their input values, `visited` is a list of length `n` with all elements set to `True`, and `coef` is a list of length `n` where each element at index `i` is 1 if `visited[i]` was `False` before the loop, and `tot` is the number of times `dfs(i)` was called with `i` where `visited[i]` was `False` before the loop. The final state of `bipartite` and `ok` depends on the DFS results.

