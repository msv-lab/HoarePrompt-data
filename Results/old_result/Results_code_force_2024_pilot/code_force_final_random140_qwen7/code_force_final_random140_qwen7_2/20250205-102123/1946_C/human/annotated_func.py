#State of the program right berfore the function call: tree is an instance of a Tree class representing a tree structure with vertices and edges, s is an integer representing the starting vertex, and x is an integer representing the minimum size of each remaining connected component after removing k edges.
def func_1(tree, s, x):
    stack = [(s, False)]
    good_components = {}
    remaining_size = {}
    while stack:
        v, postorder = stack.pop()
        
        if not postorder:
            stack.append((v, True))
            good_components[v] = 0
            remaining_size[v] = 1
            for u in tree.vertices[v].children:
                stack.append((u, False))
        elif postorder:
            for u in tree.vertices[v].children:
                good_components[v] += good_components[u]
                if remaining_size[u] >= x:
                    good_components[v] += 1
                else:
                    remaining_size[v] += remaining_size[u]
        
    #State: Output State: `stack` is empty, `tree` remains an instance of the Tree class with its vertices and edges intact, `s` remains unchanged, `x` remains unchanged, `good_components` is a dictionary where the key is the starting vertex `s` and the value is the sum of `good_components[u]` for all child vertices `u` of `s` in `tree.vertices[s].children`, plus the number of child vertices `u` of `s` where `remaining_size[u] >= x`. `remaining_size` is a dictionary where the key is the starting vertex `s` and the value is the sum of `remaining_size[u]` for all child vertices `u` of `s` in `tree.vertices[s].children` where `remaining_size[u] < x`.
    #
    #This final state occurs after the loop has processed all vertices in the tree through a depth-first search (DFS) traversal. The `stack` is emptied as all vertices are popped and processed. The `good_components` dictionary captures the count of good components for the starting vertex `s`, considering the sizes of its connected components after removing `k` edges. The `remaining_size` dictionary accumulates the sizes of the remaining components that do not meet the size requirement `x`.
    return good_components[s], remaining_size[s]
    #The program returns the tuple (good_components[s], remaining_size[s]) where `good_components[s]` is the sum of `good_components[u]` for all child vertices `u` of `s` in `tree.vertices[s].children`, plus the number of child vertices `u` of `s` where `remaining_size[u] >= x`, and `remaining_size[s]` is the sum of `remaining_size[u]` for all child vertices `u` of `s` in `tree.vertices[s].children` where `remaining_size[u] < x`.
#Overall this is what the function does:The function processes a tree structure starting from a given vertex `s`. It performs a depth-first search (DFS) to calculate two metrics for each subtree rooted at `s`: `good_components[s]` and `remaining_size[s]`. `good_components[s]` represents the sum of `good_components[u]` for all child vertices `u` of `s` plus the number of child vertices `u` where `remaining_size[u]` meets or exceeds `x`. `remaining_size[s]` is the sum of `remaining_size[u]` for all child vertices `u` where `remaining_size[u]` is less than `x`. After processing all vertices, the function returns these two values as a tuple.

#State of the program right berfore the function call: `tree` is an instance of a class representing a tree structure, `v` is the root vertex of the tree, and `x` is an integer representing the minimum size of each remaining connected component after removing the edges.
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
        
    #State: Output State: `good_components` is the sum of all `good_components_subtree` values plus additional increments based on the condition, `remaining_size` is the final aggregated value after all iterations, `v` is the initial vertex in `tree`, and `u` iterates through all child vertices of `v` until the loop completes.
    #
    #In more detail, `good_components` will be the total count of components that meet certain criteria (determined by `func_2`) plus any additional components where `remaining_size_subtree` is greater than or equal to `x`. The exact value depends on the specific outputs of `func_2` for each subtree and the condition checks during each iteration. `remaining_size` will reflect the cumulative effect of the operations performed within the loop, specifically when `remaining_size_subtree` is added to it if the condition is not met.
    print(v, good_components, remaining_size)
    #This is printed: v, good_components (where good_components is the sum of all good_components_subtree values plus additional increments based on the condition), remaining_size (where remaining_size reflects the cumulative effect of the operations performed within the loop)
    return good_components, remaining_size
    #The program returns `good_components`, which is the sum of all `good_components_subtree` values plus additional increments based on the condition, and `remaining_size`, which is the final aggregated value after all iterations.
