#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5. The input tree is represented as a list of edges where each edge is a tuple of two integers u, v representing the vertices connected by the edge.**
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
        
    #State of the program after the loop has been executed: `seen` contains all unique elements in E, `cnt` is the total number of unique elements in E, `Q` is an empty list with all elements of E appended in the order they were processed in the loop
    return cnt
    #The program returns the total number of unique elements in list E
#Overall this is what the function does:The function func_1 accepts two integer parameters `a` and `b`, where `a` represents the input tree as a list of edges. It traverses the input tree using a breadth-first search algorithm, counting the total number of unique elements in the input tree. The function then returns this count.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5. The tree is represented by n vertices and n-1 edges connecting these vertices.**
def func_2(node):
    print(node)
    if (node in seen) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *The code prints the value of the variable `node`. `node` is not in the list `seen`
    seen.add(node)
    sz[node] = 1
    for neigh in E[node]:
        print(neigh)
        
        sz[node] += func_2(neigh)
        
    #State of the program after the  for loop has been executed: `node` is not in `seen`, `node` has been added to `seen`, `sz[node]` is equal to the sum of the return values of `func_2` for all neighbors in `E[node]`
    return sz[node]
    #The program returns the sum of the return values of `func_2` for all neighbors in `E[node]` stored in `sz[node]`
#Overall this is what the function does:The function `func_2` accepts an integer `node` representing a vertex in a tree. The tree is defined by `n` vertices and `n-1` edges connecting these vertices. The function checks if the `node` is already in the `seen` set. If it is, the function returns 0. If the `node` has neighbors, the function recursively calculates the sum of return values of `func_2` for all neighbors in `E[node]` and stores it in `sz[node]`. Therefore, the functionality of the function is to either return 0 if the node is already seen or return the sum of return values of all neighbors in the tree.

