#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i], y[i] are the coordinates of the center of the i-th disk and r[i] is the radius of the i-th disk with -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for all i in the range [0, n-1]. visited and coef are lists of length n initialized to False and None respectively.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is an integer such that 1 <= n <= 1000; `x` is a list of integers with length `n`; `y` is a list of integers with length `n`; `r` is a list of integers with length `n`; `visited` is a list of length `n` with all elements set to `False`; `coef` is a list of `None` values with length `n`.
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
        
    #State: `n` is an integer such that 1 <= n <= 1000; `x` is a list of integers with length `n`; `y` is a list of integers with length `n`; `r` is a list of integers with length `n`; `visited` is a list of length `n` with all elements set to `True`; `coef` is a list of `None` values with length `n` except for elements corresponding to initially unvisited nodes which are `1`; `tot` is the value it held after the last DFS call; `bipartite` is the result of the last DFS call; `ok` is `True` if any connected component is bipartite and has a non-zero `tot` value; `i` is `n`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is an integer such that 1 <= n <= 1000; `x`, `y`, `r` are lists of integers with length `n`; `visited` is a list of length `n` with all elements set to `True`; `coef` is a list of `None` values with length `n` except for elements corresponding to initially unvisited nodes which are `1`; `tot` is the value it held after the last DFS call; `bipartite` is the result of the last DFS call; `i` is `n`. If `ok` is `True`, at least one connected component is bipartite and has a non-zero `tot` value; if `ok` is `False`, no connected component is bipartite with a non-zero `tot` value.
#Overall this is what the function does:The function reads input values for the number of disks and their respective centers and radii. It then determines if there exists at least one connected component of disks that forms a bipartite graph and has a non-zero total value (`tot`). If such a component exists, it prints "YES"; otherwise, it prints "NO". The function modifies the `visited` list to mark disks as processed and the `coef` list to store coefficients related to the disks.

