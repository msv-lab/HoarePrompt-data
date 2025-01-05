#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, and the next line contains n integers a1, a2, ..., an where 0 ≤ ai ≤ 10^8 for i from 1 to n. The following n - 1 lines describe the tree edges as pairs of integers (xi, yi) with 1 ≤ xi, yi ≤ n and xi ≠ yi.
def func_1(n):
    return [raw_input().strip() for i in range(n)]
    #The program returns a list of n strings, each representing the input from the user, as it reads n lines of input.
#Overall this is what the function does:The function accepts an integer `n` and returns a list of `n` strings, each representing a line of input read from the user. It does not perform any validation on the input and simply reads `n` lines, regardless of their content or format.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n integers where each integer ai represents the number of apples in the leaf vertices and satisfies 0 ≤ ai ≤ 10^8. The tree is defined by n - 1 edges connecting pairs of vertices (xi, yi) where 1 ≤ xi, yi ≤ n and xi ≠ yi.
def func_2():
    return raw_input().strip()
    #The program returns a string input from the user, stripped of leading and trailing whitespace.
#Overall this is what the function does:The function accepts no parameters and returns a string input from the user, stripped of leading and trailing whitespace. It does not handle any exceptions that may occur during input, such as EOFError or KeyboardInterrupt, which could lead to an unhandled situation if the input is interrupted or unavailable.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n integers where each integer ai (0 ≤ ai ≤ 10^8) represents the number of apples in the leaf vertices, and the edges are defined by n-1 pairs of integers (xi, yi) representing connections between vertices, where 1 ≤ xi, yi ≤ n and xi ≠ yi.
def func_3():
    return map(int, func_2().split())
    #The program returns a list of integers obtained from splitting the output of func_2() and converting each part to an integer. The exact values depend on the implementation of func_2().
#Overall this is what the function does:The function accepts no parameters and returns a map object that produces integers obtained from processing the output of the function `func_2()`. The actual contents of the returned integers depend on the implementation of `func_2()`, and it may not necessarily return a list directly. This function does not handle any errors or edge cases related to the output of `func_2()`.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n integers where each integer ai (0 ≤ ai ≤ 10^8) represents the number of apples in the leaf vertex i; the tree is defined by n-1 edges connecting pairs of vertices (xi, yi) where 1 ≤ xi, yi ≤ n and xi ≠ yi.
def func_4():
    return func_3()[0]
    #The program returns the first element of the result from func_3(), which processes a list of n integers representing apples in the leaf vertices of a tree defined by n-1 edges.
#Overall this is what the function does:The function accepts no parameters and returns the first element of the result from `func_3()`, which presumably processes a list of integers representing the number of apples in the leaf vertices of a tree structure. However, the specifics of how `func_3()` operates and the nature of its output are not defined within this function, meaning the behavior of `func_4()` is contingent on `func_3()`. If `func_3()` fails or returns an empty list, this could lead to an error, as the function does not handle such cases.

#State of the program right berfore the function call: o is a tuple where the first element is an integer n (2 ≤ n ≤ 10^5), the second element is a list of n integers (0 ≤ ai ≤ 10^8) representing the number of apples at each leaf vertex, and the subsequent elements are pairs of integers representing the edges of the tree connecting vertices (1 ≤ xi, yi ≤ n, xi ≠ yi).
def func_5(o):
    print(o)
#Overall this is what the function does:The function accepts a tuple `o` which contains an integer `n` (indicating the number of leaf vertices) and a list of `n` integers representing the number of apples at each leaf vertex, along with pairs of integers that represent the edges of a tree connecting vertices. However, the function currently only prints the tuple `o` and does not perform any further processing or return any value based on the tree or apple data. Therefore, it lacks the functionality implied by the annotations regarding processing the tree and apple data.

#State of the program right berfore the function call: a is a list of integers where 0 ≤ ai ≤ 10^8 for each leaf vertex i, and b is a list of tuples representing edges of the tree, where each tuple contains two distinct integers (xi, yi) such that 1 ≤ xi, yi ≤ n and there are n - 1 such edges connecting n vertices. The number of vertices n is an integer such that 2 ≤ n ≤ 10^5.
def func_6(a, b):
    while b != 0:
        a %= b
        
        a, b = b, a
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the last non-zero value from the previous value of `b` after the last iteration, and the final value of `b` is the last value of `a` before the loop terminated.
    return a
    #The program returns the last non-zero value of 'b' from the previous iteration, which is 'a'
#Overall this is what the function does:The function accepts a list of integers `a` and a list of tuples `b`. It appears to perform a loop that calculates the greatest common divisor (GCD) of the values represented by `a` and `b`. However, since `b` is a list of tuples, the operation may not be valid as the code attempts to use `b` directly as an integer. The function ultimately returns the last non-zero value of `a`, but the logic does not correctly utilize the edges represented by `b`, indicating that the code does not fulfill its intended purpose as described in the annotations.

