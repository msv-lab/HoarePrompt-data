#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed, and edges is a list of tuples where each tuple (a, b) represents an edge connecting vertices a and b.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: Output State: `g` is a list of lists where each element at index i (from 0 to n) contains its adjacent vertices (connected nodes) after adding all the edges specified in `edges`. Each vertex i is connected bidirectionally to its adjacent vertices.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: c is 0, g remains as a list of lists with each element containing its adjacent vertices, l and r are determined by the binary search process within the loop, and check(mid) is the result of the condition evaluated during the loop's execution.
    print(r)
    #This is printed: r (where r is the right bound determined by the binary search process)
#Overall this is what the function does:The function accepts three parameters: `n` (the number of vertices), `k` (the number of edges to be removed), and `edges` (a list of tuples representing the edges). It constructs an adjacency list representation of the tree, then performs a binary search to find the maximum number of connected components that can be achieved by removing up to `k` edges. The function prints the result of this binary search, which indicates the maximum number of connected components possible after removing the edges.

#State of the program right berfore the function call: A is an integer representing the minimum size of each remaining connected component after removing k edges. The function g is an adjacency list representation of the tree, where g[x] is a list of nodes connected to node x.
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
        
    #State: Output State: `stack` is an empty list; `visited` is a set containing {1}; `d` is a dictionary containing the key-value pair {(1): 1}; `r` is 0.
    #
    #Explanation: The loop continues to execute until it encounters the condition `if x == 1: break`, which happens when `x` becomes 1. During each iteration, the loop checks if the current `x` value is already in the `visited` set. If not, it adds `x` to `visited`, updates the dictionary `d` with `d[x] = 1`, and pushes nodes connected to `x` (excluding its parent `p`) onto the `stack`. If `x` is already in `visited`, it checks the value of `d[x]`. If `d[x]` is greater than or equal to `A`, it increments `r`; otherwise, it updates `d[p]` with `d[x]` and then pops `x` from the `stack`, removes `x` from `visited`, and deletes `x` from `d`. Since the loop eventually breaks when `x` is 1, the final states of the variables are as described.
    if (r > k or d[1] >= A and r == k) :
        return True
        #The program returns True
    #State: `stack` is an empty list; `visited` is a set containing {1}; `d` is a dictionary containing the key-value pair {(1): 1}; `r` is 0. Additionally, either `r` is less than or equal to `k`, or `d[1]` is less than `A` and `r` is equal to `k`.
    return False
    #The program returns False
#Overall this is what the function does:The function `check(A)` accepts an integer `A` and an adjacency list `g` representing a tree. It returns `True` if removing `k` edges from the tree results in all remaining connected components having at least `A` nodes. Otherwise, it returns `False`.

