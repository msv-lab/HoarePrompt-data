#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i] and y[i] are the coordinates of the center of the i-th disk and r[i] is the radius of the i-th disk, with -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for all i in the range [0, n-1]. visited and coef are lists of length n initialized to None and will be used to track visited nodes and coefficients during the DFS traversal, respectively.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is the input integer, `x` is a list of integers with length `n`, `y` is a list of integers with length `n`, `r` is a list of integers with length `n`, `visited` is a list of `False` with length `n`, `coef` is a list of `None` with length `n`.
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
        
    #State: `n` is the input integer, `x` is a list of integers with length `n`, `y` is a list of integers with length `n`, `r` is a list of integers with length `n`, `visited` is a list of `True` with length `n`, `coef` is a list of `None` with some `1`s at indices that were starting points of DFS, `tot` is an integer reflecting the last DFS traversal where `bipartite` is `True` and `tot` is not `0`, `bipartite` is a boolean reflecting the last DFS traversal where `bipartite` is `True` and `tot` is not `0`, `ok` is `True` if at least one DFS traversal resulted in `bipartite` being `True` and `tot` being non-zero; otherwise, it is `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is the input integer, `x` is a list of integers with length `n`, `y` is a list of integers with length `n`, `r` is a list of integers with length `n`, `visited` is a list of `True` with length `n`, `coef` is a list of `None` with some `1`s at indices that were starting points of DFS, `tot` is an integer reflecting the last DFS traversal where `bipartite` is `True` and `tot` is not `0`, `bipartite` is a boolean reflecting the last DFS traversal where `bipartite` is `True` and `tot` is not `0`. If `ok` is `True`, it indicates that at least one DFS traversal resulted in `bipartite` being `True` and `tot` being non-zero. Otherwise, `ok` is `False`, indicating that no DFS traversal resulted in `bipartite` being `True` and `tot` being non-zero.
#Overall this is what the function does:The function reads input for the number of disks and their respective center coordinates and radii. It then performs a Depth-First Search (DFS) on the disks to determine if they can be partitioned into two groups such that no two disks in the same group intersect. If such a partition is possible and at least one disk is counted in the DFS traversal, it prints "YES"; otherwise, it prints "NO".

