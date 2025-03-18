#State of the program right berfore the function call: tree is an object representing a tree structure where each vertex has a list of children and attributes good_components and remaining_size, s is an integer representing the starting vertex for the traversal, and x is a positive integer representing the minimum size of each remaining connected component.
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
        
    #State: The stack is empty, and for each vertex `v` in the tree, `tree.vertices[v].good_components` is the total count of good components in the subtree rooted at `v` (including `v` itself if `tree.vertices[v].remaining_size >= x`), and `tree.vertices[v].remaining_size` is the sum of the remaining sizes of all subtrees rooted at `v` where the remaining size is less than `x`.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the total count of good components in the subtree rooted at vertex `s` (including `s` itself if `tree.vertices[s].remaining_size >= x`) and the sum of the remaining sizes of all subtrees rooted at `s` where the remaining size is less than `x`.
#Overall this is what the function does:The function `func_1` processes a tree structure starting from a specified vertex `s`. It calculates and updates the number of good components and the remaining size for each vertex in the subtree rooted at `s`. A good component is defined as a subtree with a remaining size of at least `x`. The function returns a tuple containing the total count of good components in the subtree rooted at `s` (including `s` itself if its remaining size is at least `x`) and the sum of the remaining sizes of all subtrees rooted at `s` where the remaining size is less than `x`.

#State of the program right berfore the function call: tree is an instance of a Tree class representing a tree structure with vertices and edges, v is an integer representing a vertex in the tree, and x is a non-negative integer representing the minimum size of each remaining connected component after removing edges.
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
        
    #State: `good_components` is the sum of `good_components_subtree` for all children plus the count of children where `remaining_size_subtree` is greater than or equal to `x`, and `remaining_size` is 1 plus the sum of `remaining_size_subtree` for all children where `remaining_size_subtree` is less than `x`.
    return good_components, remaining_size
    #The program returns `good_components`, which is the sum of `good_components_subtree` for all children plus the count of children where `remaining_size_subtree` is greater than or equal to `x`, and `remaining_size`, which is 1 plus the sum of `remaining_size_subtree` for all children where `remaining_size_subtree` is less than `x`.
#Overall this is what the function does:The function `func_2` evaluates a tree structure starting from a given vertex `v`. It calculates two values: `good_components`, which counts the number of connected components in the subtree rooted at `v` that have a size of at least `x`, and `remaining_size`, which represents the size of the remaining connected component after accounting for the larger components. The function returns these two values, providing insight into the distribution and size of connected components within the subtree.

#State of the program right berfore the function call: tree is a representation of a tree structure with n vertices, n is the number of vertices in the tree, k is the number of edges to be removed such that 1 <= k < n, and x is an integer representing the minimum size of each remaining connected component.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True
    #State: `tree` is a representation of a tree structure with `n` vertices, `n` is the number of vertices in the tree, `k` is the number of edges to be removed such that 1 <= k < n, and `x` is an integer representing the minimum size of each remaining connected component. `good_components` is the result of `func_1(tree, 0, x)` indicating the number of good components, and `remaining_size` is the size of the remaining components after the function execution. `good_components` is less than or equal to `k`
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True
    #State: `tree` is a representation of a tree structure with `n` vertices, `n` is the number of vertices in the tree, `k` is the number of edges to be removed such that 1 <= k < n, and `x` is an integer representing the minimum size of each remaining connected component. `good_components` is the result of `func_1(tree, 0, x)` indicating the number of good components, and `remaining_size` is the size of the remaining components after the function execution. `good_components` is less than or equal to `k`. Either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_3` determines if it is possible to remove `k` edges from a tree with `n` vertices such that each of the resulting connected components has at least `x` vertices. It returns `True` if such a removal is possible, otherwise it returns `False`.

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
        
    #State: `tree` is an object representing a tree with `n` vertices, where `n` is greater than 1; `k` is an integer representing the number of edges to be removed such that 1 <= k < n; `beg` is `final_value` and `end` is `final_value`.
    return beg
    #The program returns `beg` which is `final_value`.
#Overall this is what the function does:The function `func_4` accepts a tree represented by an object and two integers, `n` (the number of vertices in the tree) and `k` (the number of edges to be removed such that 1 <= k < n). It returns an integer `beg` which represents the final value determined through a binary search process.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: `n` must be greater than 1, `k` is the second integer input, and `1 <= k < n`; `tree` is an instance of `Tree` initialized with `n` nodes and includes an edge between nodes `u-1` and `v-1` for each of the `n-1` pairs read from the input; `i` is `n-1`.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: result of func_4(tree, n, k) (where tree is an instance of Tree rooted at node 0, n is an integer greater than 1, and k is an integer such that 1 <= k < n)
#Overall this is what the function does:The function reads an integer `n` representing the number of vertices and an integer `k` representing the number of edges to be removed from a tree. It constructs a tree with `n` vertices and `n-1` edges provided as input. After rooting the tree at node 0, it calculates and prints the number of connected components in the tree after removing `k` edges.

