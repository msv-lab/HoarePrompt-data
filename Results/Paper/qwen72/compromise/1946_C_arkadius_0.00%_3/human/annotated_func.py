#State of the program right berfore the function call: tree is a Tree object with n vertices, s is an integer representing the starting vertex (1 ≤ s ≤ n), and x is a non-negative integer.
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
        
    #State: After the loop executes all iterations, `stack` is empty. For each vertex `v` in the tree, `tree.vertices[v].good_components` is the sum of `good_components` of all its children plus the number of children whose `remaining_size` is greater than or equal to `x`. Additionally, `tree.vertices[v].remaining_size` is the sum of the `remaining_size` of all its children whose `remaining_size` is less than `x`. The initial variables `tree`, `s`, and `x` remain unchanged.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the `good_components` and `remaining_size` of the vertex `s` in the tree. `good_components` is the sum of `good_components` of all its children plus the number of children whose `remaining_size` is greater than or equal to `x`. `remaining_size` is the sum of the `remaining_size` of all its children whose `remaining_size` is less than `x`.
#Overall this is what the function does:The function `func_1` accepts a Tree object `tree`, an integer `s` representing a starting vertex (1 ≤ s ≤ n), and a non-negative integer `x`. It modifies the `good_components` and `remaining_size` attributes of each vertex in the tree. After the function concludes, for each vertex `v` in the tree, `tree.vertices[v].good_components` is the sum of the `good_components` of all its children plus the number of children whose `remaining_size` is greater than or equal to `x`. Similarly, `tree.vertices[v].remaining_size` is the sum of the `remaining_size` of all its children whose `remaining_size` is less than `x`. The function returns the `good_components` and `remaining_size` of the starting vertex `s`.

#State of the program right berfore the function call: tree is an instance of the Tree class with at least v as a vertex, v is a non-negative integer representing a vertex in the tree, and x is a positive integer.
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
        
    #State: `tree` is an instance of the Tree class with at least `v` as a vertex, `v` is a non-negative integer representing a vertex in the tree, `x` is a positive integer, `good_components` is the sum of all `good_components_subtree` values returned by `func_2` for each child of `v` plus the number of children whose `remaining_size_subtree` is greater than or equal to `x`, `remaining_size` is 1 plus the sum of all `remaining_size_subtree` values for children whose `remaining_size_subtree` is less than `x`.
    return good_components, remaining_size
    #The program returns `good_components` and `remaining_size`. `good_components` is the sum of all `good_components_subtree` values for each child of vertex `v` plus the number of children whose `remaining_size_subtree` is greater than or equal to `x`. `remaining_size` is 1 plus the sum of all `remaining_size_subtree` values for children whose `remaining_size_subtree` is less than `x`.
#Overall this is what the function does:The function `func_2` accepts a `Tree` instance `tree`, a non-negative integer `v` representing a vertex in the tree, and a positive integer `x`. It returns two values: `good_components` and `remaining_size`. `good_components` is the total count of "good" components in the subtree rooted at `v`, where a "good" component is defined as either a child subtree that has a `remaining_size_subtree` greater than or equal to `x` or the sum of all such components in the child subtrees. `remaining_size` is the total size of the remaining components in the subtree rooted at `v` that have a `remaining_size_subtree` less than `x`, plus 1.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n is a positive integer, k is a non-negative integer such that 1 <= k < n, and x is a positive integer.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True.
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 1 <= `k` < `n`, `x` is a positive integer, `good_components` is the result of `func_1(tree, 0, x)`, and `remaining_size` is the second value returned by `func_1(tree, 0, x)`. Additionally, `good_components` is less than or equal to `k`.
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True.
    #State: `tree` is a Tree object representing a tree with `n` vertices, `n` is a positive integer, `k` is a non-negative integer such that 1 <= `k` < `n`, `x` is a positive integer, `good_components` is the result of `func_1(tree, 0, x)`, and `remaining_size` is the second value returned by `func_1(tree, 0, x)`. Additionally, `good_components` is less than or equal to `k`, and either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False.
#Overall this is what the function does:The function `func_3` accepts a Tree object `tree` with `n` vertices, a positive integer `n`, a non-negative integer `k` such that 1 <= `k` < `n`, and a positive integer `x`. It returns `True` if the number of good components in the tree (determined by `func_1(tree, 0, x)`) is greater than `k`, or if the number of good components is exactly `k` and the remaining size of the tree is at least `x`. Otherwise, it returns `False`.

#State of the program right berfore the function call: tree is an instance of the Tree class representing a tree with n vertices, n is a positive integer representing the number of vertices in the tree, and k is a positive integer such that 1 <= k < n, representing the number of edges to be removed.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `tree` is an instance of the Tree class representing a tree with `n` vertices, `n` is a positive integer representing the number of vertices in the tree, `k` is a positive integer such that 1 <= `k` < `n`, `beg` is equal to `end`, and `mid` is equal to `beg`.
    return beg
    #The program returns the value of `beg`, which is equal to `end` and `mid`.
#Overall this is what the function does:The function `func_4` accepts a tree with `n` vertices, the number of vertices `n`, and a number of edges to be removed `k`. It performs a binary search to find the maximum value `beg` such that a certain condition (determined by `func_3`) is satisfied for the given tree, `n`, `k`, and `mid`. The function returns this value `beg`, which is equal to `end` and `mid` after the search concludes. The tree remains unchanged.

#State of the program right berfore the function call: No variables are passed to the function `func_5()`. The function reads input values directly, where `n` and `k` are integers such that 1 ≤ k < n ≤ 10^5, and the subsequent `n-1` lines contain pairs of integers `u` and `v` (1 ≤ u, v ≤ n) representing the edges of the tree.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: `n` and `k` are integers such that 1 ≤ k < n ≤ 10^5, `tree` is an instance of the `Tree` class initialized with `n` nodes, `i` is `n-1`, `n` must be greater than or equal to 1, and `n-1` edges have been added to the `tree` connecting the nodes as specified by the pairs of integers `u` and `v` provided by the user.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: [result of func_4(tree, n, k)] (where the result depends on the specific implementation of `func_4`, which operates on the tree with `n` nodes and an integer `k` such that \(1 \leq k < n\))
#Overall this is what the function does:The function `func_5` reads input values for integers `n` and `k` where \(1 \leq k < n \leq 10^5\), and `n-1` pairs of integers `u` and `v` representing the edges of a tree. It constructs a tree with `n` nodes and adds `n-1` edges to it. The tree is then rooted, and the function calls `func_4` with the tree, `n`, and `k` as arguments, printing the result of `func_4`. After the function concludes, the tree is fully constructed and rooted, and the result of `func_4` is printed.

