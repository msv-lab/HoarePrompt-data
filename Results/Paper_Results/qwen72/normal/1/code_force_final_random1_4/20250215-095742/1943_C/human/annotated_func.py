#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the maximum value in the list `l`.
#Overall this is what the function does:The function `func_1` accepts a non-empty list of integers `l` and returns the index of the maximum value in the list. After the function concludes, the program has the index of the element in `l` that has the highest value.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the tree, u2vs is a list of lists where each sublist represents the neighbors of a vertex in the tree.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: After the loop executes all iterations, `n` remains unchanged, `_` is `n-2`, `u` and `v` are the last integers read from the input and each decreased by 1, and `u2vs` is a list of lists where each list contains the indices of the vertices connected to the corresponding vertex.
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
        
    #State: The loop continues to append the predecessor of the last element in `path_ba` until it encounters `-1`. At this point, the loop terminates. The final state of `path_ba` will be a list containing the sequence of predecessors starting from `b` and ending with the first vertex that has no predecessor (indicated by `-1`). The variable `n` will be `-1`, indicating the end of the path. The variables `_`, `u`, `v`, `u2vs`, `d`, `previous`, `a`, and `b` remain unchanged from their initial values.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: `i` is `ci`, `ops` contains the tuples `(c, 0)`, `(c, 1)`, ..., `(c, ci)`.
    else :
        c2 = len(path_ba) // 2
        c1 = c2 - 1
        for i in range(1, len(path_ba) - c1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: `path_ba` is a list with a length of at least 9, `i` is the last valid index in the range, `c1` is `c2 - 1`, `c2` is half the length of `path_ba`, `n` is `-1`, `ops` is a list containing tuples for each valid `i` in the range, specifically `(c2 - 1, i)` and `(c2, i)`, and the variables `_`, `u`, `v`, `u2vs`, `d`, `previous`, `a`, and `b` remain unchanged from their initial values.
    #State: *The loop continues to append the predecessor of the last element in `path_ba` until it encounters `-1`. The final state of `path_ba` will be a list containing the sequence of predecessors starting from `b` and ending with the first vertex that has no predecessor (indicated by `-1`). The variable `n` will be `-1`, indicating the end of the path. The variables `_`, `u`, `v`, `u2vs`, `d`, `previous`, `a`, and `b` remain unchanged from their initial values. If the length of `path_ba` is odd, `i` is `ci`, and `ops` contains the tuples `(c, 0)`, `(c, 1)`, ..., `(c, ci)`. If the length of `path_ba` is even, `path_ba` is a list with a length of at least 9, `i` is the last valid index in the range, `c1` is `c2 - 1`, `c2` is half the length of `path_ba`, `n` is `-1`, and `ops` is a list containing tuples for each valid `i` in the range, specifically `(c2 - 1, i)` and `(c2, i)`.
    print(len(ops))
    #This is printed: length of path_ba (where the length of path_ba is even and at least 9)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: c + 1 0
    #c + 1 1
    #c + 1 2
    #c + 1 3
    #c + 1 4
    #c + 1 5
    #c + 1 6
    #c + 1 7
    #c + 1 8
    return None
    #The program returns `None`. The final state of `path_ba` will be a list containing the sequence of predecessors starting from `b` and ending with the first vertex that has no predecessor (indicated by `-1`). The variable `n` will be `-1`, indicating the end of the path. The variables `_`, `u`, `v`, `u2vs`, `d`, `previous`, `a`, and `b` remain unchanged from their initial values. If the length of `path_ba` is odd, `i` is `ci`, and `ops` contains the tuples `(c, 0)`, `(c, 1)`, ..., `(c, ci)`. If the length of `path_ba` is even, `path_ba` is a list with a length of at least 9, `i` is the last valid index in the range, `c1` is `c2 - 1`, `c2` is half the length of `path_ba`, `n` is `-1`, and `ops` is a list containing tuples for each valid `i` in the range, specifically `(c2 - 1, i)` and `(c2, i)`.
#Overall this is what the function does:The function `func_2` reads an integer `n` and constructs a tree represented by a list of lists `u2vs`, where each sublist contains the indices of the vertices connected to the corresponding vertex. It then performs a breadth-first search (BFS) twice to find two specific vertices `a` and `b`. The function constructs a path `path_ba` from `b` to the root vertex (indicated by `-1`). Based on the length of `path_ba`, it generates a list `ops` of operations. If the length of `path_ba` is odd, `ops` contains tuples `(c, 0)`, `(c, 1)`, ..., `(c, ci)`, where `c` is the middle vertex of the path. If the length of `path_ba` is even, `ops` contains tuples `(c1, i)` and `(c2, i)` for each valid index `i`, where `c1` and `c2` are the two middle vertices of the path. The function prints the length of `ops` and the contents of `ops` in a specific format, and returns `None`.