#State of the program right berfore the function call: a is a list of integers representing the number of apples at each vertex of a tree with n vertices, where 0 ≤ ai ≤ 10^8, and b is a list of tuples representing the edges of the tree, where each tuple contains two integers (xi, yi) with 1 ≤ xi, yi ≤ n and xi ≠ yi. The number of vertices n is an integer such that 2 ≤ n ≤ 10^5.
def func_7(a, b):
    return a / func_6(a, b) * b
    #The program returns the result of the integer division of the list 'a' by the output of func_6(a, b) multiplied by the list of edges 'b'
#Overall this is what the function does:The function accepts a list of integers `a` representing the number of apples at each vertex of a tree and a list of tuples `b` representing the edges of the tree. It performs an integer division of the list `a` by the output of `func_6(a, b)` and multiplies the result by the list of edges `b`. However, there are potential issues: the function does not handle the case where `func_6(a, b)` returns zero, which could lead to a division by zero error. Additionally, as it stands, the operation involving lists is not valid in Python without further context on how to handle the division and multiplication of lists. Thus, the function may not operate as intended.

#State of the program right berfore the function call: node is an integer representing a vertex in a tree, parent is an integer representing the parent vertex of the given node. The tree has n vertices (2 ≤ n ≤ 10^5) with vertex apples represented as a list of integers (0 ≤ ai ≤ 10^8) where ai denotes the number of apples in leaf vertices and non-leaf vertices have a value of zero. The edges between vertices form a connected graph with vertex indices ranging from 1 to n.
def func_8(node, parent):
    ii = -1
    for i in range(len(node[2])):
        if node[2][i] != parent:
            func_8(node[2][i], node)
        else:
            ii = i
        
    #State of the program after the  for loop has been executed: `ii` is the index of the last occurrence of `parent` in `node[2]` or -1 if `parent` is not found; `node[2]` is a list of elements being iterated over.
    if (ii >= 0) :
        node[2].pop(ii)
    #State of the program after the if block has been executed: *`ii` is the index of the last occurrence of `parent` in `node[2]` or -1 if `parent` is not found. If `ii` is non-negative, the element at index `ii` in `node[2]` is removed; otherwise, `node[2]` remains unchanged.
#Overall this is what the function does:The function accepts a list `node` that contains an integer representing a vertex in a tree and another integer `parent` representing the parent vertex of the given node. It traverses the tree structure to remove the last occurrence of the `parent` vertex from the list of child vertices in `node[2]`. If the `parent` is not found in `node[2]`, the list remains unchanged. The function does not return any value.

#State of the program right berfore the function call: node is a tree represented as an integer where the tree has n vertices (2 ≤ n ≤ 10^5), each leaf vertex contains a non-negative integer number of apples (0 ≤ ai ≤ 10^8), and the tree is described by n - 1 edges connecting the vertices.
def func_9(node):
    if (node[1] >= 0) :
        return
        #The program returns the tree structure represented by 'node' with 'n' vertices and the non-negative integer values of apples at the leaf vertices.
    #State of the program after the if block has been executed: *`node` is a tree represented as an integer where the tree has `n` vertices (2 ≤ n ≤ 10^5), each leaf vertex contains a non-negative integer number of apples (0 ≤ ai ≤ 10^8), and the tree is described by `n - 1` edges connecting the vertices. The value of `node[1]` is less than 0.
    lcm = 1
    max = -1
    for child in node[2]:
        func_9(child)
        
        lcm = func_7(lcm, child[0])
        
    #State of the program after the  for loop has been executed: `node` is a tree represented as an integer with `n` vertices; `lcm` is the least common multiple of all child[0] values processed by func_7; `max` is -1; all children of node have been processed by func_9.
    for child in node[2]:
        t = child[1] / lcm * lcm
        
        if max < 0 or max > t:
            max = t
        
    #State of the program after the  for loop has been executed: `node` is a tree with `n` vertices; `max` is the minimum value of `child[1]` for all children in `node[2]` that are greater than or equal to 0; `lcm` is the least common multiple of all child[0] values processed by func_7; `child` is the last child in `node[2]` processed in the loop.
    node[0] = lcm
    node[1] = max * len(node[2])
#Overall this is what the function does:The function accepts a tree structure represented by a list `node`, where each node has a value indicating the least common multiple (LCM) of its children's values and a maximum value derived from the children's values. It recursively computes the LCM of the children's values, updates the maximum value based on the children's values, and returns the updated tree structure with the calculated LCM and maximum value. If the value of `node[1]` is non-negative, the function exits early without modification.

