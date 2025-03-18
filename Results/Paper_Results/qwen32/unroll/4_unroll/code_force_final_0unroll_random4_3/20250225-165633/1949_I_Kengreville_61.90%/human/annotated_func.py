#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i], y[i] are the coordinates of the center of the i-th disk and r[i] is the radius of the i-th disk such that -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for all 0 <= i < n. visited, coef0, and coef1 are lists of boolean and integer values respectively, initialized to False and None, of length n. nodes is a list that will be used to store indices during the execution of the function.
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
        
    #State: `n` is an integer such that 1 <= n <= 1000, `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of `False` values of length `n`, `coef0` is a list of `None` values of length `n`, `coef1` is a list of `None` values of length `n`, `nodes` is an empty list.
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
        
    #State: `visited` is a list of `True` values, `coef0` and `coef1` are lists of integers modified by `dfs`, `nodes` is an empty list, `ok` is `True` if any `c1` is not `0`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `visited` is a list of `True` values, `coef0` and `coef1` are lists of integers modified by `dfs`, `nodes` is an empty list, and `ok` is `True` if there is at least one `c1` that is not `0`; otherwise, `ok` is `False` because all `c1` values are `0`.
#Overall this is what the function does:The function `func_1` reads input values for `n` disks, each defined by its center coordinates `(x[i], y[i])` and radius `r[i]`. It processes these disks to determine if there is at least one disk that can be part of a specific configuration (as determined by the `dfs` function, which is not shown in the provided code). The function prints 'YES' if such a configuration exists, otherwise it prints 'NO'. The function modifies the global lists `visited`, `coef0`, `coef1`, and `nodes` during its execution but does not return any value explicitly.

#State of the program right berfore the function call: i is an integer representing the index of a disk, such that 0 <= i < n. x, y, and r are lists of integers where x[i] and y[i] represent the integer coordinates of the center of the i-th disk, and r[i] represents the radius of the i-th disk. visited, nodes, coef0, and coef1 are lists used to keep track of visited disks, nodes in the current DFS traversal, coefficients for radius adjustments, and their signs, respectively. n is the total number of disks.
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
            
        #State: `i` is an integer representing the index of a disk, such that 0 <= i < n. `x`, `y`, and `r` are lists of integers where `x[i]` and `y[i]` represent the integer coordinates of the center of the i-th disk, and `r[i]` represents the radius of the i-th disk. `visited[j]` is `True` for disks `j` that are reachable from disk `i` through the condition satisfied in the loop, and `False` otherwise. `nodes` is a list that includes `i` and possibly other disks that were visited during the DFS traversal. `coef0[j]` and `coef1[j]` are updated for disks `j` that meet the condition in the loop, with `coef0[j] = r[i] + r[j] - coef0[i]` and `coef1[j] = -coef1[i]`. `n` is the total number of disks.
    #State: `i` is an integer representing the index of a disk, such that 0 <= i < n. `x`, `y`, and `r` are lists of integers where `x[i]` and `y[i]` represent the integer coordinates of the center of the i-th disk, and `r[i]` represents the radius of the i-th disk. If `visited[i]` is `False`, then `visited[j]` is `True` for disks `j` that are reachable from disk `i` through the condition satisfied in the loop, and `False` otherwise. `nodes` includes `i` and possibly other disks that were visited during the DFS traversal. `coef0[j]` and `coef1[j]` are updated for disks `j` that meet the condition in the loop, with `coef0[j] = r[i] + r[j] - coef0[i]` and `coef1[j] = -coef1[i]`. If `visited[i]` is `True`, then no changes are made to `visited`, `nodes`, `coef0`, or `coef1`. `n` is the total number of disks.
#Overall this is what the function does:The function `dfs` performs a depth-first search (DFS) starting from a disk at index `i`. It updates the `visited` list to mark disks that are reachable from disk `i`, adds these disks to the `nodes` list, and updates the `coef0` and `coef1` lists based on the radius and position conditions. The function modifies these lists in place but does not return any value.

