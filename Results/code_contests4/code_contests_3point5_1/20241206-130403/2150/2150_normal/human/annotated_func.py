#State of the program right berfore the function call: **
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
        
    #State of the program after the loop has been executed: `Q` is an empty deque, `seen` contains all unique elements seen throughout the loop iterations, `cnt` is the total number of unique elements seen, `a` is the last element removed from `Q`
    return cnt
    #The program returns the total number of unique elements seen throughout the loop iterations
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`. It iterates through a loop and keeps track of unique elements seen during the iterations. The function returns the total number of unique elements seen throughout the loop iterations. The code may not handle the case where the initial value of `b` is not added to the `seen` set, potentially leading to an incorrect count of unique elements. This missing functionality should be considered when using the function.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5. The input tree is represented as a list of edges where each edge is a tuple of two integers u, v (1 ≤ u, v ≤ n) representing vertices connected by the edge. The edges form a tree.**
def func_2(node):
    print(node)
    if (node in seen) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *n is an integer such that 1 ≤ n ≤ 10^5. The input tree is represented as a list of edges where each edge is a tuple of two integers u, v (1 ≤ u, v ≤ n) representing vertices connected by the edge. The edges form a tree. The node is not in seen.
    seen.add(node)
    sz[node] = 1
    for neigh in E[node]:
        print(neigh)
        
        sz[node] += func_2(neigh)
        
    #State of the program after the  for loop has been executed: `sz[node]` is updated based on the return values of `func_2(neigh)` for all neighbors in the tree rooted at `node`.
    return sz[node]
    #The program returns the updated size of the tree rooted at 'node', which is calculated based on the return values of 'func_2(neigh)' for all neighbors in the tree.
#Overall this is what the function does:The function `func_2` accepts an integer `node`, representing a vertex in a tree. The input tree is represented as a list of edges. If the `node` is already in the set `seen`, the function returns 0. Otherwise, it adds the `node` to the set `seen`, initializes the size of the subtree rooted at `node`, and recursively calculates the size by calling `func_2` on all neighbors of `node`. The function then returns the updated size of the subtree rooted at the input `node`.

