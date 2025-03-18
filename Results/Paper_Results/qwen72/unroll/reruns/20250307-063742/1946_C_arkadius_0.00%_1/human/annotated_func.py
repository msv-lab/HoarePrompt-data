#State of the program right berfore the function call: tree is a Tree object with vertices and edges properly defined, s is an integer representing a vertex in the tree, and x is a non-negative integer.
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
        
    #State: The `stack` is empty, and the `good_components` and `remaining_size` attributes of each vertex in the tree have been updated according to the loop's logic.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the `good_components` and `remaining_size` attributes of the vertex `s` in the tree. `good_components` contains the number of good components associated with vertex `s`, and `remaining_size` contains the remaining size of the subtree rooted at vertex `s` after the loop's logic has been applied.
#Overall this is what the function does:The function `func_1` accepts a Tree object `tree`, an integer `s` representing a vertex in the tree, and a non-negative integer `x`. It updates the `good_components` and `remaining_size` attributes of each vertex in the tree. The `good_components` attribute of a vertex is incremented by the sum of `good_components` of its children and the number of children whose `remaining_size` is greater than or equal to `x`. The `remaining_size` attribute of a vertex is incremented by the `remaining_size` of its children whose `remaining_size` is less than `x`. After the function concludes, it returns the `good_components` and `remaining_size` attributes of the vertex `s`, reflecting the updated state of the subtree rooted at `s`.

#State of the program right berfore the function call: tree is a Tree object with n vertices, v is an integer representing a vertex in the tree, and x is a positive integer such that 1 <= x <= n.
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
        
    #State: `good_components` is the total number of good components found in the subtrees of vertex `v` plus 1 if the remaining size of the subtree is less than `x`. `remaining_size` is the sum of the sizes of the subtrees of vertex `v` that have a size less than `x` plus 1.
    return good_components, remaining_size
    #The program returns the total number of good components found in the subtrees of vertex `v` plus 1 if the remaining size of the subtree is less than `x`, and the sum of the sizes of the subtrees of vertex `v` that have a size less than `x` plus 1.
#Overall this is what the function does:The function `func_2` accepts a Tree object `tree`, an integer `v` representing a vertex in the tree, and a positive integer `x` (1 <= x <= n). It returns a tuple containing two values: the total number of "good components" found in the subtrees of vertex `v`, plus 1 if the remaining size of the subtree rooted at `v` is less than `x`; and the sum of the sizes of the subtrees of vertex `v` that have a size less than `x`, plus 1. The "good components" are counted based on the condition that if a subtree has a size of `x` or more, it is considered a good component.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is an integer such that 1 <= n <= 10^5, k is an integer such that 1 <= k < n, and x is a positive integer.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True.
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is an integer such that 1 <= `n` <= 10^5, `k` is an integer such that 1 <= `k` < `n`, `x` is a positive integer, `good_components` is the first value returned by `func_1(tree, 0, x)`, and `remaining_size` is the second value returned by `func_1(tree, 0, x)`, and `good_components` is less than or equal to `k`
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True.
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is an integer such that 1 <= `n` <= 10^5, `k` is an integer such that 1 <= `k` < `n`, `x` is a positive integer, `good_components` is the first value returned by `func_1(tree, 0, x)`, and `remaining_size` is the second value returned by `func_1(tree, 0, x)`, and `good_components` is less than or equal to `k`. Additionally, either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False.
#Overall this is what the function does:The function `func_3` accepts a Tree object `tree` with `n` vertices, an integer `k` such that 1 <= k < n, and a positive integer `x`. It returns `True` if the number of good components in the tree (as determined by `func_1`) is greater than `k`, or if the number of good components is exactly `k` and the remaining size of the tree is at least `x`. Otherwise, it returns `False`.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is a positive integer representing the number of vertices in the tree, and k is a positive integer such that 1 <= k < n.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `beg` is equal to `end`, and both are the largest integer value `x` such that `func_3(tree, n, k, x)` returns `True`.
    return beg
    #The program returns the largest integer value `x` such that `func_3(tree, n, k, x)` returns `True`.
#Overall this is what the function does:The function `func_4` accepts a Tree object `tree` with `n` vertices and a positive integer `k` such that 1 <= k < n. It returns the largest integer value `x` for which the function `func_3(tree, n, k, x)` returns `True`. After the function concludes, the input `tree` and `n` remain unchanged, and `k` is also unaffected. The final state of the program includes the return value `x` which is the largest integer satisfying the condition.

#State of the program right berfore the function call: No variables are passed to the function `func_5`. The function reads input values directly.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: The loop iterates `n-1` times, reading pairs of integers from the input and adding edges to the `tree` instance. After the loop, `n` and `k` retain their initial values, and the `tree` instance has `n-1` edges added to it.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: [result of func_4(tree, n, k)] (where the result depends on the specific implementation of `func_4`, which could be the height of the tree, the number of nodes at depth `k`, or some other property of the tree)
#Overall this is what the function does:The function `func_5` reads two integers `n` and `k` from the input, followed by `n-1` pairs of integers. It constructs a tree with `n` nodes and adds `n-1` edges to the tree based on the input pairs. The tree is then rooted, and the function calls `func_4` with the tree, `n`, and `k` as arguments, printing the result of `func_4`. The function does not return any value; it only prints the result of `func_4`.

