#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, edges is a list of tuples where each tuple contains two integers representing the nodes of an edge in the tree, and start is an integer representing the starting node where the stone is initially placed.
def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        
        tree[v].append(u)
        
    #State: `tree` is a defaultdict of lists where each key is a node and the corresponding value is a list of nodes that are directly connected to the key node via an edge. The values of `n`, `edges`, and `start` remain unchanged.
    leaves = [node for node in tree if len(tree[node]) == 1]
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if (dist1 % 2 == 0 or dist2 % 2 == 0) :
        return 'Ron'
        #The program returns 'Ron'
    else :
        return 'Hermione'
        #The program returns 'Hermione'
#Overall this is what the function does:The function `func_1` determines the winner of a game based on the distances from a starting node to two leaf nodes in a tree. It accepts an integer `n` representing the number of nodes, a list of tuples `edges` representing the tree's edges, and an integer `start` representing the starting node. The function returns 'Ron' if at least one of the distances from the starting node to any two leaf nodes is even, otherwise it returns 'Hermione'.