#Overall this is what the function does:The function processes a tree structure to determine the number of "good" components and the remaining size of these components after considering a given threshold `x`. It recursively traverses the tree, counting components that meet specific criteria and aggregating sizes. The function returns two values: `good_components`, which is the total count of components meeting the criteria, and `remaining_size`, which is the combined size of these components.

#State of the program right berfore the function call: tree is an instance of a Tree class representing a tree with n vertices, n and k are integers such that 1 ≤ k < n ≤ 10^5, and x is an integer representing the size of each remaining connected component.
def func_3(tree, n, k, x):
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True
    #State: `tree` is an instance of a Tree class representing a tree with n vertices, `n` is an integer, `k` is an integer such that 1 ≤ k < n ≤ 10^5, `x` is an integer representing the size of each remaining connected component, `good_components` is the number of good components found by the function `func_1`, `remaining_size` is the size of the remaining connected component after processing. `good_components` is less than or equal to k
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True
    #State: `tree` is an instance of a Tree class representing a tree with n vertices, `n` is an integer, `k` is an integer such that 1 ≤ k < n ≤ 10^5, `x` is an integer representing the size of each remaining connected component, `good_components` is the number of good components found by the function `func_1`, `remaining_size` is the size of the remaining connected component after processing. `good_components` is less than k or remaining_size is less than x
    return False
    #The program returns False
#Overall this is what the function does:The function accepts a tree (an instance of a Tree class), and three integers n, k, and x. It first calls another function `func_1` to get the number of good components (`good_components`) and the size of the remaining connected component (`remaining_size`). If the number of good components is greater than k, it returns True. If the number of good components is exactly k and the remaining size is at least x, it also returns True. Otherwise, it returns False.

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
        
    #State: Output State: The loop will terminate when `beg` equals `end`.
    #
    #In the given loop, `beg` starts at 1 and `end` starts at `n`. The loop continues to execute as long as `beg` is less than `end`. Each iteration adjusts either `beg` or `end` based on the result of `func_3(tree, n, k, mid)`. After multiple iterations, `beg` and `end` will converge to the same value because each adjustment brings them closer together until they meet.
    #
    #Since the loop stops when `beg` equals `end`, the final values of `beg`, `end`, and `mid` will all be the same. The exact value depends on the conditions under which `func_3(tree, n, k, mid)` evaluates to `True` or `False` during the iterations, but the key point is that the loop terminates when `beg` and `end` are equal.
    return beg
    #The program returns the value at which `beg` and `end` become equal after the loop terminates.
#Overall this is what the function does:The function accepts a tree (an instance of a Tree class), the number of vertices `n`, and the number of edges `k` to be removed. It then performs a binary search to find a specific value where the variables `beg` and `end` become equal after removing `k` edges from the tree. The function returns this value.

#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ k < n ≤ 10^5. tree is an instance of a custom Tree class representing the tree structure with n vertices, where each vertex is identified by an index from 0 to n-1. The add_edge method of the Tree class is used to add edges between vertices. The root_tree_non_recursive method is used to root the tree at vertex 0 using a non-recursive approach. The func_4 function is expected to compute the maximum number x based on the given tree and values of n and k.
def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: Output State: The loop will have executed `n-1` times, setting `i` to `n-1`. For each iteration from 1 to `n-1`, an edge was added to the tree between nodes `u-1` and `v-1`, where `u` and `v` are integers provided as input. The final state of the tree will have `n` nodes connected by `n-1` edges, forming a tree structure. All nodes from 0 to `n-1` will be reachable from any other node through these edges.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: func_4(tree, n, k) (where tree is a tree structure with n nodes and n-1 edges, and k is an integer)
#Overall this is what the function does:The function `func_5` accepts two parameters, `n` and `k`, where `n` is the number of nodes in a tree and `k` is a positive integer such that 1 ≤ k < n. It also takes a `tree` object, which represents a tree structure with `n` nodes. The function reads the tree edges from standard input, roots the tree at node 0 using a non-recursive approach, and then calls another function `func_4` to compute and return the maximum number `x` based on the given tree and values of `n` and `k`.

