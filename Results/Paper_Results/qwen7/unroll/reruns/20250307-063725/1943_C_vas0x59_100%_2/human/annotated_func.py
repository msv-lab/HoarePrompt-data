#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the maximum value in the list 'l'
#Overall this is what the function does:The function accepts a non-empty list of integers `l` and returns the index of the maximum value within that list.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 \cdot 10^3, u2vs is a list of length n where each element is a list representing the neighbors of the corresponding vertex in the tree, and the input consists of n-1 lines describing the edges of the tree.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: Output State: `n` is an input integer, 1 ≤ n ≤ 2000; `u2vs` is a list of length `n` where each element is a list representing the set of vertices connected to the vertex indexed by the list's position in the `u2vs` list. Each pair `(u, v)` from the input represents an undirected edge between vertices `u` and `v`, and both `u` and `v` are appended to each other's lists in `u2vs`.
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
        
    #State: Output State: `d` is the result of BFS starting from `a`, `previous` is a list representing the path from the start vertex to each vertex, `n` is an input integer, `u2vs` is a list of length `n` where each element is a list representing the set of vertices connected to the vertex indexed by the list's position in the `u2vs` list, `b` is the return value of `func_1(d)`, `path_ba` is a list containing the shortest path from `b` back to `a`.
    #
    #Explanation: The loop continues to append the predecessor of the last element in `path_ba` to `path_ba` until it reaches the start vertex `a`. This process reconstructs the shortest path from `b` back to `a` using the information stored in the `previous` list. Once `n` (which is the predecessor of the current vertex) becomes `-1`, indicating there is no path to the start vertex, the loop breaks. Therefore, `path_ba` will contain the shortest path from `b` to `a`.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: Output State: `ci` is the length of `path_ba` divided by 2, `path_ba` is a list containing the shortest path from `b` back to `a` and the length of `path_ba` is odd, `c` is the element at index `ci` in `path_ba`, `ops` is a list containing tuples `(c, i)` for each `i` in the range from `0` to `ci` inclusive.
    else :
        ci2 = len(path_ba) // 2
        ci1 = ci2 - 1
        c1 = path_ba[ci1]
        c2 = path_ba[ci2]
        for i in range(1, len(path_ba) - ci1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: Output State: `ci2` is the length of `path_ba` divided by 2 minus 1, `d` is the result of BFS starting from `a`, `previous` is a list representing the path from the start vertex to each vertex, `n` is an input integer, `u2vs` is a list of length `n` where each element is a list representing the set of vertices connected to the vertex indexed by the list's position in the `u2vs` list, `b` is the return value of `func_1(d)`, `path_ba` is a list containing the shortest path from `b` back to `a`, `ops` is a list containing tuples (c1, i) and (c2, i) for every odd index `i` in the range from 1 to the second last index of `path_ba` with a step of 2, `c1` is the element at index `ci1` of `path_ba`, `c2` is the element at index `path_ba[ci2]` of `path_ba`, and the length of `path_ba` is even.
    #State: `path_ba` is the shortest path from `b` back to `a`. If the length of `path_ba` is odd, `ci` is the length of `path_ba` divided by 2, `c` is the element at index `ci` in `path_ba`, and `ops` is a list containing tuples `(c, i)` for each `i` in the range from `0` to `ci` inclusive. If the length of `path_ba` is even, `ci2` is the length of `path_ba` divided by 2 minus 1, `c1` is the element at index `ci1` of `path_ba`, `c2` is the element at index `path_ba[ci2]` of `path_ba`, and `ops` is a list containing tuples `(c1, i)` and `(c2, i)` for every odd index `i` in the range from `1` to the second last index of `path_ba` with a step of 2.
    print(len(ops))
    #This is printed: len(path_ba) // 2 + 1 if len(path_ba) is odd, else len(path_ba) // 2
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: 3 1\n5 3
    return None
    #The program returns None
#Overall this is what the function does:The function processes an input integer `n` and a list `u2vs` representing the edges of a tree. It performs a breadth-first search (BFS) twice to find the shortest path from a specific vertex to another, constructs a list of operations based on the path found, and prints the number of operations and the operations themselves. The function does not return any value.

