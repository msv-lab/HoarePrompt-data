#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 150,000, m is an integer such that 0 ≤ m ≤ (n * (n - 1)) / 2, and the following pairs (ai, bi) are unique, where 1 ≤ ai, bi ≤ n and ai ≠ bi.
def func():
    n, m = map(int, stdin.readline().rstrip().split())
    graph = {}
    for i in range(n):
        graph[i + 1] = []
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(3 \leq n \leq 150,000\), `i` is \(n\), `graph` is a dictionary where keys range from 1 to `n` and each key maps to an empty list.
    for i in range(m):
        edge = map(int, stdin.readline().rstrip().split())
        
        graph[edge[0]].append(edge[1])
        
        graph[edge[1]].append(edge[0])
        
    #State of the program after the  for loop has been executed: `i` is `m`, `m` is the number of edges, `graph` is a dictionary where each key `k` (where `1 <= k <= n`) maps to a list containing all vertices connected to vertex `k` by an edge.
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
        
    #State of the program after the loop has been executed: `i` is `m`, `m` is the number of edges, `graph` is a dictionary where each key `k` (where `1 <= k <= n`) maps to a list containing all vertices connected to vertex `k` by an edge, `leftToCheck` is an empty set, `isGood` is `False`, `checkMe` is undefined, `neighbors` is an empty list, and `cliqueSize` is 0.
    if isGood :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`i` is `m`, `m` is the number of edges, `graph` is a dictionary where each key `k` (where `1 <= k <= n`) maps to a list containing all vertices connected to vertex `k` by an edge, `leftToCheck` is an empty set, `isGood` is a boolean value (`True` or `False`), `checkMe` is undefined, `neighbors` is an empty list, and `cliqueSize` is 0. If `isGood` is `True`, the console outputs 'YES'. Otherwise, the console outputs 'NO'.
#Overall this is what the function does:The function reads an integer `n` and another integer `m` from standard input, representing the number of vertices and edges in a graph respectively. It then constructs an undirected graph using these inputs. After constructing the graph, the function checks whether every vertex has the same number of neighbors (i.e., whether the graph is a clique). If all vertices have the same number of neighbors, the function prints 'YES', indicating that the graph is a clique; otherwise, it prints 'NO'. The function does not accept any parameters and does not return any value. However, it may raise an error if the input values are out of the specified ranges or if the graph construction fails due to malformed input.

