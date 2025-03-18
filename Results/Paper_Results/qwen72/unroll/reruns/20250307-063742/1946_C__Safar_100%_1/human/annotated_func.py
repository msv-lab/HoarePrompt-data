#State of the program right berfore the function call: n and k are integers such that 1 ≤ k < n ≤ 10^5, and edges is a list of tuples (a, b) where 1 ≤ a, b ≤ n, representing the edges of the tree.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: `g` is a list of lists where each list at index `i` contains the indices of nodes directly connected to node `i` in the tree. The lengths of the lists in `g` will vary depending on the degree of each node in the tree. The variables `n` and `k` remain unchanged.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: `l` is `n // k + 1` and `r` is `n // k - 1`.
    print(r)
    #This is printed: n // k - 1 (where n and k are the values of n and k, and n // k is the integer division of n by k)
#Overall this is what the function does:The function `func_1` accepts three parameters: `n` (the number of nodes in a tree), `k` (a specific node), and `edges` (a list of tuples representing the edges of the tree). It constructs an adjacency list `g` to represent the tree. The function then performs a binary search to determine a specific value, which is printed as `n // k - 1`. The function does not return any value. After the function concludes, the adjacency list `g` is populated with the tree's edges, and the value `n // k - 1` is printed. The original parameters `n` and `k` remain unchanged.

#State of the program right berfore the function call: A is a positive integer, g is a dictionary representing the adjacency list of a tree with n vertices, and k is a non-negative integer such that 1 <= k < n.
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
        
    #State: The loop terminates with `stack` being empty, `visited` containing only the root node (1), `d` containing the count of nodes in each subtree rooted at each node (except for the root node which is not deleted), and `r` being the count of nodes (excluding the root) whose subtree size is greater than or equal to `A`.
    if (r > k or d[1] >= A and r == k) :
        return True
        #The program returns True.
    #State: The loop terminates with `stack` being empty, `visited` containing only the root node (1), `d` containing the count of nodes in each subtree rooted at each node (except for the root node which is not deleted), and `r` being the count of nodes (excluding the root) whose subtree size is greater than or equal to `A`. Additionally, `r` is less than or equal to `k` and either `d[1]` is less than `A` or `r` is not equal to `k`.
    return False
    #The program returns False.
#Overall this is what the function does:The function `check` accepts a positive integer `A` and operates on a tree represented by an adjacency list `g` with `n` vertices. It returns `True` if the number of nodes (excluding the root) whose subtree size is greater than or equal to `A` is greater than `k`, or if the root node's subtree size is greater than or equal to `A` and the number of such nodes is exactly `k`. Otherwise, it returns `False`. After the function concludes, the `stack` is empty, `visited` contains only the root node (1), `d` contains the count of nodes in each subtree rooted at each node (except for the root node which is not deleted), and `r` is the count of nodes (excluding the root) whose subtree size is greater than or equal to `A`.

