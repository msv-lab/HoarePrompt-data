#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i] and y[i] represent the integer coordinates of the center of the i-th disk and r[i] represents the radius of the i-th disk such that -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9. visited and coef are lists of length n initialized with None, and tot and bipartite are variables used within the function.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is the integer input provided (between 1 and 1000); `x` is a list of `n` integers read from the input; `y` is a list of `n` integers read from the input; `r` is a list of `n` integers read from the input; `visited` is a list of `False` values with length `n`; `coef` is a list of `None` values with length `n`; `tot` and `bipartite` are variables used within the function; `i` is `n`.
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
        
    #State: `n` is the integer input provided (between 1 and 1000), `x` is a list of `n` integers read from the input, `y` is a list of `n` integers read from the input, `r` is a list of `n` integers read from the input, `visited` is a list of boolean values where each element is `True` if the corresponding node was visited during the DFS traversals, `coef` is a list of integers where each element is either `1` or `-1` indicating the bipartition of the graph, `tot` is the sum of the `r` values for nodes in one of the partitions, `bipartite` is `True` if the graph is bipartite and `False` otherwise, `i` is `n` (indicating the loop has completed all iterations), and `ok` is `True` if there exists at least one bipartite component with a non-zero total `r` value, otherwise `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is the integer input provided (between 1 and 1000), `x` is a list of `n` integers read from the input, `y` is a list of `n` integers read from the input, `r` is a list of `n` integers read from the input, `visited` is a list of boolean values where each element is `True` if the corresponding node was visited during the DFS traversals, `coef` is a list of integers where each element is either `1` or `-1` indicating the bipartition of the graph, `tot` is the sum of the `r` values for nodes in one of the partitions, `bipartite` is `True` if the graph is bipartite and `False` otherwise, `i` is `n` (indicating the loop has completed all iterations). If `ok` is `True`, there exists at least one bipartite component with a non-zero total `r` value. If `ok` is `False`, there does not exist any bipartite component with a non-zero total `r` value.
#Overall this is what the function does:The function reads input values representing disks defined by their centers and radii, then determines if there exists at least one bipartite component of disks with a non-zero total radius. It prints 'YES' if such a component exists, otherwise it prints 'NO'.

