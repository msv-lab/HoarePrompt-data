#State of the program right berfore the function call: tree is a Tree object with n vertices, s is an integer representing the starting vertex (1 ≤ s ≤ n), and x is a non-negative integer representing the minimum size of each remaining connected component.
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
        
    #State: The loop has completed, and `stack` is an empty list. For each vertex `v` in the tree, `tree.vertices[v].good_components` is the total number of good components (subtrees) rooted at `v` where the size of the subtree is at least `x`. `tree.vertices[v].remaining_size` is the size of the subtree rooted at `v` after removing all the good components.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the total number of good components (subtrees) rooted at vertex `s` where the size of the subtree is at least `x`, and the size of the subtree rooted at `s` after removing all the good components.
#Overall this is what the function does:The function `func_1` accepts a Tree object `tree`, an integer `s` representing the starting vertex, and a non-negative integer `x` representing the minimum size of each remaining connected component. It processes the tree to count the number of good components (subtrees) rooted at each vertex, where a good component is defined as a subtree with a size of at least `x`. After processing, it returns the total number of good components rooted at vertex `s` and the size of the subtree rooted at `s` after removing all the good components.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, v is an integer representing a vertex in the tree such that 1 <= v <= n, and x is a positive integer.
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
        
    #State: `tree` is a Tree object representing a tree with n vertices, `v` is an integer representing a vertex in the tree such that 1 <= v <= n, `good_components` is the sum of `good_components_subtree` for all children of `v` plus the number of children whose `remaining_size_subtree` is greater than or equal to `x`, `remaining_size` is the sum of `remaining_size_subtree` for all children of `v` whose `remaining_size_subtree` is less than `x`.
    return good_components, remaining_size
    #The program returns `good_components` and `remaining_size`. `good_components` is the sum of `good_components_subtree` for all children of `v` plus the number of children whose `remaining_size_subtree` is greater than or equal to `x`. `remaining_size` is the sum of `remaining_size_subtree` for all children of `v` whose `remaining_size_subtree` is less than `x`.
#Overall this is what the function does:The function `func_2` takes a `Tree` object `tree`, an integer `v` representing a vertex in the tree, and a positive integer `x`. It returns a tuple `(good_components, remaining_size)`. `good_components` represents the total number of "good" components in the subtree rooted at `v`, where a component is considered "good" if its remaining size is greater than or equal to `x`. `remaining_size` represents the total size of the remaining components in the subtree rooted at `v` that are smaller than `x`. The function effectively counts and aggregates these values for the entire subtree rooted at `v`.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is a positive integer, k is a non-negative integer such that 1 <= k < n, and x is a positive integer.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True.
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 1 <= `k` < `n`, `x` is a positive integer, `good_components` is the result of `func_1(tree, 0, x)`, `remaining_size` is the second value returned by `func_1(tree, 0, x)`, and `good_components` is less than or equal to `k`.
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True.
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 1 <= `k` < `n`, `x` is a positive integer, `good_components` is the result of `func_1(tree, 0, x)`, `remaining_size` is the second value returned by `func_1(tree, 0, x)`, and `good_components` is less than or equal to `k`. Additionally, either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False.
#Overall this is what the function does:The function `func_3` takes a Tree object `tree` with `n` vertices, a positive integer `n`, a non-negative integer `k` (where 1 <= k < n), and a positive integer `x`. It returns `True` if the number of good components in the tree, as determined by `func_1(tree, 0, x)`, is greater than `k`, or if the number of good components is exactly `k` and the remaining size of the tree is at least `x`. Otherwise, it returns `False`.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is a positive integer, and k is a non-negative integer such that 1 <= k < n.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 1 <= `k` < `n`, `beg` is equal to `end`.
    return beg
    #The program returns the value of `beg`, which is equal to `end`.
#Overall this is what the function does:The function `func_4` accepts a Tree object `tree`, a positive integer `n` representing the number of vertices in the tree, and a non-negative integer `k` such that `1 <= k < n`. It performs a binary search to find the maximum value `x` such that `func_3(tree, n, k, x)` returns `True`. The function returns this value `x`, which is an integer between 1 and `n` inclusive. The state of `tree`, `n`, and `k` remains unchanged after the function concludes.

#State of the program right berfore the function call: The function `func_5` does not take any parameters. However, it reads input values where `n` and `k` are integers such that 1 ≤ k < n ≤ 10^5, and `u` and `v` are integers for each edge such that 1 ≤ u, v ≤ n.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 10^5, `i` is `n-1`, `k` is an integer such that 1 ≤ k < n, `tree` is an instance of the `Tree` class with `n` nodes, and `n-1` edges have been added to the `tree` based on the user inputs.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: number of nodes at depth k in the tree (where k is an integer such that 1 ≤ k < n)
#Overall this is what the function does:The function `func_5` reads input values for `n` and `k` (integers where 1 ≤ k < n ≤ 10^5) and a series of `n-1` edges represented by pairs of integers `u` and `v` (1 ≤ u, v ≤ n). It constructs a tree with `n` nodes and `n-1` edges, roots the tree at node 0, and prints the number of nodes at depth `k` in the tree. The function does not return any value; it only prints the result.

