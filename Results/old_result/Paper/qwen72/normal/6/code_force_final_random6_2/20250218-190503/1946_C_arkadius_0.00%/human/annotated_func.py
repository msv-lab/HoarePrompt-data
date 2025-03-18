#State of the program right berfore the function call: tree is a Tree object with vertices and edges properly defined, s is a non-negative integer representing a vertex in the tree, and x is a non-negative integer such that 0 <= x <= n, where n is the number of vertices in the tree.
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
        
    #State: The loop has finished executing, and `stack` is an empty list. For each vertex `v` in the tree, `tree.vertices[v].good_components` contains the total number of good components (subtrees where the remaining size of each child is less than `x` or the child itself is a good component) rooted at `v`. The `remaining_size` of each vertex `v` is the sum of the remaining sizes of all its children whose `remaining_size` is less than `x`. The variables `s` and `x` remain unchanged.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the total number of good components rooted at vertex `s` and the remaining size of vertex `s`. The `good_components` value for `s` is the total number of subtrees where the remaining size of each child is less than `x` or the child itself is a good component. The `remaining_size` of `s` is the sum of the remaining sizes of all its children whose `remaining_size` is less than `x`.
#Overall this is what the function does:The function `func_1` accepts a `Tree` object `tree`, a non-negative integer `s` representing a vertex in the tree, and a non-negative integer `x` such that 0 <= x <= n, where n is the number of vertices in the tree. It modifies the `tree` object so that for each vertex `v` in the tree, `tree.vertices[v].good_components` contains the total number of good components (subtrees where the remaining size of each child is less than `x` or the child itself is a good component) rooted at `v`, and `tree.vertices[v].remaining_size` is the sum of the remaining sizes of all its children whose `remaining_size` is less than `x`. The function returns the total number of good components rooted at vertex `s` and the remaining size of vertex `s`. The input parameters `s` and `x` remain unchanged.

#State of the program right berfore the function call: tree is a Tree object representing a tree structure with n vertices, v is an integer representing a vertex in the tree, and x is a non-negative integer representing the minimum size of each remaining connected component after removing edges.
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
        
    #State: `tree` is a Tree object representing a tree structure with n vertices, `v` is an integer representing a vertex in the tree, `x` is a non-negative integer representing the minimum size of each remaining connected component after removing edges, `good_components` is the total number of good components found in all the subtrees of `tree.vertices[v].children` plus the number of subtrees whose remaining size is greater than or equal to `x`, and `remaining_size` is the sum of the sizes of all subtrees whose remaining size is less than `x` plus 1.
    return good_components, remaining_size
    #The program returns the total number of good components found in all the subtrees of `tree.vertices[v].children` plus the number of subtrees whose remaining size is greater than or equal to `x`, and the sum of the sizes of all subtrees whose remaining size is less than `x` plus 1.
#Overall this is what the function does:The function `func_2` accepts a Tree object `tree`, an integer `v` representing a vertex in the tree, and a non-negative integer `x`. It returns a tuple containing two values: the total number of good components found in the subtrees of `v` plus the number of subtrees with a size of at least `x`, and the sum of the sizes of all subtrees with a size less than `x` plus 1. The function does not modify the input `tree` or the parameters `v` and `x`.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is a positive integer, k is a non-negative integer such that 1 <= k < n, and x is a positive integer.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True.
    #State: `good_components` is the result of `func_1(tree, 0, x)` for the first value, and `remaining_size` is the result of `func_1(tree, 0, x)` for the second value. `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 1 <= k < n, and `x` is a positive integer. Additionally, `good_components` is less than or equal to `k`.
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True.
    #State: `good_components` is the result of `func_1(tree, 0, x)` for the first value, and `remaining_size` is the result of `func_1(tree, 0, x)` for the second value. `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 1 <= k < n, and `x` is a positive integer. Additionally, `good_components` is less than or equal to `k`, and either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False.
#Overall this is what the function does:The function `func_3` takes a Tree object `tree` with `n` vertices, a positive integer `n`, a non-negative integer `k` (1 <= k < n), and a positive integer `x`. It returns `True` if the number of good components in the tree, as determined by `func_1(tree, 0, x)`, is greater than `k`, or if the number of good components is exactly `k` and the remaining size of the tree is at least `x`. Otherwise, it returns `False`.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is a positive integer indicating the number of vertices in the tree, and k is a positive integer such that 1 <= k < n, indicating the number of edges to be removed.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer indicating the number of vertices in the tree, `k` is a positive integer such that 1 <= `k` < `n`, `beg` is the largest integer such that `func_3(tree, n, k, beg)` returns `True`, and `end` is equal to `beg`.
    return beg
    #The program returns the largest integer `beg` such that `func_3(tree, n, k, beg)` returns `True`, where `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer indicating the number of vertices in the tree, and `k` is a positive integer such that 1 <= `k` < `n`.
#Overall this is what the function does:The function `func_4` accepts a Tree object `tree`, a positive integer `n` representing the number of vertices in the tree, and a positive integer `k` (1 <= k < n) representing the number of edges to be removed. It returns the largest integer `beg` such that the function `func_3(tree, n, k, beg)` returns `True`. After the function concludes, `tree` remains a Tree object with `n` vertices, and `k` is unchanged. The value of `beg` is the largest integer for which `func_3` returns `True`, and `end` is equal to `beg`.

#State of the program right berfore the function call: No variables are passed to the function `func_5`. The function reads input values directly.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: `n` is the same as in the initial state, `i` is `n - 1`, `k` is an integer read from the input, `tree` is an instance of the `Tree` class with `n` as its argument, and `n - 1` edges have been added to the `tree` instance, each connecting nodes `u - 1` and `v - 1` where `u` and `v` are integers read from the input during each iteration.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: number of nodes at distance k from the root node (where k is the integer read from the input and the root node is node 0)
#Overall this is what the function does:The function `func_5` does not accept any parameters and reads input values directly. It constructs a tree with `n` nodes and `n - 1` edges, where `n` and `k` are integers read from the input. The tree is rooted at node 0, and the function prints the number of nodes that are at a distance `k` from the root node. The final state of the program includes the constructed tree and the printed result, but no return value is specified.

