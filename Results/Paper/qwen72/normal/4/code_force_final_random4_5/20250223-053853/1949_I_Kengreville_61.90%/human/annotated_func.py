#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers of length n, where for each i, -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9. visited, coef0, and coef1 are lists of length n initialized to False, 0, and 1 respectively. nodes is an empty list.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef0 = [None] * n
    coef1 = [None] * n
    nodes = []
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of length `n` initialized to `False`, `coef0` is a list of `None` values of length `n`, `coef1` is a list of `None` values of length `n`, `nodes` is an empty list.
    ok = False
    for i in range(n):
        if not visited[i]:
            coef0[i] = 0
            coef1[i] = 1
            nodes = []
            dfs(i)
            c0 = 0
            c1 = 0
            for j in nodes:
                c0 += coef0[j]
                c1 += coef1[j]
            ok = ok or c1 != 0
        
    #State: Output State: `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of length `n` with all elements set to `True`, `coef0` is a list of integers of length `n` with all elements set to `0`, `coef1` is a list of integers of length `n` with all elements set to `1`, `nodes` is an empty list, `ok` is `True` if any `c1` is not `0` after the DFS for any `i`, otherwise `ok` is `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of length `n` with all elements set to `True`, `coef0` is a list of integers of length `n` with all elements set to `0`, `coef1` is a list of integers of length `n` with all elements set to `1`, `nodes` is an empty list. If `ok` is `True`, it means at least one `c1` is not `0` after the DFS for any `i`. If `ok` is `False`, it means for all `i`, `c1` is `0` after the DFS.
#Overall this is what the function does:The function `func_1` reads an integer `n` and then reads `n` lines of input, each containing three integers, which are stored in lists `x`, `y`, and `r` respectively. It then performs a series of depth-first search (DFS) operations on the nodes, updating the `visited`, `coef0`, and `coef1` lists. After all DFS operations, the function checks if the sum of `coef1` values for any set of connected nodes is non-zero. If this condition is met for any set, the function prints 'YES'; otherwise, it prints 'NO'. The final state of the program is that `x`, `y`, and `r` contain the input integers, `visited` is a list of `True` values, `coef0` is a list of `0` values, and `coef1` is a list of `1` values, with `nodes` being an empty list.

#State of the program right berfore the function call: i is a non-negative integer such that 0 <= i < n, where n is the number of disks. x, y, and r are lists of integers, each of length n, where x[i] and y[i] are the coordinates of the center of the i-th disk, and r[i] is the radius of the i-th disk. visited is a list of booleans of length n, where visited[i] indicates whether the i-th disk has been visited. nodes is a list of integers representing the indices of the disks that are part of the current connected component. coef0 and coef1 are lists of integers of length n, used to store coefficients for the i-th disk.
def dfs(i):
    if (not visited[i]) :
        visited[i] = True
        nodes.append(i)
        for j in range(n):
            dx = x[i] - x[j]
            
            dy = y[i] - y[j]
            
            if not visited[j] and (r[i] + r[j]) ** 2 == dx ** 2 + dy ** 2:
                coef0[j] = r[i] + r[j] - coef0[i]
                coef1[j] = -coef1[i]
                dfs(j)
            
        #State: After the loop executes all the iterations, the `visited` list will have `True` for all disks that are directly or indirectly connected to the i-th disk through a chain of disks where the sum of their radii equals the distance between their centers. The `nodes` list will include all indices of these disks. The `coef0` and `coef1` lists will be updated for each disk that is part of the connected component, with `coef0[j]` set to `r[i] + r[j] - coef0[i]` and `coef1[j]` set to `-coef1[i]` for each connected disk `j`. The values of `x`, `y`, and `r` will remain unchanged.
    #State: *If `i` is a non-negative integer such that 0 <= i < n, and `visited[i]` is `False`, then after the loop executes all iterations, the `visited` list will have `True` for all disks that are directly or indirectly connected to the i-th disk through a chain of disks where the sum of their radii equals the distance between their centers. The `nodes` list will include all indices of these disks. The `coef0` and `coef1` lists will be updated for each disk that is part of the connected component, with `coef0[j]` set to `r[i] + r[j] - coef0[i]` and `coef1[j]` set to `-coef1[i]` for each connected disk `j`. The values of `x`, `y`, and `r` will remain unchanged. If `visited[i]` is `True`, the program does not modify any of the lists.
#Overall this is what the function does:The function `dfs` accepts an integer `i` and modifies the `nodes` list to include the indices of all disks that are directly or indirectly connected to the `i`-th disk, where the sum of their radii equals the distance between their centers. It updates the `visited` list to mark these disks as visited. Additionally, it updates the `coef0` and `coef1` lists for each connected disk `j` by setting `coef0[j]` to `r[i] + r[j] - coef0[i]` and `coef1[j]` to `-coef1[i]`. The `x`, `y`, and `r` lists remain unchanged. If the `i`-th disk is already visited, the function does not modify any lists.

