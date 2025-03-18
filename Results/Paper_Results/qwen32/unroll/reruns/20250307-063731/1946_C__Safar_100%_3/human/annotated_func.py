#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n, and edges is a list of tuples where each tuple (a, b) represents an edge between vertices a and b in the tree.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed such that 1 <= k < n, `edges` is a list of tuples where each tuple (a, b) represents an edge between vertices a and b in the tree, and `g` is a list of `n + 1` lists where each list at index i contains the neighbors of vertex i.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: l is r + 1, r is the maximum value of mid for which check(mid) is True.
    print(r)
    #This is printed: r (where r is the maximum value of mid for which check(mid) is True)
#Overall this is what the function does:The function `func_1` determines the maximum number of connected components that can be formed by removing `k` edges from a tree with `n` vertices. It accepts three parameters: `n`, the number of vertices; `k`, the number of edges to be removed; and `edges`, a list of tuples representing the edges between vertices. The function prints and returns the maximum number of connected components achievable under these conditions.

#State of the program right berfore the function call: A is a positive integer, g is an adjacency list representing the tree with n vertices, and k is a non-negative integer such that 1 <= k < n.
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
        
    #State: stack is [], visited is set(), d is {}, r is the number of nodes whose subtree size is at least A.
    if (r > k or d[1] >= A and r == k) :
        return True
        #The program returns True
    #State: stack is [], visited is set(), d is {}, r is the number of nodes whose subtree size is at least A, and either r is less than or equal to k, or (d[1] is less than A and r is equal to k)
    return False
    #The program returns False
#Overall this is what the function does:The function `check` determines whether a tree, represented by an adjacency list `g`, has at least `k` nodes whose subtree size is at least `A`. It returns `True` if this condition is met or if the entire tree's size is at least `A` and exactly `k` nodes meet the subtree size condition; otherwise, it returns `False`.

