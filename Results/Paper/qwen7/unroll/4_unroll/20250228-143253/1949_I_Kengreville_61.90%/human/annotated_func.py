#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, x and y are lists of n integers each, representing the x and y coordinates of the centers of the disks respectively, and r is a list of n integers, representing the radii of the disks respectively. The values of x, y, and r are such that -10^9 ≤ x_i, y_i ≤ 10^9 and 1 ≤ r_i ≤ 10^9 for all i.
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
        
    #State: Output State: `nodes` is an empty list, `coef0` is a list of `n` None values, `n` is the same input integer, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` False values, `coef1` is a list of `n` None values.
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
        
    #State: Output State: `nodes` is an empty list, `coef0` is a list of `n` zeros, `n` is the same input integer, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` True values, `coef1` is a list of `n` ones, `ok` is True.
    #
    #Explanation: The loop iterates over each index `i` from `0` to `n-1`. If `visited[i]` is `False`, it sets `coef0[i]` to `0`, `coef1[i]` to `1`, initializes an empty list `nodes`, and calls the `dfs(i)` function. After the DFS call, it calculates the sum of `coef0` and `coef1` for all nodes in `nodes`. If the sum of `coef1` is not `0`, it sets `ok` to `True`. Since `visited` is set to `True` for each node visited during the DFS, all elements in `visited` will be `True` by the end of the loop. The values of `x`, `y`, and `r` remain unchanged, and `coef0` and `coef1` are updated according to the conditions inside the loop.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `nodes` is an empty list, `coef0` is a list of `n` zeros, `n` is the same input integer, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` True values, `coef1` is a list of `n` ones, and `ok` is True if the sum of `coef1` for all nodes in `nodes` is not 0, otherwise `ok` is False.
#Overall this is what the function does:The function processes a set of disk centers represented by their x and y coordinates and radii. It performs a depth-first search (DFS) on these disks and calculates coefficients (`coef0` and `coef1`) for each disk. Based on the sum of `coef1` values obtained from the DFS, it determines whether to print 'YES' or 'NO'. The final state includes an empty `nodes` list, `coef0` filled with zeros, `coef1` filled with ones, `visited` marked as `True` for all disks, and `ok` set to `True` if the sum of `coef1` is non-zero, otherwise `False`.

#State of the program right berfore the function call: `n` is an integer representing the number of disks, `x`, `y`, and `r` are lists of length `n` containing the x-coordinates, y-coordinates, and radii of the disks respectively, and `visited` is a boolean list of length `n` initialized to `False`. `nodes` is a list used to store the order of visited nodes during the DFS traversal, and `coef0` and `coef1` are lists of length `n` initialized to `0`.
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
            
        #State: visited[j] is True for all j where the condition (r[i] + r[j])
    #State: During the DFS traversal, if `visited[i]` is `False`, then `visited[j]` will be set to `True` for all `j` where the condition (r[i] + r[j]) holds. Otherwise, no changes occur to the `visited` list.
#Overall this is what the function does:The function starts a Depth-First Search (DFS) traversal from the disk indexed by `i`. During the traversal, it marks all disks that are directly touchable (i.e., their distance equals the sum of their radii) from the current disk as visited and records the order of visited disks in the `nodes` list. The function does not return any value.

