#State of the program right berfore the function call: tree is an object representing a tree structure with vertices, s is an integer representing the starting vertex for the traversal, and x is an integer representing the minimum size of each remaining connected component after edge removals.
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
        
    #State: The `stack` is empty, and each vertex `v` in the tree has its `good_components` and `remaining_size` updated based on its children.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the `good_components` and `remaining_size` of the vertex `s` in the tree.
#Overall this is what the function does:The function processes a tree structure starting from a specified vertex `s`, updating each vertex's `good_components` and `remaining_size` based on its children and a minimum size threshold `x`. It returns the `good_components` and `remaining_size` of the starting vertex `s`.

#State of the program right berfore the function call: tree is an object representing a tree structure with vertices and edges, v is an integer representing the current vertex being processed, and x is an integer representing the minimum size of each remaining connected component after removing edges.
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
        
    #State: `good_components` is the total count of good components found in the subtrees of `v` plus any additional good components identified based on the size of the remaining parts of the subtrees, and `remaining_size` is the total size of the remaining parts of the subtrees that did not meet the size threshold `x`.
    return good_components, remaining_size
    #The program returns a tuple where the first element is the total count of good components found in the subtrees of `v` plus any additional good components identified based on the size of the remaining parts of the subtrees, and the second element is the total size of the remaining parts of the subtrees that did not meet the size threshold `x`.
#Overall this is what the function does:The function processes a tree structure starting from a given vertex `v` and calculates the number of good components in its subtrees, where a good component is defined as having a size of at least `x`. It also calculates the total size of the remaining parts of the subtrees that do not meet the size threshold `x`. The function returns a tuple containing the count of good components and the size of the remaining parts.

#State of the program right berfore the function call: tree is an object representing a tree with n vertices, n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed, and x is an integer representing the minimum size of each remaining connected component.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True
    #State: `tree` is an object representing a tree with `n` vertices, `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed, `x` is an integer representing the minimum size of each remaining connected component, `good_components` is the number of good components returned by `func_1`, and `remaining_size` is the remaining size returned by `func_1`. Additionally, `good_components` is less than or equal to `k`.
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True
    #State: `tree` is an object representing a tree with `n` vertices, `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed, `x` is an integer representing the minimum size of each remaining connected component, `good_components` is the number of good components returned by `func_1`, and `remaining_size` is the remaining size returned by `func_1`. Additionally, `good_components` is less than or equal to `k`. Either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_3` determines whether it is possible to remove `k` edges from the tree such that each remaining connected component has at least `x` vertices. It returns `True` if this condition can be met, otherwise it returns `False`.

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
        
    #State: beg = end = the largest integer x such that func_3(tree, n, k, x) is True.
    return beg
    #The program returns the largest integer x such that func_3(tree, n, k, x) is True.
#Overall this is what the function does:The function `func_4` takes a tree represented by the object `tree`, an integer `n` representing the number of vertices in the tree, and an integer `k` representing the number of edges to be removed. It returns the largest integer `x` for which the function `func_3(tree, n, k, x)` evaluates to True.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: `n` is an integer representing the number of vertices in the tree, and `k` is an integer representing the number of edges to be removed such that 1 <= k < n; `tree` is an instance of the Tree class with `n` vertices and `n-1` edges added to it.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: k + 1 (assuming func_4 returns the number of connected components after removing k edges from the tree)
#Overall this is what the function does:The function `func_5` reads an integer `n` representing the number of vertices and an integer `k` representing the number of edges to be removed from a tree. It constructs a tree with `n` vertices and `n-1` edges, roots the tree, and then calculates and prints the number of connected components in the tree after removing `k` edges.

