#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, edges is a list of tuples (u, v) where 1 <= u, v <= n, and start is an integer such that 1 <= start <= n.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `tree` is a defaultdict of lists where each key is an integer from 1 to n, and the value for each key is a list containing all the integers that are connected to the key by an edge in the `edges` list. The lists are not necessarily sorted. The variables `n`, `edges`, and `start` remain unchanged.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 1 or dist2 % 2 == 1) :
        return 'Ron'
        #The program returns the string 'Ron'.
    else :
        return 'Hermione'
        #The program returns the string 'Hermione'.
#Overall this is what the function does:The function `func_1` accepts three parameters: `n` (an integer such that 2 <= n <= 2 * 10^5), `edges` (a list of tuples (u, v) where 1 <= u, v <= n), and `start` (an integer such that 1 <= start <= n). It constructs a tree representation from the `edges` list and identifies the leaf nodes. The function then performs a breadth-first search (BFS) from the `start` node to the first two leaf nodes and calculates the distances. If either of these distances is odd, the function returns the string 'Ron'. Otherwise, it returns the string 'Hermione'. The original variables `n`, `edges`, and `start` remain unchanged.

