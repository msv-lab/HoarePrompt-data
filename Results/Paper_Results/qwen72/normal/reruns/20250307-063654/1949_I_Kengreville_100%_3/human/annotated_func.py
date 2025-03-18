#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers, each of length n, where -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for all 0 <= i < n. visited is a list of booleans, each of length n, initially all set to False. coef is a list of integers, each of length n, initially all set to None.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` must be greater than 0, `i` is `n-1`, `x[i]`, `y[i]`, and `r[i]` are assigned the integer values from the input split by spaces for all `i` from 0 to `n-1`. The `visited` and `coef` lists remain unchanged, with all values being `False` and `None` respectively.
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
        
    #State: `n` must be greater than 0, `i` is `n-1`, `x[i]`, `y[i]`, and `r[i]` are assigned the integer values from the input split by spaces for all `i` from 0 to `n-1`. The `visited` and `coef` lists are updated such that for each `i` from 0 to `n-1`, if `visited[i]` was `False` at the start of the loop, it is now `True` and `coef[i]` is set to 1. `tot` is 0, `bipartite` is `True`, and `ok` is `True` if at least one `bipartite` is `True` and `tot` is not 0 after any iteration, otherwise `ok` remains `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`n` is greater than 0, `i` is `n-1`, `x[i]`, `y[i]`, and `r[i]` are assigned the integer values from the input split by spaces for all `i` from 0 to `n-1`. The `visited` and `coef` lists are updated such that for each `i` from 0 to `n-1`, if `visited[i]` was `False` at the start of the loop, it is now `True` and `coef[i]` is set to 1. `tot` is 0, `bipartite` is `True`. If `ok` was `True` at the start of the if-else block, it remains `True` because at least one `bipartite` is `True` and `tot` is not 0 after any iteration. Otherwise, `ok` remains `False`.
#Overall this is what the function does:The function `func_1` processes a set of inputs representing `n` points in a 2D plane, each with coordinates `(x[i], y[i])` and a radius `r[i]`. It initializes a `visited` list to track which points have been processed and a `coef` list to store coefficients. The function then performs a depth-first search (DFS) on the points, updating the `visited` and `coef` lists. After processing all points, it prints 'YES' if at least one DFS iteration results in a bipartite condition being true and a non-zero total, otherwise it prints 'NO'. The function does not return any value explicitly.

