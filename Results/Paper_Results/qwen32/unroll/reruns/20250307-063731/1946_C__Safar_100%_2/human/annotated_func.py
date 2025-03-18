#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n, and edges is a list of tuples where each tuple (a, b) represents an edge connecting vertices a and b in the tree.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed such that 1 <= k < n, `edges` is a list of tuples where each tuple (a, b) represents an edge connecting vertices a and b in the tree, and `g` is a list of `n + 1` lists where each list at index i contains all the vertices directly connected to vertex i by an edge.`
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: `l` is greater than `r`, and `r` holds the largest value for which `check(mid)` returned `True`.
    print(r)
    #This is printed: r (where r is the largest value for which check(mid) returned True)
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, the number of vertices in a tree; `k`, the number of edges to be removed; and `edges`, a list of tuples representing the edges in the tree. It calculates and prints the largest value `r` for which a certain condition (checked by the `check(mid)` function) holds true after attempting to remove `k` edges.

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
        
    #State: stack=[], visited=set([1, 2, ..., n]), d={}, r=number of subtrees with at least A nodes.
    if (r > k or d[1] >= A and r == k) :
        return True
        #The program returns True
    #State: `stack` is an empty list, `visited` is a set containing integers from 1 to n, `d` is a dictionary, and `r` is the number of subtrees with at least A nodes. Additionally, `r` is less than or equal to `k`, and if `r` equals `k`, then `d[1]` is less than A.
    return False
    #The program returns False
#Overall this is what the function does:The function `check` determines whether there are more than `k` subtrees in a given tree (represented by adjacency list `g`) with at least `A` nodes, or exactly `k` such subtrees where the entire tree itself has at least `A` nodes. It returns `True` if either condition is met, otherwise it returns `False`.

