#State of the program right berfore the function call: l is a list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the maximum value in the list `l`.
#Overall this is what the function does:The function accepts a list of integers and returns the index of the maximum value in the list.

#State of the program right berfore the function call: u2vs is a list of lists where each inner list contains integers representing the vertices adjacent to the corresponding vertex in the tree, n is an integer representing the number of vertices in the tree such that 1 <= n <= 2 * 10^3.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: `u2vs` is a list of `n` lists, where each list at index `i` contains the indices of the vertices directly connected to vertex `i` in the tree.
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
        
    #State: path_ba is a list containing the vertices from `b` to `0` in reverse order, including both `b` and `0`.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: `path_ba` is a list containing the vertices from `b` to `0` in reverse order, including both `b` and `0`, and the length of `path_ba` is odd; `ops` is a list of tuples where each tuple is `(c, i)` for `i` ranging from `0` to `ci` (inclusive), where `c` is the middle vertex of `path_ba` and `ci` is the middle index of `path_ba`; `ci` is the middle index of `path_ba`, which is `(len(path_ba) // 2)`; `c` is the vertex at the middle index of `path_ba`.
    else :
        c2 = len(path_ba) // 2
        c1 = c2 - 1
        for i in range(1, len(path_ba) - c1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: `path_ba` is a list containing the vertices from `b` to `0` in reverse order, including both `b` and `0`; `ops` is a list of tuples `(c1, i)` and `(c2, i)` for `i` values `1, 3, 5, ..., (len(path_ba) - c1 - 1)`.
    #State: `path_ba` is a list containing the vertices from `b` to `0` in reverse order, including both `b` and `0`. If the length of `path_ba` is odd, `ops` is a list of tuples where each tuple is `(c, i)` for `i` ranging from `0` to `ci` (inclusive), where `c` is the middle vertex of `path_ba` and `ci` is the middle index of `path_ba`. If the length of `path_ba` is even, `ops` is a list of tuples `(c1, i)` and `(c2, i)` for `i` values `1, 3, 5, ..., (len(path_ba) - c1 - 1)`.
    print(len(ops))
    #This is printed: len(ops) (where len(ops) is determined by the length of path_ba and the conditions given for constructing ops)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: c+1 0\nc+1 1\nc+1 2\n...\nc+1 ci (if path_ba is odd-length)\nc1+1 1\nc2+1 1\nc1+1 3\nc2+1 3\nc1+1 5\nc2+1 5\n...\nc1+1 (len(path_ba) - c1 - 1)\nc2+1 (len(path_ba) - c1 - 1) (if path_ba is even-length)
    return None
    #The program returns None
#Overall this is what the function does:The function reads a tree structure from the input, computes a path between two specific vertices, and outputs a series of operations based on the length of this path. The operations are printed in a specific format, and the function returns `None`.

