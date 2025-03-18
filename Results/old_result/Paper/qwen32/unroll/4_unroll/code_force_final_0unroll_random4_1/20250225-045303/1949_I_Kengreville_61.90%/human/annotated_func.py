#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of length n, where each element of x and y is an integer such that -10^9 <= x_i, y_i <= 10^9, and each element of r is an integer such that 1 <= r_i <= 10^9. visited, coef0, and coef1 are lists of length n initialized with None. nodes is an initially empty list.
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
        
    #State: `n` is an input integer such that 1 <= `n` <= 1000; `x` is a list of length `n` with elements as integers from the input; `y` is a list of length `n` with elements as integers from the input; `r` is a list of length `n` with elements as integers from the input; `visited` is a list of length `n` with all elements as `False`; `coef0` is a list of length `n` with all elements as `None`; `coef1` is a list of length `n` with all elements as `None`; `nodes` is an empty list.
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
        
    #State: `n` is an input integer such that 1 <= `n` <= 1000; `x` is a list of length `n` with elements as integers from the input; `y` is a list of length `n` with elements as integers from the input; `r` is a list of length `n` with elements as integers from the input; `visited` is a list of length `n` with elements as `True` for all indices that were part of any DFS traversal; `coef0` is a list of length `n` with elements as integers assigned based on DFS traversal; `coef1` is a list of length `n` with elements as integers assigned based on DFS traversal; `nodes` is an empty list; `ok` is `True` if any DFS traversal resulted in a non-zero `c1`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is an input integer such that 1 <= `n` <= 1000; `x` is a list of length `n` with elements as integers from the input; `y` is a list of length `n` with elements as integers from the input; `r` is a list of length `n` with elements as integers from the input; `visited` is a list of length `n` with elements as `True` for all indices that were part of any DFS traversal; `coef0` is a list of length `n` with elements as integers assigned based on DFS traversal; `coef1` is a list of length `n` with elements as integers assigned based on DFS traversal; `nodes` is an empty list; `ok` is `True` if at least one DFS traversal resulted in a non-zero `c1`, otherwise `ok` is `False`.
#Overall this is what the function does:The function `func_1` reads an integer `n` and three lists `x`, `y`, and `r` of length `n` from the input. It uses these lists to perform a series of operations involving depth-first search (DFS) to determine if there exists a non-zero sum of coefficients (`c1`). Based on the result, it prints 'YES' if `c1` is non-zero for any DFS traversal, otherwise it prints 'NO'. The function does not return any value explicitly.

#State of the program right berfore the function call: i is an integer representing the index of a disk, x is a list of integers representing the x-coordinates of the disks, y is a list of integers representing the y-coordinates of the disks, r is a list of integers representing the radii of the disks, visited is a list of booleans indicating whether a disk has been visited, nodes is a list that will store the indices of the disks being processed, coef0 and coef1 are lists of coefficients used in the calculations, and n is the total number of disks.
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
            
        #State: `i` is an integer representing the index of a disk, `x` is a list of integers representing the x-coordinates of the disks, `y` is a list of integers representing the y-coordinates of the disks, `r` is a list of integers representing the radii of the disks, `visited` is a list of booleans indicating whether a disk has been visited (with `visited[j]` set to True for all disks `j` that are touching disk `i` and haven't been visited), `nodes` is a list that will store the indices of the disks being processed and now includes `i` and all disks `j` that are touching `i` and haven't been visited, `coef0` and `coef1` are lists of coefficients used in the calculations (with updated values for all disks `j` that are touching disk `i` and haven't been visited), and `n` is the total number of disks.
    #State: `i` is an integer representing the index of a disk, `x` is a list of integers representing the x-coordinates of the disks, `y` is a list of integers representing the y-coordinates of the disks, `r` is a list of integers representing the radii of the disks, `visited` is a list of booleans indicating whether a disk has been visited, `nodes` is a list that will store the indices of the disks being processed, `coef0` and `coef1` are lists of coefficients used in the calculations, and `n` is the total number of disks. If `visited[i]` is False, then `visited[j]` is set to True for all disks `j` that are touching disk `i` and haven't been visited, `nodes` includes `i` and all disks `j` that are touching `i` and haven't been visited, and `coef0` and `coef1` are updated for all disks `j` that are touching `i` and haven't been visited. If `visited[i]` is True, no changes are made to `visited`, `nodes`, `coef0`, or `coef1`.
#Overall this is what the function does:The function `dfs` processes a disk at index `i` and recursively visits all disks that are touching it and haven't been visited yet. It marks these disks as visited, adds their indices to the `nodes` list, and updates the `coef0` and `coef1` lists with specific calculations based on the radii and positions of the disks.

