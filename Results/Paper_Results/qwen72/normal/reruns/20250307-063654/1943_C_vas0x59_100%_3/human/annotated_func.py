#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the largest integer in the list `l`.
#Overall this is what the function does:The function `func_1` accepts a non-empty list of integers `l` and returns the index of the largest integer in the list. After the function concludes, the list `l` remains unchanged, and the user receives the index of the largest integer in the list.

#State of the program right berfore the function call: The function does not take any parameters, but it reads input values from the standard input. The first input is an integer n (1 ≤ n ≤ 2 · 10^3) representing the number of vertices in the tree. The subsequent n - 1 inputs are pairs of integers (u, v) (1 ≤ u, v ≤ n, u ≠ v) representing the edges of the tree.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: `n` is an integer between 1 and 2000, `u2vs` is a list of `n` lists, where each list contains the indices (decreased by 1) of the nodes connected to the corresponding node.
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
        
    #State: The loop will continue to append the previous node in the shortest path to `path_ba` until it reaches the starting node (node 0) or a node with no previous node (indicated by -1). The final state of `path_ba` will be a list containing the node indices in the shortest path from node `b` to node 0, in reverse order. The value of `n` will be -1, indicating that the loop has reached the end of the path. The other variables (`u2vs`, `d`, `a`, `b`, and `previous`) will remain unchanged.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: `ops` contains tuples from `(c, 0)` to `(c, ci)`, and `i` is `ci + 1`.
    else :
        ci2 = len(path_ba) // 2
        ci1 = ci2 - 1
        c1 = path_ba[ci1]
        c2 = path_ba[ci2]
        for i in range(1, len(path_ba) - ci1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: `path_ba` is a list containing the node indices in the shortest path from node `b` to node 0, in reverse order. `i` is the last odd index in the range from 1 to `len(path_ba) - ci1 - 1`, inclusive. `ops` has a total of `len(path_ba) - ci1 - 1` tuples appended to it, with each pair of tuples being `(c1, i)` and `(c2, i)`, where `i` is an odd number starting from 1 and incrementing by 2.
    #State: *`path_ba` is a list containing the node indices in the shortest path from node `b` to node 0, in reverse order. The value of `n` is -1. The other variables (`u2vs`, `d`, `a`, `b`, and `previous`) remain unchanged. If the length of `path_ba` is odd, `ops` contains tuples from `(c, 0)` to `(c, ci)`, and `i` is `ci + 1`. If the length of `path_ba` is even, `i` is the last odd index in the range from 1 to `len(path_ba) - ci1 - 1`, inclusive, and `ops` has a total of `len(path_ba) - ci1 - 1` tuples appended to it, with each pair of tuples being `(c1, i)` and `(c2, i)`, where `i` is an odd number starting from 1 and incrementing by 2.
    print(len(ops))
    #This is printed: - If the length of `path_ba` is odd, the output will be `ci + 1`.
    #- If the length of `path_ba` is even, the output will be `len(path_ba) - ci1 - 1`.
    #
    #Therefore, the final output is:
    #Output:
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: c + 1 0
    #         c + 1 1
    #         c + 1 2
    #         ...
    #         c + 1 ci (if the length of `path_ba` is odd)
    #         or
    #         c1 + 1 1
    #         c2 + 1 1
    #         c1 + 1 3
    #         c2 + 1 3
    #         ...
    #         c1 + 1 i
    #         c2 + 1 i (if the length of `path_ba` is even)
    return None
    #The program returns `None`.
#Overall this is what the function does:The function `func_2` reads the number of vertices `n` and the edges of a tree from the standard input. It constructs an adjacency list `u2vs` representing the tree. It then performs a breadth-first search (BFS) starting from node 0 to find a node `a`, and another BFS starting from node `a` to find a node `b`. The function constructs a list `path_ba` representing the shortest path from node `b` to node 0 in reverse order. Depending on the length of `path_ba`, it generates a list of operations `ops` where each operation is a tuple. If the length of `path_ba` is odd, `ops` contains tuples from `(c, 0)` to `(c, ci)`, where `c` is the middle node in `path_ba`. If the length is even, `ops` contains alternating tuples `(c1, i)` and `(c2, i)`, where `c1` and `c2` are the two middle nodes in `path_ba`, and `i` is an odd number starting from 1. The function prints the number of operations in `ops` and then prints each operation in the format `node_index + 1 index`. Finally, the function returns `None`.

