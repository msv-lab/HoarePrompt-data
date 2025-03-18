#State of the program right berfore the function call: tree is a Tree object with vertices and edges defined, s is a non-negative integer representing a vertex in the tree, and x is a non-negative integer such that 0 <= x <= n, where n is the number of vertices in the tree.
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
        
    #State: The `stack` is empty, and the `good_components` and `remaining_size` attributes of each vertex in the tree have been updated according to the loop logic.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the `good_components` and `remaining_size` attributes of the vertex `s` in the tree. `good_components` is the number of good components associated with vertex `s`, and `remaining_size` is the size of the remaining components after some operations have been performed. Both values have been updated according to the loop logic.
#Overall this is what the function does:The function `func_1` accepts a Tree object `tree`, a non-negative integer `s` representing a vertex in the tree, and a non-negative integer `x` such that 0 <= x <= n, where n is the number of vertices in the tree. It updates the `good_components` and `remaining_size` attributes of each vertex in the tree. Specifically, for each vertex `v` in the tree, `good_components` is incremented by the `good_components` of its children and by 1 for each child whose `remaining_size` is greater than or equal to `x`. The `remaining_size` of each vertex `v` is incremented by the `remaining_size` of its children whose `remaining_size` is less than `x`. The function returns the `good_components` and `remaining_size` attributes of the vertex `s` after these updates.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, v is an integer representing a vertex in the tree, and x is a positive integer representing the minimum size of each remaining connected component after removing edges.
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
        
    #State: `good_components` is the total number of good components found in the subtrees of vertex `v` and any additional good components formed by the remaining vertices that meet the size requirement `x`. `remaining_size` is the size of the remaining connected component that includes vertex `v` after removing edges from its children.
    return good_components, remaining_size
    #The program returns the total number of good components found in the subtrees of vertex `v` and any additional good components formed by the remaining vertices that meet the size requirement `x`, along with the size of the remaining connected component that includes vertex `v` after removing edges from its children.
#Overall this is what the function does:The function `func_2` accepts a Tree object `tree`, an integer `v` representing a vertex in the tree, and a positive integer `x` representing the minimum size of each remaining connected component. It returns a tuple containing two values: the total number of good components found in the subtrees of vertex `v` and any additional good components formed by the remaining vertices that meet the size requirement `x`, and the size of the remaining connected component that includes vertex `v` after removing edges from its children. A "good component" is a connected component of the tree that has at least `x` vertices.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is a positive integer, k is a non-negative integer such that 0 <= k < n, and x is a positive integer.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True.
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 0 <= `k` < `n`, `x` is a positive integer, `good_components` is the result of `func_1(tree, 0, x)` for the first returned value, and `remaining_size` is the result of `func_1(tree, 0, x)` for the second returned value. Additionally, `good_components` is less than or equal to `k`.
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns `True`.
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 0 <= `k` < `n`, `x` is a positive integer, `good_components` is the result of `func_1(tree, 0, x)` for the first returned value, and `remaining_size` is the result of `func_1(tree, 0, x)` for the second returned value. Additionally, `good_components` is less than or equal to `k`, and either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False.
#Overall this is what the function does:The function `func_3` takes a Tree object `tree` with `n` vertices, a positive integer `n`, a non-negative integer `k` such that `0 <= k < n`, and a positive integer `x`. It returns `True` if the number of good components in the tree is greater than `k` or if the number of good components is exactly `k` and the remaining size of the tree is at least `x`. Otherwise, it returns `False`. The function does not modify the input `tree` or any of the input parameters.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is an integer such that 1 <= n <= 10^5, and k is an integer such that 1 <= k < n.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `beg` equals `end`.
    return beg
    #The program returns the value of `beg`, which is equal to the value of `end`.
#Overall this is what the function does:The function `func_4` accepts a Tree object `tree`, an integer `n` representing the number of vertices in the tree (1 <= n <= 10^5), and an integer `k` (1 <= k < n). It performs a binary search to find the maximum value `x` such that a certain condition (determined by `func_3`) is satisfied for `x`. The function returns this value `x`, which is the point where `beg` and `end` converge.

#State of the program right berfore the function call: No variables are passed to the function `func_5`. The function reads input values `n` and `k` from the standard input, where `n` is the number of vertices in the tree and `k` is the number of edges to be removed, such that 1 <= k < n <= 10^5. It also reads `n-1` pairs of integers `u` and `v` representing the edges of the tree, where 1 <= u, v <= n.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: The loop has added `n-1` edges to the `tree` object, connecting vertices as specified by the input pairs `[u, v]`. The values of `n` and `k` remain unchanged.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: func_4(tree, n, k) (where `func_4` is a function that processes the tree with `n` vertices and `k` as parameters and returns a value)
#Overall this is what the function does:The function `func_5` reads the number of vertices `n` and the number of edges to be removed `k` from the standard input, along with `n-1` pairs of integers representing the edges of a tree. It constructs a tree with these vertices and edges, roots the tree, and then processes the tree by calling `func_4` with the tree, `n`, and `k` as parameters. The function prints the result of `func_4` and does not return any value. The state of the program after the function concludes is that the tree has been constructed and processed, and the result of this processing has been printed to the standard output.

