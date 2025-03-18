#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the largest integer in the list `l`.
#Overall this is what the function does:The function `func_1` accepts a non-empty list of integers `l` and returns the index of the largest integer in the list. After the function concludes, the list `l` remains unchanged, and the user receives the index of the largest integer in `l`.

#State of the program right berfore the function call: No variables are passed in the function signature. The function reads input values for n and the edges of the tree directly from stdin. n is an integer such that 1 ≤ n ≤ 2 · 10^3, and the edges are pairs of integers (u, v) such that 1 ≤ u, v ≤ n and u ≠ v, representing the vertices connected by an edge.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: `u2vs` is a list of `n` lists where each list contains the indices (0-based) of the vertices connected to the corresponding vertex by an edge. The length of each list in `u2vs` will be the degree of the corresponding vertex.
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
        
    #State: The `path_ba` list contains the indices of the vertices in the shortest path from vertex `b` to vertex `0`, in reverse order (from `b` to `0`). The `previous` list remains unchanged. The `d` list remains unchanged. The `_` variable remains unchanged. The `a` and `b` variables remain unchanged.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: Output State: The `ops` list now contains tuples where the first element is the middle element `c` of the `path_ba` list, and the second element is the index `i` ranging from 0 to `ci` (inclusive). The length of the `ops` list is `ci + 1`. The `path_ba`, `previous`, `d`, `_`, `a`, `b`, `ci`, and `c` variables remain unchanged.
    else :
        c2 = len(path_ba) // 2
        c1 = c2 - 1
        for i in range(1, len(path_ba) - c1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: Output State: The `ops` list contains pairs of the form `(c1, i)` and `(c2, i)` for each `i` in the range from `1` to `len(path_ba) - c1` with a step of `2`. The `path_ba` list, `previous` list, `d` list, `_` variable, `a` variable, and `b` variable remain unchanged. `c1` and `c2` also remain unchanged.
    #State: The `path_ba` list contains the indices of the vertices in the shortest path from vertex `b` to vertex `0`, in reverse order (from `b` to `0`). The `previous` list remains unchanged. The `d` list remains unchanged. The `_` variable remains unchanged. The `a` and `b` variables remain unchanged. The `ops` list is now populated based on the length of `path_ba`. If the length of `path_ba` is odd, the `ops` list contains tuples where the first element is the middle element `c` of the `path_ba` list, and the second element is the index `i` ranging from 0 to `ci` (inclusive), with the length of the `ops` list being `ci + 1`. If the length of `path_ba` is even, the `ops` list contains pairs of the form `(c1, i)` and `(c2, i)` for each `i` in the range from `1` to `len(path_ba) - c1` with a step of `2`. The `c1` and `c2` variables remain unchanged.
    print(len(ops))
    #This is printed: len(ops) (where len(ops) is `ci + 1` if the length of `path_ba` is odd, and `len(path_ba) - c1` if the length of `path_ba` is even)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: (c + 1 0
    #c + 1 1
    #...
    #c + 1 ci) (if the length of `path_ba` is odd) or (c1 + 1 1
    #c2 + 1 1
    #c1 + 1 3
    #c2 + 1 3
    #...
    #c1 + 1 (len(path_ba) - c1 - 1)
    #c2 + 1 (len(path_ba) - c1 - 1)) (if the length of `path_ba` is even)
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` reads an integer `n` and a list of edges from standard input, where `n` is the number of vertices in a tree and each edge is a pair of integers representing connected vertices. It constructs an adjacency list `u2vs` for the tree. The function then performs a breadth-first search (BFS) starting from vertex `0` to find a vertex `a` with the maximum distance from `0`. Another BFS is performed starting from vertex `a` to find a vertex `b` with the maximum distance from `a`. The function computes the shortest path from `b` to `0` and populates a list `ops` based on the length of this path. If the length of the path is odd, `ops` contains tuples where the first element is the middle vertex of the path, and the second element is the index ranging from 0 to the middle index. If the length is even, `ops` contains pairs of tuples where the first elements are the two middle vertices of the path, and the second element is the index ranging from 1 to the length of the path minus the first middle index, in steps of 2. The function prints the length of `ops` and the contents of `ops` in a specific format, and returns `None`.

