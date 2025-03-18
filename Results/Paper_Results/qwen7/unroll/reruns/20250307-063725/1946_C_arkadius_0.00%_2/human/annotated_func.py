#State of the program right berfore the function call: `tree` is an instance of a custom `Tree` class representing the tree structure, `s` is the starting vertex (an integer), and `x` is an integer representing the minimum size of each remaining connected component after removing exactly `k` edges.
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
        
    #State: Output State: The `stack` is empty, and for each vertex `v` in the `tree`, `tree.vertices[v].good_components` is updated based on the sizes of its children's components and their remaining sizes compared to `x`. Specifically, `tree.vertices[v].good_components` counts how many connected components, including itself, have a remaining size of at least `x` after removing exactly `k` edges from the tree.
    #
    #In this state, the `tree` has been traversed using a post-order traversal (hence the use of the `postorder` flag in the stack). For every vertex, the count of good components (components with remaining size ≥ `x`) is accumulated from its children. If a child's remaining size is at least `x`, it contributes to the parent's `good_components` count. Otherwise, the parent's `remaining_size` is incremented by the child's `remaining_size`.
    #
    #The `stack` being empty indicates that all vertices have been processed according to the described logic.
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns the tuple containing the number of good components for vertex `s` in the tree and the remaining size of vertex `s`. The number of good components is the count of connected components, including itself, that have a remaining size of at least `x` after removing exactly `k` edges from the tree. The remaining size of vertex `s` is the total size of the component rooted at `s` minus the size of the components that have a remaining size less than `x`.
#Overall this is what the function does:The function `func_1` takes a `Tree` object, a starting vertex `s`, and an integer `x` as inputs. It performs a post-order traversal of the tree to update the `good_components` and `remaining_size` attributes for each vertex. After processing all vertices, it returns a tuple containing the number of good components for the starting vertex `s` and the remaining size of the component rooted at `s`. A good component is defined as a connected component, including itself, that has a remaining size of at least `x` after removing exactly `k` edges from the tree.

#State of the program right berfore the function call: `tree` is an instance of a tree class representing a tree structure where each vertex has a list of children. `v` is an integer representing the current vertex being processed, and `x` is an integer representing the minimum size of each remaining connected component after removing edges.
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
        
    #State: Output State: `good_components` is the sum of all `good_components_subtree` plus the number of subtrees where `remaining_size_subtree` is greater than or equal to `x`, and `remaining_size` is the cumulative sum of all `remaining_size_subtree`.
    return good_components, remaining_size
    #The program returns good_components which is the sum of all good_components_subtree plus the number of subtrees where remaining_size_subtree is greater than or equal to x, and remaining_size which is the cumulative sum of all remaining_size_subtree.
#Overall this is what the function does:The function processes a tree structure to count the number of good components and calculate the remaining size. A good component is defined as a subtree where the remaining size (number of vertices) is greater than or equal to the given minimum size \( x \). The function returns two values: `good_components`, which is the total count of such good components, and `remaining_size`, which is the cumulative size of all subtrees.

#State of the program right berfore the function call: tree is a Tree object representing a tree with n vertices, n and k are integers such that 1 ≤ k < n ≤ 10^5, and x is an integer representing the size of the connected components after removing k edges.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True
    #State: `tree` is a Tree object representing a tree with n vertices, `n` and `k` are integers such that 1 ≤ k < n ≤ 10^5, `x` is an integer representing the size of the connected components after removing k edges, `good_components` is the result returned by `func_1`, and `remaining_size` is the result returned by `func_1`. `good_components` is less than or equal to k
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True
    #State: `tree` is a Tree object representing a tree with n vertices, `n` and `k` are integers such that 1 ≤ k < n ≤ 10^5, `x` is an integer representing the size of the connected components after removing k edges, `good_components` is the result returned by `func_1`, and `remaining_size` is the result returned by `func_1`. `good_components` is less than k or `remaining_size` is less than x
    return False
    #The program returns False
#Overall this is what the function does:The function `func_3` accepts a Tree object `tree`, an integer `n`, an integer `k`, and an integer `x`. It first calls another function `func_1` to determine the number of good connected components (`good_components`) and their total size (`remaining_size`) after removing `k` edges from the tree. Based on the values of `good_components` and `remaining_size`, the function returns either `True` or `False`. Specifically, it returns `True` if the number of good connected components is greater than `k`, or if the number of good connected components equals `k` and their total size is at least `x`. Otherwise, it returns `False`.

#State of the program right berfore the function call: tree is an instance of a Tree class representing the given tree structure, n is the number of vertices in the tree (an integer), and k is the number of edges to be removed (an integer such that 1 ≤ k < n).
def func_4(tree, n, k):
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: The value of `beg` is the smallest integer `x` such that `func_3(tree, n, k, x)` returns False, and `end` remains as `n`.
    return beg
    #The program returns the smallest integer 'beg' such that 'func_3(tree, n, k, x)' returns False.
#Overall this is what the function does:The function accepts an instance of a Tree class, the number of vertices in the tree, and the number of edges to be removed. It performs a binary search to find the smallest integer `beg` such that calling `func_3(tree, n, k, x)` with `x` starting from `beg` returns False. The function returns this integer `beg`.

#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ k < n ≤ 10^5. The input describes a tree with n vertices, where each of the n-1 lines represents an edge connecting two vertices u and v (1 ≤ u, v ≤ n). The function `func_4` is expected to compute and return the maximum number x such that it is possible to remove exactly k edges from the tree in such a way that the size of each remaining connected component is at least x.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: `tree` is a Tree object with `n` nodes and `k` edges added, connecting nodes based on user input during each iteration of the loop. Each edge connects two nodes, where the nodes are zero-indexed integers ranging from 0 to `n-1`.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: func_4(tree, n, k) (where `tree` is a Tree object with `n` nodes and `k` edges, `n` is the number of nodes, and `k` is the number of edges added)
#Overall this is what the function does:The function processes a tree described by its vertices and edges, computes and returns the maximum number \( x \) such that by removing exactly \( k \) edges from the tree, the size of each remaining connected component is at least \( x \).

