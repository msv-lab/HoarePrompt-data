#State of the program right berfore the function call: tree is an object representing a tree structure with vertices attribute, s is an integer representing the starting vertex, and x is a non-negative integer representing the minimum size of each remaining connected component.
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
        
    #State: stack is `[]`, and each vertex in `tree` has its `good_components` and `remaining_size` updated based on its children.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the `good_components` and `remaining_size` of the vertex `s` in the `tree`.
#Overall this is what the function does:The function `func_1` processes a tree structure to calculate and return the number of "good components" and the remaining size of the component starting from a specified vertex `s`. A "good component" is defined as a connected sub-component with a size of at least `x`. The function updates each vertex in the tree with the count of good components and the remaining size of its sub-components.

#State of the program right berfore the function call: tree is an object representing a tree structure with vertices that have children, v is an integer representing a vertex in the tree, and x is a non-negative integer representing the minimum size of a connected component.
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
        
    #State: `good_components` is the sum of all `good_components_subtree` values plus the number of times `remaining_size_subtree` was greater than or equal to `x`, and `remaining_size` is 1 if the last `remaining_size_subtree` was greater than or equal to `x`, otherwise it is the sum of all `remaining_size_subtree` values that were less than `x` up to the last child processed.
    return good_components, remaining_size
    #The program returns `good_components` which is the sum of all `good_components_subtree` values plus the number of times `remaining_size_subtree` was greater than or equal to `x`, and `remaining_size` which is 1 if the last `remaining_size_subtree` was greater than or equal to `x`, otherwise it is the sum of all `remaining_size_subtree` values that were less than `x` up to the last child processed.
#Overall this is what the function does:The function `func_2` evaluates a tree structure to count the number of connected components of at least size `x` starting from a given vertex `v`. It returns two values: `good_components`, which is the total count of such components, and `remaining_size`, which indicates the size of the last component that did not meet the minimum size requirement or is 1 if the last component did meet the requirement.

#State of the program right berfore the function call: tree is an object representing a tree with n vertices, n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n, and x is an integer representing the minimum size of each remaining connected component after removing k edges.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True
    #State: `tree` is an object representing a tree with n vertices, `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed such that 1 <= k < n, and `x` is an integer representing the minimum size of each remaining connected component after removing k edges; `good_components` and `remaining_size` are the values returned by `func_1(tree, 0, x)`. `good_components` is less than or equal to `k`.
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True
    #State: `tree` is an object representing a tree with `n` vertices, `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed such that 1 <= k < n, and `x` is an integer representing the minimum size of each remaining connected component after removing `k` edges; `good_components` and `remaining_size` are the values returned by `func_1(tree, 0, x)`. `good_components` is less than or equal to `k`, and either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_3` determines if it is possible to remove `k` edges from a tree with `n` vertices such that each remaining connected component has at least `x` vertices. It returns True if this is possible, otherwise it returns False.

#State of the program right berfore the function call: tree is an object representing a tree structure with n vertices, n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n <= 10^5.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `beg` equals `end`, and both represent the largest value for which `func_3(tree, n, k, mid)` returns `True`.
    return beg
    #The program returns `beg`, which is the largest value for which `func_3(tree, n, k, mid)` returns `True`.
#Overall this is what the function does:The function accepts a tree structure with `n` vertices and an integer `k` representing the number of edges to be removed. It returns the largest value for which a certain condition (checked by `func_3`) is satisfied.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: `n` remains unchanged; `k` remains unchanged; `tree` contains `n-1` edges added from the input pairs.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: func_4(tree, n, k) (where `tree` is the processed tree with root node 0, `n` is the unchanged value representing the number of nodes, and `k` is the unchanged value representing some parameter used by `func_4`)
#Overall this is what the function does:The function reads an integer `n` representing the number of vertices and an integer `k` representing the number of edges to be removed from a tree. It constructs a tree with `n` vertices and `n-1` edges based on the input. The tree is then rooted at node 0. The function computes and prints a value or structure derived from the tree after potentially removing `k` edges, as determined by the function `func_4`.

