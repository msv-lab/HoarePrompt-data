#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the largest integer in the list `l`.
#Overall this is what the function does:The function `func_1` accepts a non-empty list of integers `l` and returns the index of the largest integer in the list. After the function concludes, the list `l` remains unchanged, and the user receives the index of the largest integer in the list.

#State of the program right berfore the function call: No variables are passed to the function `func_2()`. The function reads input from the standard input, where the first line contains an integer `n` (1 ≤ n ≤ 2 · 10^3) representing the number of vertices in the tree. The following `n - 1` lines each contain two integers `u` and `v` (1 ≤ u, v ≤ n, u ≠ v) representing an edge between vertices `u` and `v`.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: `n` is an integer between 1 and 2000, inclusive; `u2vs` is a list containing `n` lists, where each list contains integers representing the indices of other lists that are connected to it.
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
        
    #State: The `path_ba` list contains the shortest path from node `b` to node `a` in reverse order, starting from `b` and ending at `a`. The variable `n` is the last node in this path before `a`.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: The `ops` list contains tuples where the first element is the node `c` (the middle node of `path_ba`) and the second element is the index `i` ranging from 0 to `ci` (inclusive). The variables `path_ba`, `n`, and `ci` remain unchanged.
    else :
        ci2 = len(path_ba) // 2
        ci1 = ci2 - 1
        c1 = path_ba[ci1]
        c2 = path_ba[ci2]
        for i in range(1, len(path_ba) - ci1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: The `ops` list contains tuples of the form `(c1, i)` and `(c2, i)` for each `i` starting from 1 and incrementing by 2, up to `len(path_ba) - ci1 - 1`. The values of `path_ba`, `n`, `ci1`, `ci2`, `c1`, and `c2` remain unchanged.
    #State: *The `path_ba` list contains the shortest path from node `b` to node `a` in reverse order, starting from `b` and ending at `a`. The variable `n` is the last node in this path before `a`. The `ops` list is populated based on the length of `path_ba`. If the length of `path_ba` is odd, `ops` contains tuples where the first element is the middle node `c` of `path_ba` and the second element is the index `i` ranging from 0 to `ci` (inclusive). If the length of `path_ba` is even, `ops` contains tuples of the form `(c1, i)` and `(c2, i)` for each `i` starting from 1 and incrementing by 2, up to `len(path_ba) - ci1 - 1`. The values of `path_ba`, `n`, `ci`, `ci1`, `ci2`, `c1`, and `c2` remain unchanged.
    print(len(ops))
    #This is printed: len(ops) (where len(ops) is ci + 1 if the length of path_ba is odd, or ((len(path_ba) - ci1 - 1) // 2) * 2 if the length of path_ba is even)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: [c + 1 0, c + 1 1, ..., c + 1 ci] (if the length of `path_ba` is odd)
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` reads the number of vertices and edges of a tree from standard input. It constructs an adjacency list representation of the tree and then performs a breadth-first search (BFS) to find the shortest path between two specific nodes `a` and `b`. The function then generates a list of operations (`ops`) based on the length of this path. If the path length is odd, it creates operations centered around the middle node of the path. If the path length is even, it creates operations involving the two middle nodes of the path. Finally, the function prints the number of operations and the operations themselves in a specific format, and returns `None`.

