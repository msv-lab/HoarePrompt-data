#State of the program right berfore the function call: tree is an instance of a Tree class representing a tree structure with vertices, s is an integer representing the starting vertex for the traversal, and x is an integer representing the minimum size of each remaining connected component after removing edges.
def func_1(tree, s, x):
    stack = [(s, False)]
    while stack:
        v, postorder = stack.pop()
        
        if not postorder:
            stack.append((v, True))
            for u in tree.vertices[v].children:
                stack.append((u, False))
        
        if postorder:
            for u in tree.vertices[v].children:
                tree.vertices[v].good_components += tree.vertices[u].good_components
                if tree.vertices[u].remaining_size >= x:
                    tree.vertices[v].good_components += 1
                else:
                    tree.vertices[v].remaining_size += tree.vertices[u].remaining_size
        
    #State: `stack` is an empty list, and `tree` has its `good_components` and `remaining_size` fields updated for all vertices.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the `good_components` and `remaining_size` of the vertex `s` in the `tree`.
#Overall this is what the function does:The function processes a tree structure starting from a specified vertex, updating the count of "good components" and the remaining size of each vertex based on a minimum size threshold. It returns the count of good components and the remaining size of the starting vertex.

#State of the program right berfore the function call: tree is an object representing a tree structure where each vertex has a list of children, v is an integer representing the current vertex, and x is an integer representing the minimum size of each connected component.
def func_2(tree, v, x):
    good_components = 0
    remaining_size = 1
    for u in tree.vertices[v].children:
        good_components_subtree, remaining_size_subtree = func_2(tree, u, x)
        
        good_components += good_components_subtree
        
        if remaining_size_subtree >= x:
            good_components += 1
        else:
            remaining_size += remaining_size_subtree
        
    #State: `tree` is an object representing a tree structure, `v` is an integer representing the current vertex, `x` is an integer representing the minimum size of each connected component, `good_components` is the total count of good components accumulated from all iterations, and `remaining_size` is the final remaining size after all iterations.
    return good_components, remaining_size
    #The program returns `good_components`, which is the total count of good components accumulated from all iterations, and `remaining_size`, which is the final remaining size after all iterations.
#Overall this is what the function does:The function `func_2` calculates and returns the total count of good components and the remaining size of the current subtree in a tree structure, given a vertex `v` and a minimum size `x` for each connected component. A good component is defined as a subtree with at least `x` vertices.

#State of the program right berfore the function call: tree is an object representing a tree with n vertices, n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n, and x is an integer representing the minimum size of each remaining connected component.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True
    #State: `tree` is an object representing a tree with `n` vertices, `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed such that 1 <= k < n, and `x` is an integer representing the minimum size of each remaining connected component. `good_components` and `remaining_size` are returned values from the function `func_1(tree, 0, x)`. `good_components` is less than or equal to `k`.
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True.
    #State: `tree` is an object representing a tree with `n` vertices, `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed such that 1 <= k < n, and `x` is an integer representing the minimum size of each remaining connected component. `good_components` and `remaining_size` are returned values from the function `func_1(tree, 0, x)`. `good_components` is less than or equal to `k`, and either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_3` determines whether a tree can be split by removing `k` edges into connected components, each having at least `x` vertices. It returns `True` if such a split is possible; otherwise, it returns `False`.

#State of the program right berfore the function call: tree is an object representing a tree with n vertices, n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `beg` is equal to `end`, and both are the largest integer for which `func_3(tree, n, k, mid)` returns True.
    return beg
    #The program returns the largest integer for which `func_3(tree, n, k, mid)` returns True, and this integer is equal to both `beg` and `end`.
#Overall this is what the function does:The function `func_4` determines the largest integer `mid` for which `func_3(tree, n, k, mid)` returns True, given a tree with `n` vertices and an integer `k` representing the number of edges to be removed. The function returns this integer.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: `n` is at least 2, `k` is the number of edges to be removed such that `1 <= k < n`, `tree` is a Tree object with `n` vertices and includes `n-1` additional edges between vertices `u - 1` and `v - 1`, where `u` and `v` are integers read from the input for each iteration, `i` is `n-1`.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: result of `func_4(tree, n, k)` (where `tree` is a Tree object with `n` vertices and `n-1` edges rooted at vertex `0`, `n` is at least 2, and `k` is the number of edges to be removed such that `1 <= k < n`)
#Overall this is what the function does:The function reads an integer `n` representing the number of vertices and an integer `k` representing the number of edges to be removed from a tree. It constructs a tree with `n` vertices and `n-1` edges based on the input, roots the tree at vertex 0, and then calculates and prints the number of connected components in the tree after removing `k` edges.

