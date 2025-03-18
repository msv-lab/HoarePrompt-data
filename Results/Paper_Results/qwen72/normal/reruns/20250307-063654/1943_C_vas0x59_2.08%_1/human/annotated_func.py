#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the maximum value in the list `l`.
#Overall this is what the function does:The function `func_1` accepts a non-empty list of integers `l` and returns the index of the maximum value in the list. After the function concludes, the list `l` remains unchanged, and the user receives the index of the largest integer in the list.

#State of the program right berfore the function call: The function `func_2` does not take any parameters. It reads input from the standard input, where the first input is an integer `n` representing the number of vertices in the tree, and the subsequent `n - 1` inputs are pairs of integers `(u, v)` representing edges between vertices `u` and `v` in the tree. The vertices are 0-indexed, and the edges form a valid tree structure.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: After the loop executes all iterations, `n` must be greater than 1, `_` is a placeholder, `u2vs` is a list of `n` lists where each list contains the indices of the nodes connected to the corresponding node, and each connection is bidirectional.
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
        
    #State: The loop will continue appending the value of `previous[path_ba[-1]]` to `path_ba` until it encounters a value of `-1`. At this point, the loop will terminate. The final `path_ba` will be a list containing the indices of the nodes from `b` to `a` in reverse order, representing the shortest path from `b` to `a` as determined by the `bfs` function. The variable `n` will be `-1` at the end of the loop, indicating that the path has reached the starting node `a`. The values of `u2vs`, `d`, `previous`, `a`, and `b` remain unchanged.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: `i` is `ci + 1`, `ci` is at least 0, `ops` contains `ci + 1` tuples, each of the form `(c, i)` where `i` ranges from 0 to `ci`.
    else :
        c2 = len(path_ba) // 2
        c1 = c2 - 1
        for i in range(1, len(path_ba) - c1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: The loop has completed all iterations, `i` is the last odd number less than `len(path_ba) - c1`, `path_ba` is a list of indices of nodes from `b` to `a` in reverse order, `c1` is `c2 - 1` where `c2` is half the length of `path_ba`, and `ops` is a list containing tuples `(c1, 1)`, `(c2, 1)`, `(c1, 3)`, `(c2, 3)`, ..., `(c1, i)`, `(c2, i)` for all odd `i` from 1 up to the last valid `i`.
    #State: *`path_ba` is a list containing the indices of the nodes from `b` to `a` in reverse order, and `n` is `-1`. If the length of `path_ba` is odd, `i` is `ci + 1`, `ci` is at least 0, and `ops` contains `ci + 1` tuples, each of the form `(c, i)` where `i` ranges from 0 to `ci`. If the length of `path_ba` is even, the loop has completed all iterations, `i` is the last odd number less than `len(path_ba) - c1`, `c1` is `c2 - 1` where `c2` is half the length of `path_ba`, and `ops` is a list containing tuples `(c1, 1)`, `(c2, 1)`, `(c1, 3)`, `(c2, 3)`, ..., `(c1, i)`, `(c2, i)` for all odd `i` from 1 up to the last valid `i`. The values of `u2vs`, `d`, `previous`, `a`, and `b` remain unchanged.
    print(len(ops))
    #This is printed: len(ops) (where len(ops) is `ci + 1` if the length of `path_ba` is odd, and `L / 2` if the length of `path_ba` is even, with `L` being the length of `path_ba`)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: c1 + 1 1
    #c2 + 1 1
    #c1 + 1 3
    #c2 + 1 3
    #...
    #c1 + 1 i
    #c2 + 1 i (where c1 is c2 - 1, c2 is half the length of path_ba, and i is the last odd number less than len(path_ba) - c1)
    return None
    #The program returns `None`.
#Overall this is what the function does:The function `func_2` reads input from the standard input to construct a tree with `n` vertices and `n-1` edges. It then performs a breadth-first search (BFS) starting from vertex 0 to find the farthest vertex `a`. Another BFS is performed starting from `a` to find the farthest vertex `b` and the shortest path from `b` to `a`. Depending on the length of this path, the function constructs a list of operations `ops` and prints the number of operations followed by the operations themselves. If the path length is odd, the operations involve a central vertex `c` and its connections. If the path length is even, the operations involve two central vertices `c1` and `c2` and their connections. The function ultimately returns `None`.

