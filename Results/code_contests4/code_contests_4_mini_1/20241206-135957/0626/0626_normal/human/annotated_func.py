#State of the program right berfore the function call: n is an integer (2 ≤ n ≤ 100000), and there is a list of n integers where each integer represents the number of apples in the vertices (0 ≤ ai ≤ 10^8) with non-leaf vertices guaranteed to have a value of zero. The tree structure is defined by n - 1 edges connecting pairs of vertices.
def func_1(n):
    return [raw_input().strip() for i in range(n)]
    #The program returns a list of n integers, each representing the number of apples in the vertices, with values taken from user input.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 100000) and returns a list of `n` strings, each representing the input values for the number of apples at the vertices, taken from user input. The function does not enforce any constraints on the values inputted, meaning users can enter any string, and there is no validation to ensure these inputs are integers or within the specified range for apples (0 ≤ ai ≤ 10^8).

#State of the program right berfore the function call: n is an integer (2 ≤ n ≤ 10^5), representing the number of vertices in the tree; a is a list of integers of length n (0 ≤ ai ≤ 10^8), where ai is the number of apples in the leaf vertices; and the tree is represented by n - 1 edges, each edge connecting two distinct vertices indexed from 1 to n.
def func_2():
    return raw_input().strip()
    #The program returns a string input from the user, stripped of leading and trailing whitespace.
#Overall this is what the function does:The function accepts no parameters and returns a string input from the user, stripped of leading and trailing whitespace. It does not handle any potential exceptions that may arise from invalid input types or other input-related issues, as it relies on the raw_input function to gather input directly from the user.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n integers where each integer ai (0 ≤ ai ≤ 10^8) represents the number of apples in the corresponding vertex, with non-leaf vertices having a value of zero. The tree is defined with n - 1 edges connecting pairs of vertices, and the vertices are indexed from 1 to n with vertex 1 as the root.
def func_3():
    return map(int, func_2().split())
    #The program returns a list of integers obtained from the output of `func_2()` after converting each element to an integer
#Overall this is what the function does:The function accepts no parameters and returns a map object containing integers obtained from the output of `func_2()`, where each element is converted to an integer. Note that the output is not a list but a map object, which is an iterator in Python. This means that if the output is intended to be a list, it should be explicitly cast to a list using `list(map(...))` for proper usage.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n non-negative integers where each element a[i] (0 ≤ a[i] ≤ 10^8) represents the number of apples in leaf vertex i; the tree edges are defined by n-1 pairs of integers (xi, yi) such that 1 ≤ xi, yi ≤ n and xi ≠ yi. Vertex 1 is the root of the tree.
def func_4():
    return func_3()[0]
    #The program returns the first element of the output from func_3, which likely contains information based on the number of apples in the leaf vertices of the tree structure defined by the given integer n and list a.
#Overall this is what the function does:The function accepts no parameters and returns the first element of the output from func_3. The output from func_3 is expected to contain information related to the number of apples in the leaf vertices of a tree structure, which is defined by a given integer n and a list a. However, without knowing the exact implementation of func_3, it is unclear what this first element represents or if it handles all edge cases related to the tree structure and the number of apples properly.

#State of the program right berfore the function call: o is a tuple consisting of an integer n (2 ≤ n ≤ 10^5) representing the number of vertices in the tree, a list of n integers where each integer ai (0 ≤ ai ≤ 10^8) represents the number of apples in the leaf vertices, and a list of n-1 pairs of integers representing the edges of the tree where each pair (xi, yi) (1 ≤ xi, yi ≤ n, xi ≠ yi) connects two vertices.
def func_5(o):
    print(o)
#Overall this is what the function does:The function accepts a tuple `o` that contains an integer `n` (representing the number of vertices in a tree), a list of `n` integers (each representing the number of apples in the leaf vertices), and a list of `n-1` pairs of integers (representing the edges of the tree). Currently, the function only prints the input tuple and does not perform any processing or produce any result based on the tree structure or the apples.

#State of the program right berfore the function call: a is a list of integers representing the number of apples in each vertex of a rooted tree, with the first element corresponding to the root and subsequent elements corresponding to leaf vertices, where 0 ≤ ai ≤ 10^8; b is a list of tuples representing edges between vertices, with each tuple containing two integers (xi, yi) indicating a connection between vertex xi and vertex yi, where 1 ≤ xi, yi ≤ n and xi ≠ yi. n is an integer such that 2 ≤ n ≤ 10^5.
def func_6(a, b):
    while b != 0:
        a %= b
        
        a, b = b, a
        
    #State of the program after the loop has been executed: `b` is an empty list, `a` holds the final result of the last non-empty value of `b`, which is derived from the iterations of the loop using the previous values of `a` and `b`.
    return a
    #The program returns the final result 'a' derived from the last non-empty value of list 'b' after iterations using previous values of 'a' and 'b'
