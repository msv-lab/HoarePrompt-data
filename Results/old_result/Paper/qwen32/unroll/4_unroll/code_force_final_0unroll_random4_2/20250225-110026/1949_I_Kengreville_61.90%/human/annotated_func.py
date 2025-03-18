#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i], y[i] are the integer coordinates of the center of the i-th disk and r[i] is the radius of the i-th disk (1 <= r[i] <= 10^9), and visited, coef0, and coef1 are lists of length n initialized to False and None respectively.
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
        
    #State: `n` is the integer value provided by the input, `x` is a list of integers with length `n`, `y` is a list of integers with length `n`, `r` is a list of integers with length `n`, `visited` is a list of `False` values with length `n`, `coef0` is a list of `None` values with length `n`, `coef1` is a list of `None` values with length `n`, `nodes` is an empty list.
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
        
    #State: `n` is the integer value provided by the input, `x` is a list of integers with length `n`, `y` is a list of integers with length `n`, `r` is a list of integers with length `n`, `visited` is a list of `True` values for all indices that were visited during the `dfs` traversals, `coef0` is a list of integers with length `n` with values assigned based on the `dfs` function, `coef1` is a list of integers with length `n` with values assigned based on the `dfs` function, `nodes` is an empty list, `ok` is `True` if any `dfs` traversal resulted in a non-zero sum of `coef1` values for the nodes visited.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is the integer value provided by the input, `x` is a list of integers with length `n`, `y` is a list of integers with length `n`, `r` is a list of integers with length `n`, `visited` is a list of `True` values for all indices that were visited during the `dfs` traversals, `coef0` is a list of integers with length `n` with values assigned based on the `dfs` function, `coef1` is a list of integers with length `n` with values assigned based on the `dfs` function, `nodes` is an empty list, and `ok` is `True` if at least one `dfs` traversal resulted in a non-zero sum of `coef1` values for the nodes visited, otherwise `ok` is `False`.
#Overall this is what the function does:The function reads input values representing disks with their centers and radii, performs some form of traversal (likely depth-first search) on these disks, and prints "YES" if any traversal results in a non-zero sum of certain coefficients (`coef1`), otherwise it prints "NO". The function modifies the `visited`, `coef0`, and `coef1` lists during its execution.

#State of the program right berfore the function call: i is an integer such that 0 <= i < n, where n is the number of disks. x, y, and r are lists of integers representing the x-coordinates, y-coordinates, and radii of the disks, respectively. visited is a list of boolean values indicating whether each disk has been visited. nodes is a list that will store the indices of the disks that are part of the current connected component. coef0 and coef1 are lists of values that will be used to store coefficients for the system of equations representing the constraints on the radii.
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
            
        #State: `i` is an integer such that 0 <= i < n, where n is the number of disks. `x`, `y`, and `r` are lists of integers representing the x-coordinates, y-coordinates, and radii of the disks, respectively. `visited` is a list of boolean values indicating whether each disk has been visited, and additional disks directly connected to `i` may now be marked as `True`. `nodes` is a list that will store the indices of the disks that are part of the current connected component and now includes `i` and any disks directly connected to `i` through the DFS. `coef0` and `coef1` are lists of values that will be used to store coefficients for the system of equations representing the constraints on the radii, and they will be updated for disks directly connected to `i`.
    #State: `i` is an integer such that 0 <= i < n, where n is the number of disks. `x`, `y`, and `r` are lists of integers representing the x-coordinates, y-coordinates, and radii of the disks, respectively. `visited` is a list of boolean values indicating whether each disk has been visited. If `visited[i]` was `False`, then `visited[i]` and any disks directly connected to `i` are now marked as `True`, `nodes` includes `i` and any disks directly connected to `i` through the DFS, and `coef0` and `coef1` are updated for disks directly connected to `i`. If `visited[i]` was already `True`, then no changes are made to `visited`, `nodes`, `coef0`, or `coef1`.
#Overall this is what the function does:The function `dfs` performs a depth-first search starting from a given disk index `i`. It marks the disk and all disks directly connected to it as visited, adds their indices to the `nodes` list, and updates the `coef0` and `coef1` lists with coefficients related to the constraints on the radii of the disks in the connected component.

