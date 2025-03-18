#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i], y[i] are the coordinates of the center and r[i] is the radius of the i-th disk with -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for all i in the range [0, n-1]. visited and coef are lists of length n initialized to False and None respectively.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is the new input integer, `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of `False` values of length `n`, `coef` is a list of `None` values of length `n`.
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
        
    #State: `visited` is a list of `True` values of length `n`, `coef` is a list of `1` values of length `n`, `tot` is the combined total from all `dfs` calls, `bipartite` is `True` if all components are bipartite, `ok` is `True` if any component is bipartite and has a non-zero `tot`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `visited` is a list of `True` values of length `n`, `coef` is a list of `1` values of length `n`, `tot` is the combined total from all `dfs` calls, `bipartite` is `True` if all components are bipartite, and `ok` is `True` if any component is bipartite and has a non-zero `tot`. If `ok` is `True`, then at least one component is bipartite with a non-zero `tot`. If `ok` is `False`, then no component is bipartite or all bipartite components have a zero `tot`.
#Overall this is what the function does:The function `func_1` reads an integer `n` and three lists `x`, `y`, and `r` of length `n` from the input. Each triplet `(x[i], y[i], r[i])` represents the center coordinates and radius of the i-th disk. The function checks if the disks can be partitioned into two groups such that no two disks in the same group intersect. If such a partition exists and at least one disk is present, it prints 'YES'; otherwise, it prints 'NO'.

