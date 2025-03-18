#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n where for each i (0 ≤ i < n), x[i], y[i], and r[i] are integers representing the x-coordinate, y-coordinate, and radius of the i-th disk respectively. visited is a list of boolean values of length n indicating whether the i-th disk has been visited during the DFS process. coef is a list of length n initially set to None, used to store coefficients during the DFS process. tot is an integer used to keep track of the total number of disks visited during the current DFS call. bipartite is a boolean variable used to check if the graph formed by the tangency relationships between disks is bipartite.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `n`, `x[i]`, `y[i]`, and `r[i]` will be the last set of integers input by the user for the `n`-th disk, with all values of `x[i]`, `y[i]`, and `r[i]` for `0 ≤ i < n` being the integers input from the user during the loop's execution.
    #
    #In simpler terms, after the loop has completed all its iterations, the index `i` will have reached the value of `n`, meaning the loop has processed all `n` disks. The coordinates (`x[i]`, `y[i]`) and radius (`r[i]`) for the last disk (the `n`-th disk) will be the most recent inputs provided by the user, while the coordinates and radii for the previous disks (from the 0-th to the `(n-1)`-th) will be the inputs given during the corresponding iterations of the loop.
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
        
    #State: Output State: `bipartite` is True, `i` is `n`, `ok` is True, `tot` is 0, all nodes have been visited (`visited[i]` is True for all `i`), and `coef[i]` is 1 for the last node visited.
    #
    #This means that after the loop completes all its iterations, `i` will be equal to `n`, indicating that the loop has processed all nodes up to `n-1`. The variable `bipartite` remains True, suggesting that the graph was determined to be bipartite throughout the process. The variable `ok` is True, indicating that the conditions for the loop to continue were met in each iteration. The variable `tot` remains 0, which might indicate that no cycles were found during the depth-first search (DFS) in any component of the graph. All nodes have been marked as visited, and the `coef` array has been updated such that the last node visited has a coefficient of 1.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `bipartite` is True, `i` is `n`, `ok` is either True or False, `tot` is 0, all nodes have been visited (`visited[i]` is True for all `i`), and the last node visited has a coefficient of 1.
#Overall this is what the function does:The function processes a set of disks represented by their coordinates and radii. It performs a depth-first search (DFS) on the graph formed by the tangency relationships between these disks to determine if the graph is bipartite. If the graph is bipartite and at least one disk is visited during the DFS, the function prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value but modifies the `visited` and `coef` lists and sets the `bipartite` and `ok` flags based on the DFS results.

