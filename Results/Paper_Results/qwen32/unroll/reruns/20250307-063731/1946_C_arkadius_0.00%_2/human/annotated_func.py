#State of the program right berfore the function call: tree is an object representing a tree with vertices and edges, s is an integer representing the starting vertex for the traversal, and x is an integer representing the minimum size of each remaining connected component.
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
        
    #State: the `stack` is empty, and the `tree` object has updated `good_components` and `remaining_size` for each vertex.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the `good_components` and `remaining_size` of the vertex `s` in the `tree` object.
#Overall this is what the function does:The function `func_1` processes a tree structure starting from a specified vertex `s`, updating each vertex's `good_components` and `remaining_size` based on a minimum size `x` for connected components. It returns the `good_components` and `remaining_size` of the starting vertex `s`.

#State of the program right berfore the function call: tree is an instance of a Tree class representing a tree structure with vertices and edges, v is an integer representing a vertex in the tree, and x is a non-negative integer representing the minimum size of each connected component after removing edges.
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
        
    #State: `good_components` is the total number of good components found in the subtree rooted at `v` plus one for each child subtree whose remaining size is at least `x`. `remaining_size` is the sum of the remaining sizes of child subtrees whose sizes are less than `x`, plus the initial `remaining_size` of 1.
    return good_components, remaining_size
    #The program returns `good_components` which is the total number of good components found in the subtree rooted at `v` plus one for each child subtree whose remaining size is at least `x`, and `remaining_size` which is the sum of the remaining sizes of child subtrees whose sizes are less than `x`, plus the initial `remaining_size` of 1.
#Overall this is what the function does:The function `func_2` evaluates a tree structure to determine the number of "good" components in the subtree rooted at a given vertex `v`. A "good" component is defined as a subtree whose size is at least `x`. The function returns a tuple containing the count of such good components and the total size of the remaining components that are smaller than `x`.

#State of the program right berfore the function call: tree is an object representing a tree structure with n vertices, n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n, and x is an integer representing the minimum size of each remaining connected component after removing k edges.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True.
    #State: `tree` is an object representing a tree structure with `n` vertices, `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed such that 1 <= k < n, and `x` is an integer representing the minimum size of each remaining connected component after removing `k` edges. `good_components` and `remaining_size` are the values returned by `func_1(tree, 0, x)`. `good_components` is less than or equal to `k`.
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True.
    #State: `tree` is an object representing a tree structure with `n` vertices, `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed such that 1 <= k < n, and `x` is an integer representing the minimum size of each remaining connected component after removing `k` edges. `good_components` and `remaining_size` are the values returned by `func_1(tree, 0, x)`. `good_components` is less than or equal to `k`, and either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_3` determines if it is possible to remove `k` edges from a tree structure with `n` vertices such that all remaining connected components have at least `x` vertices. It returns `True` if this condition is met; otherwise, it returns `False`.

#State of the program right berfore the function call: tree is an instance of a Tree class representing a tree with n vertices, n is a positive integer representing the number of vertices in the tree, and k is a positive integer such that 1 <= k < n.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `beg` is equal to `end`, and both represent the largest integer `m` such that `func_3(tree, n, k, m)` returns `True`.
    return beg
    #The program returns `beg`, which is equal to `end`, and both represent the largest integer `m` such that `func_3(tree, n, k, m)` returns `True`.
#Overall this is what the function does:The function `func_4` takes a tree represented by an instance of the Tree class with `n` vertices and an integer `k` (where `1 <= k < n`). It returns the largest integer `m` such that when passed to `func_3(tree, n, k, m)`, `func_3` returns `True`.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: `n` and `k` remain unchanged. The `tree` object now contains `n-1` edges, each representing a connection between two nodes as specified by the input pairs `[u, v]`. Each node is identified by an index from `0` to `n-1`.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: result of func_4(tree, n, k) (where result is the value returned by the function func_4 given the tree structure, n nodes, and k)
#Overall this is what the function does:The function reads the number of vertices `n` and the number of edges `k` to be removed from the input. It constructs a tree with `n` vertices and `n-1` edges based on the subsequent input pairs. After rooting the tree, it calculates and prints the number of connected components in the tree after removing `k` edges.

