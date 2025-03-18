#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n where each element (x[i], y[i], r[i]) represents the coordinates (x-coordinate, y-coordinate) and radius of the i-th disk respectively. visited is a list of boolean values of length n indicating whether the i-th disk has been visited during the DFS traversal. coef is a list of floating-point numbers of length n used to store coefficients for the linear equations derived from the tangency conditions.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `n` is an input integer, 1 ≤ n ≤ 1000; `x` is a list of length `n` filled with integers; `y` is a list of length `n` filled with integers; `r` is a list of length `n` filled with integers; `visited` is a list of length `n` filled with `False`; `coef` is a list of length `n` filled with `None`.
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
        
    #State: Output State: `bipartite` is True, `n` is an input integer, 1 ≤ n ≤ 1000; `x` is a list of length `n` filled with integers; `y` is a list of length `n` filled with integers; `r` is a list of length `n` filled with integers; `visited` is a list of length `n` filled with `False`; `coef` is a list of length `n` filled with either `1` or `None`; `tot` is an integer that could be any value since it is not specified how `dfs(i)` affects it; `ok` is `True` if at least one call to `dfs(i)` resulted in `bipartite` being `True` and `tot` not equal to `0`, otherwise `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `bipartite` is True if at least one call to `dfs(i)` resulted in `bipartite` being True and `tot` not equal to 0. Otherwise, `bipartite` is False.
#Overall this is what the function does:The function processes a set of disks represented by their coordinates and radii. It performs a depth-first search (DFS) traversal on these disks to determine if they can be partitioned into two groups such that no two disks in the same group are tangent to each other. If such a partition exists and at least one group contains more than one disk, the function prints 'YES'. Otherwise, it prints 'NO'.

