#State of the program right berfore the function call: n is an integer where 3 ≤ n ≤ 150,000, and m is a non-negative integer representing the number of friendship pairs. The friendship pairs are represented as a list of m tuples (ai, bi), where 1 ≤ ai, bi ≤ n and ai ≠ bi, and no pair appears more than once in the list.
def func():
    n, m = map(int, stdin.readline().rstrip().split())
    graph = {}
    for i in range(n):
        graph[i + 1] = []
        
    #State of the program after the  for loop has been executed: `n` is an integer where 3 ≤ n ≤ 150,000, `m` is a non-negative integer, `graph` is a dictionary with keys from 1 to `n` inclusive, each key mapping to an empty list `[]`, `i` is `n - 1`.
    for i in range(m):
        edge = map(int, stdin.readline().rstrip().split())
        
        graph[edge[0]].append(edge[1])
        
        graph[edge[1]].append(edge[0])
        
    #State of the program after the  for loop has been executed: `n` is an integer where 3 ≤ n ≤ 150,000, `m` is a non-negative integer, `graph` is a dictionary with keys from 1 to `n` inclusive, each key mapping to a list of adjacent nodes based on the edges read from the input.
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
        
    #State of the program after the loop has been executed: `n` is an integer where 3 ≤ n ≤ 150,000, `m` is a non-negative integer, `graph` is a dictionary with keys from 1 to `n` inclusive, each key mapping to a list of adjacent nodes, `leftToCheck` is an empty set, `isGood` is False if any node in the graph has a different number of neighbors than any other node in its connected component, otherwise `isGood` remains True, `checkMe` is the last element removed from `leftToCheck` (or undefined if `leftToCheck` was empty), `neighbors` is the list of adjacent nodes corresponding to the last `checkMe`, `cliqueSize` is the number of elements in the last `graph[checkMe]`).
    if isGood :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer where 3 ≤ n ≤ 150,000, `m` is a non-negative integer, `graph` is a dictionary with keys from 1 to `n` inclusive, each key mapping to a list of adjacent nodes, `leftToCheck` is an empty set, `checkMe` is the last element removed from `leftToCheck` (or undefined if `leftToCheck` was empty), `neighbors` is the list of adjacent nodes corresponding to the last `checkMe`, `cliqueSize` is the number of elements in the last `graph[checkMe]`. If `isGood` is True, then the graph meets the criteria for all nodes in each connected component having the same number of neighbors. If `isGood` is False, at least one node in the graph has a different number of neighbors compared to other nodes in its connected component.
#Overall this is what the function does:The function reads from standard input an integer `n` (where 3 ≤ n ≤ 150,000) representing the number of nodes, and an integer `m` (a non-negative integer) representing the number of friendship pairs. It then reads `m` lines, each containing a pair of integers `(ai, bi)` representing a friendship between nodes `ai` and `bi` (where 1 ≤ ai, bi ≤ n and ai ≠ bi, and no pair appears more than once). The function constructs an undirected graph using these pairs, where each node is represented by a key in a dictionary, and the value is a list of adjacent nodes. The function then checks if every node in each connected component of the graph has the same number of neighbors. If all nodes in each connected component have the same number of neighbors, the function prints 'YES'. Otherwise, it prints 'NO'. After the function completes, the graph is stored in the `graph` dictionary, and the variable `isGood` indicates whether the graph meets the criteria (True for 'YES', False for 'NO'). The function does not return any value.

