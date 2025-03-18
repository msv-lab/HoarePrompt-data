#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the maximum value in the list 'l'
#Overall this is what the function does:The function accepts a non-empty list of integers and returns the index of the maximum value within that list.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 ⋅ 10³, u2vs is a list of length n where each element is a list of integers representing the neighbors of the corresponding vertex, and the input format is correct according to the problem description.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: Output State: `n` is an input integer, `u2vs` is a list of length `n` where each element is a list containing two elements: one for each directed edge connected to the corresponding index. The lists represent an undirected graph where `u2vs[u].append(v)` and `u2vs[v].append(u)` add a bidirectional edge between nodes `u` and `v`.
    d, _ = bfs(0)
    a = func_1(d)
    d, previous = bfs(a)
    b = func_1(d)
    path_ba = [b]
    while True:
        n = previous[path_ba[-1]]
        
        if n == -1:
            break
        
        path_ba.append(n)
        
    #State: Output State: `path_ba` is a list containing the shortest path from node 0 to the node pointed by `b` in reverse order.
    #
    #Explanation: The loop continues to append nodes to `path_ba` until it reaches a node with no previous node (`-1`), indicating the start of the path (node 0). Since the loop appends nodes in reverse order, `path_ba` will contain the shortest path from node 0 to the node pointed by `b`, but in reverse order.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: Output State: `ops` is a list containing tuples `(c, i)` where `i` ranges from `0` to `ci` (inclusive), and `c` is the element at index `ci` in `path_ba`.
    else :
        c2 = len(path_ba) // 2
        c1 = c2 - 1
        for i in range(1, len(path_ba) - c1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: Output State: `path_ba` is a list containing the shortest path from node 0 to the node pointed by `b` in reverse order, `ops` is a list containing the following elements: (0, 1), (0, 3), (0, 5), ..., (c2, len(path_ba) - c1 - 2); `c2` is half the length of `path_ba`; `c1` is `c2 - 1`.
    #State: `path_ba` is a list containing the shortest path from node 0 to the node pointed by `b` in reverse order, and `ops` is a list containing either tuples `(c, i)` where `i` ranges from `0` to `ci` (inclusive), and `c` is the element at index `ci` in `path_ba`, or the elements (0, 1), (0, 3), (0, 5), ..., (c2, len(path_ba) - c1 - 2); where `c2` is half the length of `path_ba` and `c1` is `c2 - 1`.
    print(len(ops))
    #This is printed: n / 4 + 1 (where n is the number of elements in path_ba)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: 6 0
    #5 1
    #4 2
    #3 3
    #2 4
    #1 1
    #1 3
    #1 5
    return None
    #The program returns None
#Overall this is what the function does:The function processes an undirected graph represented by an integer `n` and a list `u2vs`. It performs a breadth-first search (BFS) twice to find the shortest path from node 0 to another node, constructs a list of operations based on the path, and prints the count of operations followed by the operations themselves. The function does not return any value.

