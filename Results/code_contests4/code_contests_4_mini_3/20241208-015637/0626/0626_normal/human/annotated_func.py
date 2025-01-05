#State of the program right berfore the function call: n is an integer between 2 and 100,000 (2 ≤ n ≤ 10^5), representing the number of vertices in the tree; and there is a list of n integers where each integer (0 ≤ ai ≤ 10^8) represents the number of apples at the leaf vertices, with non-leaf vertices guaranteed to have zero apples. Additionally, there are n - 1 edges described by pairs of integers, each representing a connection between two vertices (1 ≤ xi, yi ≤ n, xi ≠ yi).
def func_1(n):
    return [raw_input().strip() for i in range(n)]
    #The program returns a list of n integers, where each integer represents the number of apples at the leaf vertices, inputted by the user
#Overall this is what the function does:The function accepts an integer `n`, representing the number of leaf vertices in a tree, and returns a list of `n` integers which are inputted by the user. Each integer represents the number of apples at the corresponding leaf vertices. The function does not validate the input or handle any potential errors that may arise from user input.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, and there is a list of n integers where each integer ai (0 ≤ ai ≤ 10^8) represents the number of apples in the leaf vertices, with non-leaf vertices guaranteed to have zero apples. The tree is described by n - 1 edges connecting pairs of vertices, where each edge consists of two distinct integers xi and yi (1 ≤ xi, yi ≤ n).
def func_2():
    return raw_input().strip()
    #The program returns the raw input as a string, stripped of any leading or trailing whitespace.
#Overall this is what the function does:The function accepts no parameters and returns the raw input from the user as a string, stripped of any leading or trailing whitespace. It does not process any additional logic related to the tree structure or the integers described in the comments.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, and there is a list of n integers representing the number of apples in each vertex, where each integer ai satisfies 0 ≤ ai ≤ 10^8. The tree is described by n-1 edges connecting the vertices, with each edge connecting two distinct vertices indexed from 1 to n.
def func_3():
    return map(int, func_2().split())
    #The program returns a map object containing integers parsed from the output of func_2(), which is expected to be a space-separated string of integers.
#Overall this is what the function does:The function accepts no parameters and returns a map object that contains integers parsed from the output of `func_2()`, which is expected to be a space-separated string of integers. There are no checks for the output of `func_2()`, so if `func_2()` returns an invalid string or if exceptions occur, they will not be handled within this function.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree (2 ≤ n ≤ 10^5), and a is a list of n integers where each integer ai (0 ≤ ai ≤ 10^8) represents the number of apples in the leaf vertices of the tree. The tree is defined by n-1 edges connecting the vertices, where each edge connects two distinct vertices indexed from 1 to n.
def func_4():
    return func_3()[0]
    #The program returns the first element of the result from the function func_3(), which is expected to contain relevant information based on the number of vertices and the number of apples in the leaf vertices of the tree.
#Overall this is what the function does:The function accepts no parameters and returns the first element from the output of the function `func_3()`, which is expected to provide relevant information regarding the number of vertices and the number of apples in the leaf vertices of a tree. However, the exact nature of this information and potential edge cases related to the output of `func_3()` are not specified in the provided code.

#State of the program right berfore the function call: o is a tuple containing an integer n (2 ≤ n ≤ 10^5), a list of n integers representing the number of apples in the leaf vertices (0 ≤ ai ≤ 10^8), and a list of n-1 pairs of integers representing the edges of the tree.
def func_5(o):
    print(o)
#Overall this is what the function does:The function accepts a tuple `o` containing an integer `n` (where 2 ≤ n ≤ 10^5), a list of `n` integers representing the number of apples in the leaf vertices (where each value is between 0 and 10^8), and a list of `n-1` pairs of integers representing the edges of a tree. The current implementation only prints the input tuple and does not process or return any value based on the structure of the tree or the apples in the leaf vertices. Therefore, it lacks any functionality beyond this print statement.

#State of the program right berfore the function call: a is a list of n integers representing the number of apples in each vertex, where 0 ≤ ai ≤ 10^8, and b is a list of n-1 tuples representing the edges of the tree, where each tuple contains two distinct integers representing connected vertices (1 ≤ xi, yi ≤ n).
def func_6(a, b):
    while b != 0:
        a %= b
        
        a, b = b, a
        
    #State of the program after the loop has been executed: `a` is a list of n-1 tuples, `b` is a list of n integers, the loop has terminated.
    return a
    #The program returns the list of n-1 tuples stored in variable 'a'
#Overall this is what the function does:The function accepts a list of integers `a` and a list of tuples `b`. However, the code incorrectly uses the variables `a` and `b`, leading to unexpected behavior. The intended functionality seems to involve a loop that modifies `a` and `b` using the modulo operation, but this will not yield a meaningful result based on the provided annotations. Ultimately, the function attempts to return the list stored in `a`, which is a list of integers, not tuples as stated in the annotations. Therefore, the function does not perform as described in the annotations and instead returns the modified `a`. Additionally, there are no checks for the input parameters, and if `b` is not initialized correctly, it may lead to an infinite loop or an error.

