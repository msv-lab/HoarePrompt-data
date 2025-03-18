#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers where len(x) == len(y) == len(r) == n, and for each i, -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9. visited, coef0, and coef1 are lists of boolean and integer values, respectively, with len(visited) == len(coef0) == len(coef1) == n. nodes is an empty list.
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
        
    #State: `x` is a list of integers with length `n`, `y` is a list of integers with length `n`, `r` is a list of integers with length `n`, `visited` is a list of `False` values with length `n`, `coef0` is a list of `None` values with length `n`, `coef1` is a list of `None` values with length `n`, and `nodes` is an empty list.
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
        
    #State: Output State: `x` is a list of integers with length `n`, `y` is a list of integers with length `n`, `r` is a list of integers with length `n`, `visited` is a list where each element is `True` if the corresponding index has been visited by the `dfs` function, `coef0` is a list of integers with length `n` where each element is `0` if the corresponding index has been visited by the `dfs` function, `coef1` is a list of integers with length `n` where each element is `1` if the corresponding index has been visited by the `dfs` function, `nodes` is an empty list, `ok` is `True` if any of the `dfs` function calls resulted in a non-empty `nodes` list, otherwise `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`x`, `y`, and `r` are lists of integers with length `n`. `visited` is a list where each element is `True` if the corresponding index has been visited by the `dfs` function. `coef0` is a list of integers with length `n` where each element is `0` if the corresponding index has been visited by the `dfs` function. `coef1` is a list of integers with length `n` where each element is `1` if the corresponding index has been visited by the `dfs` function. `nodes` is an empty list. If `ok` is `True`, at least one of the `dfs` function calls resulted in a non-empty `nodes` list. If `ok` is `False`, none of the `dfs` function calls resulted in a non-empty `nodes` list.
#Overall this is what the function does:The function `func_1` reads an integer `n` and `n` sets of coordinates and radii from the user input. It then processes these inputs using a depth-first search (DFS) algorithm to determine if there is any set of nodes that, when visited, results in a non-zero sum of coefficients (`coef1`). The function modifies the `visited`, `coef0`, and `coef1` lists to reflect the nodes visited by the DFS. Finally, it prints 'YES' if any DFS call results in a non-empty list of nodes, and 'NO' otherwise. After the function concludes, `x`, `y`, and `r` remain lists of integers with length `n`, `visited` is a list of booleans indicating which nodes have been visited, `coef0` is a list of integers where visited nodes have a value of `0`, `coef1` is a list of integers where visited nodes have a value of `1`, and `nodes` is an empty list.

#State of the program right berfore the function call: i is an integer representing the index of a disk, such that 0 <= i < n. n is a positive integer (1 <= n <= 1000) representing the number of disks. x and y are lists of integers representing the x and y coordinates of the centers of the disks, respectively, with -10^9 <= x[i], y[i] <= 10^9 for all 0 <= i < n. r is a list of positive integers representing the radii of the disks, with 1 <= r[i] <= 10^9 for all 0 <= i < n. visited is a list of booleans, where visited[i] is False if the i-th disk has not been visited, and True otherwise. nodes is a list of integers representing the indices of the disks that have been visited. coef0 and coef1 are lists of integers or real numbers, where coef0[i] and coef1[i] are the coefficients used to adjust the radii of the disks.
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
            
        #State: The loop will update the `coef0` and `coef1` lists for all disks `j` that have not been visited and whose centers are exactly at a distance equal to the sum of their radii and the radius of the initially visited disk `i`. The `visited` list and `nodes` list will also be updated to reflect the new disks that have been visited and added to `nodes` through the `dfs` function calls. The values of `x`, `y`, and `r` remain unchanged.
    #State: *`i` is an integer representing the index of a disk, such that 0 <= i < n. `n` is a positive integer (1 <= n <= 1000) representing the number of disks. `x` and `y` are lists of integers representing the x and y coordinates of the centers of the disks, respectively, with -10^9 <= x[i], y[i] <= 10^9 for all 0 <= i < n. `r` is a list of positive integers representing the radii of the disks, with 1 <= r[i] <= 10^9 for all 0 <= i < n. If `visited[i]` is False, the `coef0` and `coef1` lists are updated for all disks `j` that have not been visited and whose centers are exactly at a distance equal to the sum of their radii and the radius of the initially visited disk `i`. The `visited` list and `nodes` list are also updated to reflect the new disks that have been visited and added to `nodes` through the `dfs` function calls. The values of `x`, `y`, and `r` remain unchanged. If `visited[i]` is True, no changes are made to any of the lists.
#Overall this is what the function does:The function `dfs` accepts an integer `i` representing the index of a disk. It marks the disk at index `i` as visited in the `visited` list and adds the index `i` to the `nodes` list. It then recursively visits all disks `j` that have not been visited and whose centers are exactly at a distance equal to the sum of their radii and the radius of the disk at index `i`. For each such disk `j`, it updates the `coef0` and `coef1` lists. The function does not modify the `x`, `y`, or `r` lists.

