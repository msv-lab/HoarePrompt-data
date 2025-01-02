#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 150,000, m is an integer such that 0 ≤ m ≤ (n * (n - 1)) / 2, and the following pairs (ai, bi) represent distinct members that are friends, with 1 ≤ ai, bi ≤ n and ai ≠ bi.
def func():
    n, m = map(int, stdin.readline().rstrip().split())
    graph = {}
    for i in range(n):
        graph[i + 1] = []
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range \(3 \leq n \leq 150,000\), `m` is an integer within the range \(0 \leq m \leq \frac{n \cdot (n - 1)}{2}\), `graph` is a dictionary where the keys are integers ranging from 1 to `n` and the values are all empty lists.
    for i in range(m):
        edge = map(int, stdin.readline().rstrip().split())
        
        graph[edge[0]].append(edge[1])
        
        graph[edge[1]].append(edge[0])
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range \(3 \leq n \leq 150,000\); `m` is an integer within the range \(0 \leq m \leq \frac{n \cdot (n - 1)}{2}\); `graph` is a dictionary where the keys are integers ranging from 1 to `n`. Each key's value is a list containing all vertices connected to it by edges; `i` is `m`; `edge` is a tuple of integers read from standard input, where `edge[0]` and `edge[1]` represent the two vertices connected by the edge.
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
        
    #State of the program after the loop has been executed: `leftToCheck` is an empty set, `isGood` is `False`, `checkMe` is `None`, `neighbors` is an empty list, `cliqueSize` is 0
    if isGood :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`leftToCheck` is an empty set, `isGood` is either `True` or `False`, `checkMe` is `None`, `neighbors` is an empty list, `cliqueSize` is 0.
#Overall this is what the function does:The function reads in the number of nodes \(n\) and edges \(m\) from standard input, followed by \(m\) pairs representing friendships between nodes. It constructs a graph where each node is connected to its friends. Then, it checks whether the graph contains a clique (a subset of nodes where every two distinct nodes are adjacent) of size \(n\). If such a clique exists, the function prints 'YES'; otherwise, it prints 'NO'. The function operates on the inferred inputs \(n\), \(m\), and friendship pairs \((ai, bi)\), and returns a string indicating whether a full clique exists.

