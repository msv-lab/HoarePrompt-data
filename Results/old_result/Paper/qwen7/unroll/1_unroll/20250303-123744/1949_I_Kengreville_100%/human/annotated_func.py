#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n where each element is a tuple (x[i], y[i], r[i]) representing the coordinates (x, y) and radius r of the i-th disk. visited is a list of boolean values of length n indicating whether a disk has been visited during the DFS process. coef is a list of floating-point numbers of length n used to store coefficients during the DFS process. tot is an integer used to accumulate the number of disks visited in the current component. bipartite is a boolean flag used to check if the current component is bipartite.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `n` is assigned the value read from input, `x` is a list of length `n` where each element is an integer read from input, `y` is a list of length `n` where each element is an integer read from input, `r` is a list of length `n` where each element is an integer read from input, `x[0]` to `x[n-1]` are integers, `y[0]` to `y[n-1]` are integers, `r[0]` to `r[n-1]` are integers, `visited` is a list of length `n` filled with `False`, `coef` is a list of length `n` filled with `None`.
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
        
    #State: Output State: `bipartite` is True/False based on the result of all `dfs` calls, `n` is the same value read from input, `x` is the same list of length `n` where each element is an integer read from input, `y` is the same list of length `n` where each element is an integer read from input, `r` is the same list of length `n` where each element is an integer read from input, `x[0]` to `x[n-1]` are integers, `y[0] to y[n-1]` are integers, `r[0]` to `r[n-1]` are integers, `visited` is a list of length `n` filled with `True` (since every node will be visited at least once), `coef` is a list of length `n` where each element is either `1` or `None` (set to `1` during the first visit of each component), `tot` is 0, `ok` is True if any `dfs` call resulted in `bipartite` being True and `tot` not equal to 0, otherwise `ok` is False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `bipartite` is True, `n` is the same value read from input, `x` is the same list of length `n` where each element is an integer read from input, `y` is the same list of length `n` where each element is an integer read from input, `r` is the same list of length `n` where each element is an integer read from input, `x[0]` to `x[n-1]` are integers, `y[0] to y[n-1]` are integers, `r[0]` to `r[n-1]` are integers, `visited` is a list of length `n` filled with `True` (since every node will be visited at least once), `coef` is a list of length `n` where each element is either `1` or `None` (set to `1` during the first visit of each component), `tot` is 0, `ok` is True. If `ok` is False, then `bipartite` is False, `n` is the same value read from input, `x` is the same list of length `n` where each element is an integer read from input, `y` is the same list of length `n` where each element is an integer read from input, `r` is the same list of length `n` where each element is an integer read from input, `x[0]` to `x[n-1]` are integers, `y[0] to y[n-1]` are integers, `r[0]` to `r[n-1]` are integers, `visited` is a list of length `n` filled with `True` (since every node will be visited at least once), `coef` is a list of length `n` where each element is either `1` or `None` (set to `1` during the first visit of each component), `tot` is 0, `ok` is False.
#Overall this is what the function does:The function reads the number of disks and their coordinates and radii from input. It then performs a depth-first search (DFS) on each unvisited disk to determine if the component formed by connected disks is bipartite. If any component is found to be bipartite and contains more than one disk, the function prints 'YES'. Otherwise, it prints 'NO'. The function modifies the `visited` list to mark all disks as visited and updates the `coef` list to store coefficients during the DFS process. The final state of the program includes the updated `visited` and `coef` lists, and the output 'YES' or 'NO' based on the bipartite property of the components.

