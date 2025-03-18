#State of the program right berfore the function call: The function `func_1` does not take any parameters, but it reads input from the user. The first input is an integer `n` such that 1 <= n <= 1000. The next `n` inputs are tuples of three integers each, representing the coordinates and radius of each disk: `x[i]`, `y[i]` are integers such that -10^9 <= x[i], y[i] <= 10^9, and `r[i]` is a positive integer such that 1 <= r[i] <= 10^9.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `x` is a list of length `n` with all elements initialized to integers, `y` is a list of length `n` with all elements initialized to integers, `r` is a list of length `n` with all elements initialized to integers, `visited` is a list of length `n` with all elements initialized to `False`, `coef` is a list of length `n` with all elements initialized to `None`.
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
        
    #State: `x` is a list of length `n` with all elements initialized to integers, `y` is a list of length `n` with all elements initialized to integers, `r` is a list of length `n` with all elements initialized to integers, `visited` is a list of length `n` with all elements initialized to `False`, `coef` is a list of length `n` where each element is either `1` or `None` depending on whether the corresponding index was visited or not, `tot` is 0, `bipartite` is `True`, `ok` is `True` if at least one `dfs` call resulted in `bipartite` being `True` and `tot` not being `0`, otherwise `ok` is `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`x` is a list of length `n` with all elements initialized to integers, `y` is a list of length `n` with all elements initialized to integers, `r` is a list of length `n` with all elements initialized to integers, `visited` is a list of length `n` with all elements initialized to `False`, `coef` is a list of length `n` where each element is either `1` or `None` depending on whether the corresponding index was visited or not, `tot` is 0, `bipartite` is `True`. If `ok` is `True`, it indicates that at least one `dfs` call resulted in `bipartite` being `True` and `tot` not being `0`. Otherwise, `ok` is `False`.
#Overall this is what the function does:The function `func_1` reads an integer `n` and `n` tuples of coordinates and radii of disks from the user. It then processes these disks to determine if there is at least one set of disks that can be colored in a bipartite manner (i.e., no two overlapping disks have the same color) and that set is not empty. If such a set exists, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. After the function concludes, the lists `x`, `y`, and `r` contain the coordinates and radii of the disks, `visited` is a list of length `n` with all elements initialized to `False`, and `coef` is a list of length `n` where each element is either `1` or `None` depending on whether the corresponding index was visited or not.

