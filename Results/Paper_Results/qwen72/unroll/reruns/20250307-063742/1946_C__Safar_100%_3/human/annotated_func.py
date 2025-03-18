#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the tree, k is a positive integer such that 1 <= k < n representing the number of edges to be removed, and edges is a list of tuples (a, b) where 1 <= a, b <= n and a != b, representing the edges of the tree.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: `g` is a list of lists where each list at index `a` contains the indices of the vertices connected to vertex `a` by an edge, and each list at index `b` contains the indices of the vertices connected to vertex `b` by an edge. The other variables `n`, `k`, and `edges` remain unchanged.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: `c` is 0, `l` is `n // k + 1`, `r` is `n // k`.
    print(r)
    #This is printed: n // k (where n // k is the integer division of n by k)
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` representing the number of vertices in a tree, a positive integer `k` such that 1 <= k < n representing the number of edges to be removed, and a list of tuples `edges` where each tuple (a, b) represents an edge between vertices a and b in the tree. It constructs an adjacency list `g` representing the tree. The function then performs a binary search to determine the maximum value `r` that satisfies a certain condition (checked by the `check` function, which is not provided in the code). Finally, the function prints the value of `r`, which is the integer division of `n` by `k` (i.e., `n // k`). The function does not return any value. After the function concludes, the adjacency list `g` is populated with the connections between vertices, and the variables `n`, `k`, and `edges` remain unchanged.

#State of the program right berfore the function call: A is a positive integer, and g is a dictionary representing the adjacency list of a tree with n vertices, where each key is a vertex and each value is a list of adjacent vertices.
def check(A):
    stack = [(1, 1)]
    visited = set()
    d = {(1): 1}
    r = 0
    while True:
        x, p = stack[-1]
        
        if x not in visited:
            visited.add(x)
            d[x] = 1
            for node in g[x]:
                if node != p:
                    stack.append((node, x))
        else:
            if x == 1:
                break
            if d[x] >= A:
                r += 1
            else:
                d[p] += d[x]
            stack.pop()
            visited.remove(x)
            del d[x]
        
    #State: `stack` is an empty list, `visited` is a set containing all vertices of the tree, `d` is a dictionary where each key is a vertex and the value is the number of vertices in the subtree rooted at that vertex (excluding the parent), `r` is the number of vertices in the tree that have at least `A` vertices in their subtree.
    if (r > k or d[1] >= A and r == k) :
        return True
        #The program returns True.
    #State: `stack` is an empty list, `visited` is a set containing all vertices of the tree, `d` is a dictionary where each key is a vertex and the value is the number of vertices in the subtree rooted at that vertex (excluding the parent), `r` is the number of vertices in the tree that have at least `A` vertices in their subtree, and either `r` is less than or equal to `k` or (`d[1]` is less than `A` and `r` is not equal to `k`).
    return False
    #The program returns False.
#Overall this is what the function does:The function `check` accepts a positive integer `A` and a dictionary `g` representing the adjacency list of a tree. It returns `True` if the number of vertices in the tree that have at least `A` vertices in their subtree is greater than `k`, or if the root vertex (1) has at least `A` vertices in its subtree and the number of such vertices is exactly `k`. Otherwise, it returns `False`. After the function concludes, the `stack` is an empty list, `visited` is a set containing all vertices of the tree, `d` is a dictionary where each key is a vertex and the value is the number of vertices in the subtree rooted at that vertex (excluding the parent), and `r` is the number of vertices in the tree that have at least `A` vertices in their subtree.

