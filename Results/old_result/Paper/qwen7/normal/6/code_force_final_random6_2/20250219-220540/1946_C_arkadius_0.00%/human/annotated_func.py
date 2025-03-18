#State of the program right berfore the function call: `tree` is an instance of a class representing a tree where each vertex has attributes `children`, `good_components`, and `remaining_size`. `s` is an integer representing the starting vertex, and `x` is an integer representing the minimum size of each remaining connected component after removing the edges.
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
        
    #State: All vertices in the tree have their `good_components` attribute set to the sum of `good_components` from all their children plus the number of children whose `remaining_size` is greater than or equal to `x`. The `remaining_size` attribute of each vertex is the total `remaining_size` of all its children.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the tuple containing the `good_components` and `remaining_size` attributes of the vertex with the identifier `s` in the tree. The `good_components` attribute is calculated as the sum of `good_components` from all its children plus the number of children whose `remaining_size` is greater than or equal to `x`. The `remaining_size` attribute is the total `remaining_size` of all its children.
#Overall this is what the function does:The function accepts a tree (an instance with attributes `children`, `good_components`, and `remaining_size`), a starting vertex `s`, and a minimum size `x`. It traverses the tree using a postorder traversal to update the `good_components` and `remaining_size` attributes of each vertex. After processing, it returns a tuple containing the updated `good_components` and `remaining_size` attributes of the vertex with the identifier `s`. The `good_components` is calculated as the sum of `good_components` from all its children plus the count of children whose `remaining_size` is greater than or equal to `x`. The `remaining_size` is the total `remaining_size` of all its children.

#State of the program right berfore the function call: `tree` is an instance of a tree class representing a tree structure where each vertex has a `children` attribute containing its child vertices; `v` is an integer representing the root vertex of the current subtree being processed; `x` is an integer representing the minimum size of each remaining connected component after removing exactly `k` edges.
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
        
    #State: good_components is the sum of all `good_components_subtree` values plus the number of times `remaining_size_subtree` was greater than or equal to `x`; `remaining_size` is the sum of all `remaining_size_subtree` values.
    return good_components, remaining_size
    #The program returns good_components which is the sum of all `good_components_subtree` values plus the number of times `remaining_size_subtree` was greater than or equal to `x`, and remaining_size which is the sum of all `remaining_size_subtree` values.
#Overall this is what the function does:The function processes a tree structure to determine the number of "good components" and their total size after removing exactly k edges. A "good component" is defined as a subtree where the remaining size (number of vertices) is at least x. The function returns two values: the total count of such good components and their combined size.

#State of the program right berfore the function call: tree is a representation of a tree with n vertices, n and k are positive integers such that 1 ≤ k < n ≤ 10^5, and x is an integer representing the minimum size of each remaining connected component after removing k edges.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True
    #State: `tree` is a representation of a tree with n vertices, `n` and `k` are positive integers such that 1 ≤ k < n ≤ 10^5, `x` is an integer representing the minimum size of each remaining connected component after removing k edges, `good_components` is the result returned by `func_1` and `remaining_size` is the result returned by `func_1`. `good_components` is less than or equal to k
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True
    #State: `tree` is a representation of a tree with n vertices, `n` and `k` are positive integers such that 1 ≤ k < n ≤ 10^5, `x` is an integer representing the minimum size of each remaining connected component after removing k edges, `good_components` is less than or equal to k, `good_components` is not equal to k or `remaining_size` is less than x
    return False
    #The program returns False
#Overall this is what the function does:The function `func_3` accepts a tree representation (`tree`), along with integers `n`, `k`, and `x`. It returns `True` if either:

- More than `k` components remain after removing `k` edges, or
- Exactly `k` components remain and each component has at least `x` vertices.

Otherwise, it returns `False`.

#State of the program right berfore the function call: tree is an instance of a Tree class representing the given tree structure, n is the number of vertices in the tree, and k is the number of edges to be removed such that 1 ≤ k < n.
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: Output State: The final values of `beg`, `end`, and `mid` will be such that `beg` is equal to `end`.
    #
    #Explanation: The loop continues to narrow down the range between `beg` and `end` until they converge. After each iteration, `mid` is recalculated as the midpoint of the current range. Depending on the outcome of `func_3(tree, n, k, mid)`, either `beg` or `end` is updated. Eventually, when `beg` equals `end`, the condition `beg < end` fails, and the loop terminates. At this point, both `beg` and `end` will hold the same value, which is the result of the binary search performed by the loop.
    return beg
    #The program returns the value of `beg` (or `end`) which is the point where the binary search converges, meaning `beg` and `end` are equal after the loop terminates.
#Overall this is what the function does:The function accepts a tree (an instance of a Tree class), the number of vertices `n`, and the number of edges `k` to be removed such that 1 ≤ k < n. It performs a binary search to find a point where the condition converges, meaning the values of `beg` and `end` are equal after the loop terminates, and returns this converged value.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed, and tree is an instance of a custom Tree class with methods add_edge and root_tree_non_recursive. The input is read from standard input, where the first line contains t (1 ≤ t ≤ 10^4), the number of test cases. Each test case starts with two integers n and k, followed by n-1 lines describing the edges of the tree.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: Output State: `i` is equal to `n`, `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed, and the `tree` object contains `n-1 + k` edges, as all possible edges between `n` vertices have been added and `k` edges have been removed.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will be equal to `n`, indicating that the loop has completed all its iterations. The `tree` object will have exactly `n-1 + k` edges, because initially it would have `n-1` edges (a tree with `n` vertices always has `n-1` edges), and then `k` edges are removed, resulting in `n-1 + k` edges in total. The values of `n` and `k` remain unchanged, and the list `[u, v]` represents the last pair of vertices for which an edge was added before `k` edges were removed.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: func_4(tree, n, k) (where tree is an object representing the tree with n-1 + k edges, n is the number of vertices in the tree, and k is the number of edges to be removed)
#Overall this is what the function does:The function processes input data from standard input to construct a tree with a specified number of vertices and edges. It then removes a specified number of edges from the tree and returns the result of another function `func_4` applied to the modified tree, along with the original number of vertices and edges to be removed.

