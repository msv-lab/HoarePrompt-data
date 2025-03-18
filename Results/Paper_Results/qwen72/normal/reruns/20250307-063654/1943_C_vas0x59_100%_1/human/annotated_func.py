#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the largest integer in the list `l`.
#Overall this is what the function does:The function `func_1` accepts a non-empty list of integers `l` and returns the index of the largest integer in the list. After the function concludes, the list `l` remains unchanged, and the user receives the index of the largest integer in the list.

#State of the program right berfore the function call: No input parameters are provided for the function `func_2`. The function reads input from the standard input, where the first input is an integer `n` representing the number of vertices in the tree, and the subsequent `n - 1` inputs are pairs of integers `(u, v)` representing the edges of the tree. The values of `u` and `v` are integers such that 1 <= u, v <= n and u ≠ v.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: `n` is an integer greater than or equal to 1, `u2vs` is a list of `n` lists where each list contains the indices of the vertices connected to the corresponding vertex, `_` is `n - 2`, and the values of `u` and `v` are the last input values, each decremented by 1.
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
        
    #State: The loop will continue appending values to `path_ba` until it encounters a value of `-1` in the `previous` list. At the end of the loop, `path_ba` will contain the sequence of vertices that form the path from `b` to the starting vertex, with the last element being `-1`. The variable `n` will be the last value of `previous[path_ba[-1]]` before the loop breaks, which is `-1`. The other variables (`u2vs`, `u`, `v`, `d`, `a`, `previous`, `b`) will remain unchanged.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: `i` is `ci + 1`, `ci` is the integer division of the length of `path_ba` by 2, `path_ba` is a list with an odd length of at least 1, `n` is -1, `ops` is a list containing the tuples `(c, 0)`, `(c, 1)`, ..., `(c, ci)`, `c` is the vertex at the index `ci` in `path_ba`.
    else :
        ci2 = len(path_ba) // 2
        ci1 = ci2 - 1
        c1 = path_ba[ci1]
        c2 = path_ba[ci2]
        for i in range(1, len(path_ba) - ci1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: `i` reaches the maximum value such that `i < len(path_ba) - ci1` and is odd, `path_ba` contains the sequence of vertices from `b` to the starting vertex with the last element being `-1`, `ci1` is `ci2 - 1` where `ci2` is half the length of `path_ba` (an integer), `ops` contains tuples `(c1, i)` and `(c2, i)` for all odd `i` from 1 to the maximum value of `i` that satisfies the loop condition.
    #State: `path_ba` is a list containing the sequence of vertices that form the path from `b` to the starting vertex, with the last element being `-1`. The variable `n` is `-1`. The other variables (`u2vs`, `u`, `v`, `d`, `a`, `previous`, `b`) remain unchanged. `ops` is a list that, if `len(path_ba)` is odd, contains tuples `(c, 0)`, `(c, 1)`, ..., `(c, ci)` where `ci` is the integer division of `len(path_ba)` by 2 and `c` is the vertex at index `ci` in `path_ba`. If `len(path_ba)` is even, `ops` contains tuples `(c1, i)` and `(c2, i)` for all odd `i` from 1 to the maximum value of `i` that is less than `len(path_ba) - ci1`, where `ci1` is `ci2 - 1` and `ci2` is half the length of `path_ba`.
    print(len(ops))
    #This is printed: - The `print(len(ops))` statement will print the length of the `ops` list.
    #   - The length of `ops` depends on whether `L` is odd or even.
    #
    #Let's summarize the possible outputs:
    #
    #- If `L` is odd, `len(ops) = L // 2 + 1`.
    #- If `L` is even, `len(ops) = 2 * (L // 2 // 2)`.
    #
    #Since the exact length of `path_ba` is not provided, we can't compute the exact numerical value of `len(ops)`. However, based on the structure of the problem, the print statement will output the calculated length of `ops`.
    #
    #Output:
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: [c + 1] [i] for each tuple (c, i) in `ops` (where `c` is a vertex in `path_ba` and `i` is an index based on the length of `path_ba` and the conditions described)
    return None
    #The program returns `None`.
#Overall this is what the function does:The function `func_2` reads from the standard input to construct a tree with `n` vertices and `n-1` edges. It then performs a breadth-first search (BFS) from vertex 0 to find a vertex `a` and another BFS from vertex `a` to find a vertex `b`. The function constructs a path from `b` to the starting vertex. Depending on the length of this path, it generates a list of operations `ops` and prints the length of `ops`. Finally, it prints each operation in a specific format and returns `None`. The function does not modify any global state or input parameters.

