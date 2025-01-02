#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 150 000, and m is an integer such that 0 ≤ m ≤ (n * (n - 1)) / 2. The following m lines contain pairs of distinct integers (ai, bi) such that 1 ≤ ai, bi ≤ n and ai ≠ bi, representing that members ai and bi are friends. No pair (ai, bi) repeats within the input.
def func():
    n, m = map(int, stdin.readline().rstrip().split())
    graph = {}
    for i in range(n):
        graph[i + 1] = []
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range [3, 150,000], `m` is an integer, `graph` is a dictionary where each key from 1 to `n` (inclusive) maps to an empty list, and `i` is `n - 1`.
    for i in range(m):
        edge = map(int, stdin.readline().rstrip().split())
        
        graph[edge[0]].append(edge[1])
        
        graph[edge[1]].append(edge[0])
        
    #State of the program after the  for loop has been executed: `i` is `m`, `n` is an integer within the range [3, 150,000], `m` is the number of edges added to the graph, `graph` is an undirected graph represented as a dictionary where each key from 1 to `n` maps to a list of its neighbors.
    leftToCheck = set([(i + 1) for i in range(n)])
    isGood = True
    while len(leftToCheck) > 0:
        checkMe = leftToCheck.pop()
        
        neighbors = graph[checkMe]
        
        cliqueSize = len(neighbors)
        
        for neighbor in neighbors:
            if len(graph[neighbor]) != cliqueSize:
                isGood = False
                leftToCheck = set([])
                break
        
        leftToCheck.discard(set(neighbors))
        
    #State of the program after the loop has been executed: `leftToCheck` is an empty set, `isGood` is `True` if all nodes in the graph form cliques with their neighbors, otherwise `isGood` is `False`, `graph` is the final state of the graph after checking all nodes, `checkMe` is the last node checked, `neighbors` is the list of neighbors of `checkMe` after all checks, `cliqueSize` is the number of neighbors of `checkMe`.
    if isGood :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`leftToCheck` is an empty set, `isGood` is either `True` (indicating all nodes in the graph form cliques with their neighbors) or `False` (if not all nodes form cliques), `graph` is the final state of the graph after checking all nodes, `checkMe` is the last node checked, `neighbors` is the list of neighbors of `checkMe` after all checks, `cliqueSize` is the number of neighbors of `checkMe`. If `isGood` is `True`, printed to console: YES.
#Overall this is what the function does:The function processes a set of friendship pairs among \( n \) members and determines whether all members form cliques with their neighbors. It reads the number of members \( n \) and the number of friendship pairs \( m \) from standard input. It then constructs an undirected graph using adjacency lists. The function checks each member to ensure that every member has the same number of neighbors as all of its neighbors. If all members satisfy this condition, the function prints 'YES'; otherwise, it prints 'NO'. The function handles the case where no pair of friends repeats and ensures that the input constraints are respected. If any member does not form a clique with its neighbors, the function immediately breaks out of the loop and sets the result to 'NO'.

