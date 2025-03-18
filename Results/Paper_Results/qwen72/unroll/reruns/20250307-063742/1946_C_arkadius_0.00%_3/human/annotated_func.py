#State of the program right berfore the function call: tree is a Tree object with n vertices, s is an integer representing the starting vertex (1 <= s <= n), and x is a non-negative integer representing the minimum size of each remaining connected component after removing k edges.
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
        
    #State: The `stack` is empty, and the `good_components` and `remaining_size` attributes of each vertex in the `tree` have been updated. Specifically, for each vertex `v`, `good_components` represents the number of connected components rooted at `v` that have a size of at least `x`, and `remaining_size` represents the total size of the connected components rooted at `v` that are smaller than `x`.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the `good_components` and `remaining_size` attributes of the vertex `s` in the `tree`. `good_components` is the number of connected components rooted at `s` that have a size of at least `x`, and `remaining_size` is the total size of the connected components rooted at `s` that are smaller than `x`.
#Overall this is what the function does:The function `func_1` accepts a Tree object `tree`, an integer `s` (1 <= s <= n) representing the starting vertex, and a non-negative integer `x`. It updates the `good_components` and `remaining_size` attributes of each vertex in the tree. After the function concludes, `good_components` for each vertex `v` represents the number of connected components rooted at `v` that have a size of at least `x`, and `remaining_size` represents the total size of the connected components rooted at `v` that are smaller than `x`. The function returns the `good_components` and `remaining_size` attributes of the starting vertex `s`.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, v is an integer representing a vertex in the tree, and x is a positive integer such that 1 <= x <= n.
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
        
    #State: `good_components` is the sum of `good_components_subtree` values for all children of vertex `v` plus the number of subtrees where `remaining_size_subtree` is greater than or equal to `x`. `remaining_size` is the sum of `remaining_size_subtree` values for all children of vertex `v` where `remaining_size_subtree` is less than `x`, plus 1.
    return good_components, remaining_size
    #The program returns `good_components` and `remaining_size`. `good_components` is the sum of `good_components_subtree` values for all children of vertex `v` plus the number of subtrees where `remaining_size_subtree` is greater than or equal to `x`. `remaining_size` is the sum of `remaining_size_subtree` values for all children of vertex `v` where `remaining_size_subtree` is less than `x`, plus 1.
#Overall this is what the function does:The function `func_2` accepts a `Tree` object `tree`, an integer `v` representing a vertex in the tree, and a positive integer `x` (1 <= x <= n). It recursively traverses the tree starting from vertex `v` and calculates two values: `good_components` and `remaining_size`. `good_components` is the total number of subtrees rooted at `v` where the size of the subtree is greater than or equal to `x`, plus the sum of `good_components` from all child subtrees. `remaining_size` is the total size of all child subtrees where the size is less than `x`, plus 1 for the current vertex. The function returns these two values.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is a positive integer, k is a non-negative integer such that 1 <= k < n, and x is a positive integer.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True.
    #State: *`tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 1 <= `k` < `n`, `x` is a positive integer, `good_components` is the result of `func_1(tree, 0, x)`, `remaining_size` is the second value returned by `func_1(tree, 0, x)`, and `good_components` is less than or equal to `k`
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True, indicating that the conditions where `good_components` is equal to `k` and `remaining_size` is greater than or equal to `x` are satisfied.
    #State: *`tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 1 <= `k` < `n`, `x` is a positive integer, `good_components` is the result of `func_1(tree, 0, x)`, `remaining_size` is the second value returned by `func_1(tree, 0, x)`, and `good_components` is less than or equal to `k`. Additionally, either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False.
#Overall this is what the function does:The function `func_3` accepts a Tree object `tree` with `n` vertices, a positive integer `n`, a non-negative integer `k` (1 <= k < n), and a positive integer `x`. It returns `True` if the number of good components (`good_components`) is greater than `k`, or if `good_components` is equal to `k` and the remaining size (`remaining_size`) is greater than or equal to `x`. If neither of these conditions is met, it returns `False`.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is an integer such that 1 ≤ n ≤ 10^5, and k is an integer such that 1 ≤ k < n.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `beg` is equal to `end`, and both are the largest integer value for which `func_3(tree, n, k, mid)` returns `True`.
    return beg
    #The program returns the largest integer value for which `func_3(tree, n, k, mid)` returns `True`.
#Overall this is what the function does:The function `func_4` accepts a Tree object `tree`, an integer `n` representing the number of vertices in the tree (1 ≤ n ≤ 10^5), and an integer `k` (1 ≤ k < n). It returns the largest integer value `mid` for which the function `func_3(tree, n, k, mid)` returns `True`. After the function concludes, `mid` is the largest integer value within the range [1, n] that satisfies the condition defined by `func_3`.

#State of the program right berfore the function call: No variables are passed to the function `func_5()`. The function reads input values `n` and `k` from the standard input, where `n` is the number of vertices in the tree and `k` is the number of edges to be removed, with the constraints 1 ≤ k < n ≤ 10^5. It also reads `n-1` pairs of integers `u` and `v` representing the edges of the tree, with the constraints 1 ≤ u, v ≤ n.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: The tree object has `n-1` edges added, forming a complete tree with `n` nodes. The variables `n` and `k` remain unchanged.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: func_4(tree, n, k) (where `func_4` is a function that operates on the tree object with `n` nodes and returns a value based on the parameters `tree`, `n`, and `k`)
#Overall this is what the function does:The function `func_5` reads the number of vertices `n` and the number of edges to be removed `k` from the standard input, along with `n-1` pairs of integers representing the edges of a tree. It constructs a tree with `n` nodes and `n-1` edges, then performs a computation using the `func_4` function on this tree, and prints the result of `func_4(tree, n, k)`. The function does not return any value. After the function concludes, the tree object is fully constructed with the specified edges, and the result of the computation is printed to the standard output.

