#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the largest integer in the list `l`.
#Overall this is what the function does:The function `func_1` accepts a non-empty list of integers `l` and returns the index of the largest integer in the list. After the function concludes, the list `l` remains unchanged, and the user receives the index of the largest integer in the list.

#State of the program right berfore the function call: No variables are passed to the function `func_2()`. The function reads input from the standard input, where the first line contains an integer `n` (1 ≤ n ≤ 2 · 10^3) representing the number of vertices in the tree. The following `n - 1` lines each contain two integers `u` and `v` (1 ≤ u, v ≤ n, u ≠ v) representing the edges of the tree. The function constructs a list of adjacency lists `u2vs` from the input, where `u2vs[u]` contains the list of vertices adjacent to vertex `u`.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: `u2vs` is a list of `n` lists, where each list contains the indices of the vertices that are directly connected to the vertex corresponding to the list's index.
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
        
    #State: `path_ba` is a list containing the indices of vertices from `b` to `0` in the reverse order of the BFS traversal path, and `n` is the index of the last vertex added to `path_ba` before the loop terminates.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: `path_ba` remains a list containing the indices of vertices from `b` to `0` in the reverse order of the BFS traversal path, `n` is the index of the last vertex added to `path_ba` before the loop terminates, `ops` is a list containing tuples where the first element is `c` and the second element is the index `i` ranging from 0 to `ci` inclusive, `ci` is the integer division of the length of `path_ba` by 2, `c` is the vertex at the middle index of `path_ba`.
    else :
        ci2 = len(path_ba) // 2
        ci1 = ci2 - 1
        c1 = path_ba[ci1]
        c2 = path_ba[ci2]
        for i in range(1, len(path_ba) - ci1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: `ops` is a list containing tuples of the form `(c1, i)` and `(c2, i)` for each `i` in the range from 1 to `len(path_ba) - ci1` with a step of 2. `ci1` and `ci2` remain unchanged. `c1` and `c2` remain unchanged. `path_ba` remains unchanged. `n` remains unchanged.
    #State: *`path_ba` is a list containing the indices of vertices from `b` to `0` in the reverse order of the BFS traversal path, `n` is the index of the last vertex added to `path_ba` before the loop terminates, `ops` is an empty list if the length of `path_ba` is even. If the length of `path_ba` is odd, `ops` is a list containing tuples where the first element is `c` and the second element is the index `i` ranging from 0 to `ci` inclusive, `ci` is the integer division of the length of `path_ba` by 2, and `c` is the vertex at the middle index of `path_ba`. If the length of `path_ba` is even, `ops` is a list containing tuples of the form `(c1, i)` and `(c2, i)` for each `i` in the range from 1 to `len(path_ba) - ci1` with a step of 2, where `ci1` and `ci2` remain unchanged, and `c1` and `c2` remain unchanged.
    print(len(ops))
    #This is printed: 0 (if the length of `path_ba` is even) or `len(path_ba) // 2 + 1` (if the length of `path_ba` is odd)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: (nothing printed if the length of `path_ba` is even, or a series of lines in the format `c + 1 i` if the length of `path_ba` is odd, where `c` is the vertex at the middle index of `path_ba` and `i` ranges from 0 to `ci` inclusive, and `ci` is the integer division of the length of `path_ba` by 2)
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` reads from standard input to construct a tree with `n` vertices and `n - 1` edges, represented as an adjacency list `u2vs`. It then performs a breadth-first search (BFS) starting from vertex 0 to find a vertex `a` that is farthest from 0. Another BFS is performed starting from vertex `a` to find a vertex `b` that is farthest from `a`. The function constructs a path `path_ba` from `b` to `0` in reverse BFS order. Depending on the length of `path_ba`, it generates a list of operations `ops`. If the length of `path_ba` is odd, `ops` contains pairs of the form `(c, i)` where `c` is the middle vertex of `path_ba` and `i` ranges from 0 to the middle index. If the length of `path_ba` is even, `ops` contains pairs of the form `(c1, i)` and `(c2, i)` where `c1` and `c2` are the two middle vertices of `path_ba` and `i` ranges from 1 to the length of `path_ba` minus the index of `c1`, with a step of 2. The function prints the number of operations in `ops` and then prints each operation in the format `c + 1 i`. Finally, the function returns `None`.

