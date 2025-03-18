#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i], y[i] are the coordinates of the center of the i-th disk and r[i] is the radius of the i-th disk with -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for each i from 0 to n-1. visited and coef are lists of size n initialized to False and None respectively.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is an integer provided by the user input, `x` is a list of size `n` with elements set to integers from user input, `y` is a list of size `n` with elements set to integers from user input, `r` is a list of size `n` with elements set to integers from user input, `visited` is a list of size `n` initialized to `False`, `coef` is a list of size `n` with all elements `None`.
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
        
    #State: `n` is an integer provided by the user input, `x` is a list of size `n` with elements set to integers from user input, `y` is a list of size `n` with elements set to integers from user input, `r` is a list of size `n` with elements set to integers from user input, `visited` is a list of size `n` with all elements `True`, `coef` is a list of size `n` with the first element of each connected component set to `1` and others `None` or `1` depending on the `dfs(i)` function, `tot` is the sum of values from the last connected component processed, `bipartite` is `True` if all connected components are bipartite, otherwise `False`, `ok` is `True` if at least one connected component is bipartite and its `tot` is not zero.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is an integer provided by the user input, `x` is a list of size `n` with elements set to integers from user input, `y` is a list of size `n` with elements set to integers from user input, `r` is a list of size `n` with elements set to integers from user input, `visited` is a list of size `n` with all elements `True`, `coef` is a list of size `n` with the first element of each connected component set to `1` and others `None` or `1` depending on the `dfs(i)` function, `tot` is the sum of values from the last connected component processed, `bipartite` is `True` if all connected components are bipartite, otherwise `False`. If `ok` is `True`, it indicates that at least one connected component is bipartite and its `tot` is not zero. If `ok` is `False`, it indicates that no connected component is bipartite or the `tot` of all bipartite components is zero.
#Overall this is what the function does:The function reads the number of disks and their respective center coordinates and radii. It then checks if the disks can be partitioned into two groups such that no two disks in the same group intersect. If at least one such partition exists, it prints "YES"; otherwise, it prints "NO".