#State of the program right berfore the function call: a is a list of integers where each integer represents the number of apples in the leaf vertices of a rooted tree, and b is a list of tuples where each tuple contains two integers representing the edges connecting the vertices in the tree. The number of vertices in the tree is n, where 2 ≤ n ≤ 10^5, and each integer in the list a satisfies 0 ≤ ai ≤ 10^8.
def func_7(a, b):
    return a / func_6(a, b) * b
    #The program returns the result of dividing the list of integers 'a' by the result of 'func_6(a, b)' and then multiplying by 'b', where 'a' represents the number of apples in the leaf vertices and 'b' contains the edges connecting the vertices in the tree.
#Overall this is what the function does:The function accepts a list of integers `a` representing the number of apples in leaf vertices of a rooted tree and a list of tuples `b` representing the edges connecting the vertices in the tree. It divides the list of integers `a` by the result of the function `func_6(a, b)` and then multiplies this result by the list of tuples `b`. However, it is important to note that if `func_6(a, b)` returns 0, this will lead to a division by zero error. Additionally, the overall operation involving lists `a` and `b` may not be correctly defined for element-wise operations as indicated. Therefore, the function may not behave as intended if the assumptions about the mathematical operations on lists are incorrect.

#State of the program right berfore the function call: node is an integer representing a vertex in the tree, parent is an integer representing the parent vertex of the current node. The tree has n vertices (2 ≤ n ≤ 10^5), with leaf vertices containing non-negative integers (0 ≤ ai ≤ 10^8) representing the number of apples, and non-leaf vertices having zero apples.
def func_8(node, parent):
    ii = -1
    for i in range(len(node[2])):
        if node[2][i] != parent:
            func_8(node[2][i], node)
        else:
            ii = i
        
    #State of the program after the  for loop has been executed: `ii` is the index of the last occurrence of `parent` in `node[2]` or -1 if `parent` is not found, `i` is equal to `len(node[2])`, and `node[2]` is a list with at least `len(node[2])` elements.
    if (ii >= 0) :
        node[2].pop(ii)
    #State of the program after the if block has been executed: *`ii` is the index of the last occurrence of `parent` in `node[2]` or -1 if `parent` is not found, `i` is equal to `len(node[2])`, and if `ii` is non-negative, then `node[2]` has one less element after the pop operation. If `ii` is -1, there is no change to `node[2]` or `i`.
#Overall this is what the function does:The function accepts a `node`, which is a list containing information about a vertex in a tree structure, and a `parent`, which is an integer representing the parent vertex of the current node. It recursively processes the child vertices of the given node, removing the last occurrence of the parent from the list of child vertices if found. The function does not return any value, and it modifies the `node` in place. The function does not compute or return any information related to the number of apples in leaf vertices or their relationships; it only focuses on modifying the list of child vertices.

#State of the program right berfore the function call: node is a tree represented as a rooted structure with n vertices where n is an integer (2 ≤ n ≤ 10^5). Each leaf vertex contains a non-negative integer representing the number of apples (0 ≤ ai ≤ 10^8), and non-leaf vertices have a value of zero. The edges connecting the vertices are given as pairs of integers.
def func_9(node):
    if (node[1] >= 0) :
        return
        #The program returns the tree structure 'node' with 'n' vertices, where leaf vertices contain non-negative integers representing the number of apples, and non-leaf vertices have a value of zero. The value of 'node[1]' is greater than or equal to 0.
    #State of the program after the if block has been executed: *`node` is a tree represented as a rooted structure with `n` vertices where `n` is an integer (2 ≤ n ≤ 10^5). Each leaf vertex contains a non-negative integer representing the number of apples (0 ≤ ai ≤ 10^8), and non-leaf vertices have a value of zero. The value of `node[1]` is less than 0.
    lcm = 1
    max = -1
    for child in node[2]:
        func_9(child)
        
        lcm = func_7(lcm, child[0])
        
    #State of the program after the  for loop has been executed: `node` is a tree with at least one child in `node[2]`; `lcm` is the least common multiple of the values returned by `func_7(lcm, child[0])` for all children in `node[2]`; `func_9(child)` has been executed for all children in `node[2]`.
    for child in node[2]:
        t = child[1] / lcm * lcm
        
        if max < 0 or max > t:
            max = t
        
    #State of the program after the  for loop has been executed: `node` is a tree with at least one child in `node[2]`, `lcm` is the least common multiple of the values returned by `func_7(lcm, child[0])` for all children in `node[2]`, `func_9(child)` has been executed for all children in `node[2]`, `child` is the last child in `node[2]`, `t` is equal to the value of the last child's second element, and `max` is the maximum value of `t` encountered during the iterations, which is either equal to the last `t` or the maximum of all previous `t` values if `max` was updated during the loop executions.`
    node[0] = lcm
    node[1] = max * len(node[2])
#Overall this is what the function does:The function accepts a tree structure `node` representing a rooted tree with `n` vertices, where each leaf vertex contains a non-negative integer (the number of apples) and non-leaf vertices have a value of zero. If `node[1]` is less than zero, the function calculates the least common multiple of the values from its children nodes and updates `node[0]` to this LCM. It also calculates the maximum adjusted value based on the number of apples in the children nodes, updates `node[1]` accordingly, and returns the modified tree structure. If `node[1]` is greater than or equal to zero, the function returns without making any changes.

