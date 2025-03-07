#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the tree, k is a positive integer such that 1 <= k < n representing the number of edges to be removed, and edges is a list of tuples (a, b) where 1 <= a, b <= n, representing the edges of the tree.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: `n` is a positive integer, `k` is a positive integer such that 1 <= k < n, `edges` is a list of tuples (a, b) where 1 <= a, b <= n, `g` is a list of `n + 1` lists where each list `g[i]` contains the indices of all vertices connected to vertex `i` by an edge in the tree.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: `n` is a positive integer, `k` is a positive integer such that 1 <= k < n, `edges` is a list of tuples (a, b) where 1 <= a, b <= n, `g` is a list of `n + 1` lists where each list `g[i]` contains the indices of all vertices connected to vertex `i` by an edge in the tree, `c` is 0, `l` is the smallest integer such that `check(l - 1)` is false and `check(l)` is true, `r` is `l - 1`.
    print(r)
    #This is printed: - Since `r` is `l - 1`, and `l` is the smallest integer where `check(l - 1)` is false and `check(l)` is true, the print statement will output the integer `r` which is the largest integer where `check(r)` is false.
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` representing the number of vertices in a tree, a positive integer `k` (1 <= k < n) representing the number of edges to be removed, and a list of tuples `edges` representing the edges of the tree. It constructs an adjacency list `g` representing the tree and then performs a binary search to find the largest integer `r` such that the function `check(r)` returns false. The function prints this integer `r` and does not return any value. The final state of the program includes the adjacency list `g` and the integer `r` which is the largest value for which `check(r)` is false.