#Overall this is what the function does:The function accepts a list of integers `a` and a list of tuples `b`. It appears to implement an iterative algorithm that computes the greatest common divisor (GCD) of the values represented in `a` and `b`. However, the code does not utilize the elements of the list `a`, which means it only processes the list `b`. As written, the function will return the last non-zero value of `b` after performing the modulus operation, but it lacks proper handling for edge cases such as an empty list `b` or cases where all elements in `b` are zero. If `b` does not contain any non-zero values, the function may lead to unexpected results.

#State of the program right berfore the function call: a is a list of integers representing the number of apples at each leaf vertex, with 0 ≤ ai ≤ 10^8, and b is an integer representing the number of edges in the tree, where 2 ≤ n ≤ 10^5. The edges are defined as pairs of integers representing connections between vertices.
def func_7(a, b):
    return a / func_6(a, b) * b
    #The program returns the list of integers 'a' divided by the result of func_6(a, b) multiplied by the integer 'b'
#Overall this is what the function does:The function accepts a list of integers `a` representing the number of apples at each leaf vertex and an integer `b` representing the number of edges in the tree. It returns the result of dividing each element in `a` by the output of `func_6(a, b)` (which may be a number or could potentially lead to a division by zero error if `func_6(a, b)` returns zero) and then multiplying by `b`. If `func_6(a, b)` returns zero, this will cause a division error, which is not handled in the code.

#State of the program right berfore the function call: node is an integer representing a vertex in a tree with n vertices, where 2 ≤ n ≤ 10^5; parent is an integer representing the parent vertex of the current node, with the constraint that 1 ≤ parent ≤ n. The tree is defined such that all non-leaf vertices have a value of zero apples, while leaf vertices contain an integer number of apples (0 ≤ ai ≤ 10^8).
def func_8(node, parent):
    ii = -1
    for i in range(len(node[2])):
        if node[2][i] != parent:
            func_8(node[2][i], node)
        else:
            ii = i
        
    #State of the program after the  for loop has been executed: `ii` is the last index of `node[2]` where `node[2][i]` is equal to `parent`, or -1 if no such index exists; `i` is equal to `len(node[2])` after all iterations.
    if (ii >= 0) :
        node[2].pop(ii)
    #State of the program after the if block has been executed: *`ii` is the last index of `node[2]` where `node[2][i]` is equal to `parent`, or -1 if no such index exists; `i` is equal to `len(node[2])` after all iterations. If `ii` is greater than or equal to 0, the element at index `ii` in `node[2]` has been removed.
#Overall this is what the function does:The function accepts a `node`, which is a list representing a vertex in a tree, and `parent`, which is the parent vertex of the current node. It recursively traverses the tree, removing the parent from the list of children in `node[2]` if it exists. The function does not return the number of apples associated with the specified node, as stated in the annotations, but instead modifies the input `node` in place by removing the specified parent from its children. There is no handling of the number of apples or any related computation.

#State of the program right berfore the function call: node is a tree represented as a rooted structure with n vertices, where n is an integer (2 ≤ n ≤ 10^5), and each leaf vertex contains a non-negative integer (0 ≤ ai ≤ 10^8) representing the number of apples. Non-leaf vertices have a value of zero. The tree is defined by n-1 edges connecting pairs of distinct vertices.
def func_9(node):
    if (node[1] >= 0) :
        return
        #The program returns the tree structure represented by 'node' with 'n' vertices, where each leaf vertex contains a non-negative integer representing the number of apples, and non-leaf vertices have a value of zero. The vertex at index 1 has a value greater than or equal to 0.
    #State of the program after the if block has been executed: *`node` is a tree represented as a rooted structure with n vertices, where n is an integer (2 ≤ n ≤ 10^5), and each leaf vertex contains a non-negative integer (0 ≤ ai ≤ 10^8) representing the number of apples. Non-leaf vertices have a value of zero. The value of the root vertex (node[1]) is negative.
    lcm = 1
    max = -1
    for child in node[2]:
        func_9(child)
        
        lcm = func_7(lcm, child[0])
        
    #State of the program after the  for loop has been executed: `node[2]` contains `k` children, `lcm` is the least common multiple of `child[0]` values from all `k` children, `max` is -1.
    for child in node[2]:
        t = child[1] / lcm * lcm
        
        if max < 0 or max > t:
            max = t
        
    #State of the program after the  for loop has been executed: `lcm` is the least common multiple of `child[0]` values from all `k` children; `max` is the minimum value of `t` calculated from all `child[1]` values of the children in `node[2]`, if `k` is greater than 0; if `k` is 0, `max` remains -1.
    node[0] = lcm
    node[1] = max * len(node[2])
#Overall this is what the function does:The function accepts a tree structure represented by the `node`, where `node` has `n` vertices (2 ≤ n ≤ 10^5). Each leaf vertex contains a non-negative integer representing apples, while non-leaf vertices have a value of zero. The function checks if the value of the root vertex (node[1]) is non-negative; if it is, the function returns early without modifying the tree. If the root vertex is negative, it calculates the least common multiple (LCM) of the values of the children nodes and assigns this value to node[0]. It also calculates a maximum value derived from the child nodes' values and multiplies it by the number of children, assigning this to node[1]. The function does not handle cases where the tree structure is malformed or does not adhere to the assumptions about its structure.

