#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n <= 10^5, and edges is a list of tuples where each tuple (a, b) represents an edge between vertices a and b, with 1 <= a, b <= n.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: g is a list of n + 1 lists where each list at index i contains the indices of the vertices connected to vertex i by an edge. The lengths of these lists represent the number of edges connected to each vertex. The variables n and k remain unchanged, and the edges list remains the same as in the initial state.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: l is the smallest value such that check(l) would return True, and r is l - 1.
    print(r)
    #This is printed: l - 1 (where l is the smallest value such that check(l) returns True)
#Overall this is what the function does:The function `func_1` accepts three parameters: `n` (the number of vertices in a tree), `k` (the number of edges to be removed), and `edges` (a list of tuples representing the edges). It constructs an adjacency list representation of the tree and performs a binary search to find the smallest value `l` such that a hypothetical `check` function returns `True`. The function prints `l - 1` and does not return any value. The input parameters `n`, `k`, and `edges` remain unchanged after the function execution.

#State of the program right berfore the function call: A is a positive integer, g is a dictionary representing the adjacency list of the tree, and k is a non-negative integer such that 1 <= k < n, where n is the number of vertices in the tree.
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
        
    #State: The loop terminates with `r` being the count of nodes in the tree that have a degree (number of children) greater than or equal to `A`, `visited` and `d` are empty, and `stack` is empty.
    if (r > k or d[1] >= A and r == k) :
        return True
        #The program returns True.
    #State: The loop terminates with `r` being the count of nodes in the tree that have a degree (number of children) greater than or equal to `A`, `visited` and `d` are empty, and `stack` is empty. Additionally, `r` is less than or equal to `k` and either `d[1]` is less than `A` or `r` is not equal to `k`.
    return False
    #The program returns False.
#Overall this is what the function does:The function `check` accepts a positive integer `A` and a global dictionary `g` representing the adjacency list of a tree. It returns `True` if the number of nodes in the tree that have a degree (number of children) greater than or equal to `A` is greater than `k` or if the root node (node 1) has a degree greater than or equal to `A` and the count of such nodes is exactly `k`. Otherwise, it returns `False`. After the function concludes, `r` is the count of nodes with a degree greater than or equal to `A`, and the `visited`, `d`, and `stack` variables are empty.

