#State of the program right berfore the function call: l is a list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the maximum value in the list `l`
#Overall this is what the function does:The function accepts a list of integers and returns the index of the maximum value in the list.

#State of the program right berfore the function call: u2vs is a list of lists where each sublist contains integers representing the vertices connected to the corresponding vertex in a tree, n is an integer representing the number of vertices in the tree, and u and v are integers representing the vertices connected by an edge in the tree such that 0 <= u, v < n.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: `u2vs` is a list of `n` lists, where each list at index `i` contains the indices of all vertices that are directly connected to vertex `i` in the tree.
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
        
    #State: `path_ba` contains the vertices of the shortest path from `b` to `a` in order from `b` to `a`.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: `path_ba` contains the vertices of the shortest path from `b` to `a` in order from `b` to `a`, and the length of `path_ba` is odd; `ops` contains tuples `(c, i)` for `i` ranging from `0` to `ci`, where `ci` is the integer division of the length of `path_ba` by 2, and `c` is the middle element of `path_ba`; `ci` is the integer division of the length of `path_ba` by 2; `c` is the middle element of `path_ba`.
    else :
        c2 = len(path_ba) // 2
        c1 = c2 - 1
        for i in range(1, len(path_ba) - c1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: `ops` contains `[(c1, 1), (c2, 1), (c1, 3), (c2, 3)]`, `path_ba` remains the same, and other variables remain unchanged.
    #State: `path_ba` contains the vertices of the shortest path from `b` to `a` in order from `b` to `a`. If the length of `path_ba` is odd, `ops` contains tuples `(c, i)` for `i` ranging from `0` to `ci`, where `ci` is the integer division of the length of `path_ba` by 2, and `c` is the middle element of `path_ba`. If the length of `path_ba` is even, `ops` contains `[(c1, 1), (c2, 1), (c1, 3), (c2, 3)]`.
    print(len(ops))
    #This is printed: len(ops) (where len(ops) is n // 2 + 1 if the length of path_ba is odd, otherwise 4 if the length of path_ba is even)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: c+1 0\nc+1 1\nc+1 2 (where c is the middle element of path_ba) if length of path_ba is odd, otherwise c1+1 1\nc2+1 1\nc1+1 3\nc2+1 3 (where c1 and c2 are the middle elements of path_ba)
    return None
    #The program returns None
#Overall this is what the function does:The function reads input to construct a tree and then determines a specific path and operations based on the longest path in the tree. It prints the number of operations and the details of each operation. The function does not modify the input parameters and returns `None`.

