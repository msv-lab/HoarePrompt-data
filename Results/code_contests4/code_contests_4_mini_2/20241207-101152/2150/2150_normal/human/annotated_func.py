#State of the program right berfore the function call: a is an integer n (1 ≤ n ≤ 10^5) representing the number of vertices in a tree, and b is a list of n-1 tuples (u, v) where each tuple represents an edge between vertices u and v (1 ≤ u, v ≤ n).
def func_1(a, b):
    Q = deque()
    Q.append(a)
    seen = {b}
    cnt = 0
    while Q:
        a = Q.popleft()
        
        if a in seen:
            continue
        
        cnt += 1
        
        seen.add(a)
        
        for b in E[a]:
            Q.append(b)
        
    #State of the program after the loop has been executed: `Q` is empty, `cnt` is the total number of unique elements encountered from the initial `Q`, `seen` includes all unique elements processed, and `a` is the last element removed from `Q` before it became empty.
    return cnt
    #The program returns the total number of unique elements encountered from the initial empty queue `Q`
#Overall this is what the function does:The function accepts an integer `a` representing the number of vertices in a tree and a list `b` of tuples representing edges between these vertices. It performs a breadth-first traversal of the tree to count and return the total number of unique vertices encountered. The code does not account for any missing edges or invalid vertex references in the adjacency representation, which may lead to potential inaccuracies in the count if the edges do not represent a connected tree. Additionally, the function assumes that the edges are correctly defined and that every vertex from 1 to `n` is reachable from the starting vertex.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree (1 ≤ n ≤ 100000), and the edges are provided as pairs of integers (u, v) representing connections between vertices (1 ≤ u, v ≤ n), with exactly n - 1 pairs indicating a valid tree structure.
def func_2(node):
    print(node)
    if (node in seen) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`n` is an integer representing the number of vertices in the tree (1 ≤ n ≤ 100000), the variable `node` is printed and its value is not in the `seen` set.
    seen.add(node)
    sz[node] = 1
    for neigh in E[node]:
        print(neigh)
        
        sz[node] += func_2(neigh)
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of vertices in the tree; `node` is printed and its value is not in the `seen` set; `sz[node]` is increased by the cumulative return value of `func_2(neigh)` for all neighbors in `E[node]`; `E[node]` contains all neighbors of `node`; `neigh` is the last neighbor printed.
    return sz[node]
    #The program returns the size 'sz[node]' which has been increased by the cumulative return value of 'func_2(neigh)' for all neighbors in 'E[node]'
#Overall this is what the function does:The function accepts an integer `node` representing a vertex in a tree and returns the size of the subtree rooted at `node`, including the node itself. If the `node` has already been seen (visited), it returns 0. If the node has no neighbors, it will still calculate the size of the subtree by recursively visiting all its neighbors, accumulating their sizes. This function is primarily used to determine the size of connected components in a tree structure.

