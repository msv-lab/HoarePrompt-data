#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5.**
def func_1(n):
    return [raw_input().strip() for i in range(n)]
    #The program returns a list of n strings where n is an integer between 2 and 10^5
#Overall this is what the function does:The function func_1 accepts an integer n, where 2 <= n <= 10^5, and returns a list of n strings obtained by stripping input from the user.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. ai is an integer such that 0 <= ai <= 10^8 for each 1 <= i <= n.**
def func_2():
    return raw_input().strip()
    #The program returns the input string after stripping any leading or trailing whitespaces
#Overall this is what the function does:The function does not accept any parameters. It reads a line of input from the user and returns the input string after removing any leading or trailing whitespaces.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. ai is an integer such that 0 <= ai <= 10^8 for 1 <= i <= n.**
def func_3():
    return map(int, func_2().split())
    #The program returns a map object containing integers after applying the int function to the result of splitting the output of func_2().
#Overall this is what the function does:The function `func_3` does not accept any parameters. It internally calls another function `func_2` and processes its output. The output of `func_2` is split and then the `int` function is applied to each element. The function `func_3` returns a map object containing these processed integers.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 105. ai is an integer such that 0 <= ai <= 10^8. xi and yi are integers such that 1 <= xi, yi <= n and xi != yi.**
def func_4():
    return func_3()[0]
    #The program returns the first element of the output of function func_3()
#Overall this is what the function does:The function `func_4` does not accept any parameters. It calls `func_3()` and returns the first element of its output.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8 for i from 1 to n, and the number of apples in non-leaf vertices is zero. The tree edges are described by pairs of integers xi, yi where 1 <= xi, yi <= n and xi ≠ yi. Vertex 1 is the root.**
def func_5(o):
    print(o)
#Overall this is what the function does:The function `func_5` accepts a parameter `o` and prints the value of `o`. The parameter `n` is an integer such that 2 <= n <= 10^5. The parameter `ai` is an integer such that 0 <= ai <= 10^8 for i from 1 to n. The number of apples in non-leaf vertices is zero. The tree edges are described by pairs of integers xi, yi where 1 <= xi, yi <= n and xi ≠ yi. Vertex 1 is the root. The function does not have a specified return value.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. a is a list of integers with length n such that 0 <= ai <= 10^8.**
def func_6(a, b):
    while b != 0:
        a %= b
        
        a, b = b, a
        
    #State of the program after the loop has been executed: `a` and `b` hold the greatest common divisor of the initial values of `a` and `b`, `b` is 0
    return a
    #The program returns the greatest common divisor of the initial values of `a` and `b`, where `b` is 0.
#Overall this is what the function does:The function `func_6` accepts two parameters, `a` and `b`. Parameter `a` is a list of integers with length n such that 0 <= ai <= 10^8, and parameter `b` is an integer. The function calculates the greatest common divisor of the initial values of `a` and `b` and returns it. If `b` is 0, it returns the greatest common divisor. However, there is a potential issue with the code logic as the current implementation may not handle the case where `b` is not 0 properly.

#State of the program right berfore the function call: **Precondition**: **n is an integer such that 2 <= n <= 10^5. a1, a2, ..., an are integers such that 0 <= ai <= 10^8. The input represents a rooted tree with n vertices where the number of apples in non-leaf vertices is zero.**
def func_7(a, b):
    return a / func_6(a, b) * b
    #The program returns the result of dividing the value of 'a' by the result of calling function func_6 with 'a' and 'b' as parameters, then multiplying the result by the value of 'b'
#Overall this is what the function does:The function func_7 accepts two parameters `a` and `b`. It calculates the result of dividing 'a' by the return value of func_6(a, b), then multiplies this result by 'b' and returns the final value. However, there is a missing implementation detail for func_6 which could affect the functionality if not handled correctly.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8, and xi, yi are integers such that 1 <= xi, yi <= n and xi != yi.**
def func_8(node, parent):
    ii = -1
    for i in range(len(node[2])):
        if node[2][i] != parent:
            func_8(node[2][i], node)
        else:
            ii = i
        
    #State of the program after the  for loop has been executed: n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8, xi and yi are integers such that 1 <= xi, yi <= n and xi != yi, ii is the index of the last occurrence where node[2][i] is equal to parent or -1 if no such occurrence happened during the loop execution.
    if (ii >= 0) :
        node[2].pop(ii)
    #State of the program after the if block has been executed: *n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8, xi and yi are integers such that 1 <= xi, yi <= n and xi != yi. If ii >= 0, the last occurrence where node[2][i] is equal to parent has been removed from the node[2] list.
#Overall this is what the function does:The function `func_8` recursively processes a tree-like structure represented by `node` and `parent`. It iterates through the children nodes of `node`, removing the last occurrence where a child node is equal to the parent node from the list of children nodes. The function does not have a specific return value mentioned, so the final state of the tree structure depends on the execution of the function.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. The list a contains n integers where 0 <= ai <= 10^8. Each pair of integers xi, yi in the following n-1 lines represents valid edges in the tree.**
def func_9(node):
    if (node[1] >= 0) :
        return
        #The program does not return anything
    #State of the program after the if block has been executed: *n is an integer such that 2 <= n <= 10^5. The list a contains n integers where 0 <= ai <= 10^8. Each pair of integers xi, yi in the following n-1 lines represents valid edges in the tree. The first node does not have a value less than 0
    lcm = 1
    max = -1
    for child in node[2]:
        func_9(child)
        
        lcm = func_7(lcm, child[0])
        
    #State of the program after the  for loop has been executed: `lcm` is updated based on the result of `func_7` for each child in `node[2] and there are no more child nodes left in `node[2]` to iterate over, `max` remains -1
    for child in node[2]:
        t = child[1] / lcm * lcm
        
        if max < 0 or max > t:
            max = t
        
    #State of the program after the  for loop has been executed: `lcm` is updated based on the result of `func_7` for each child in `node[2]`, `max` is updated to the maximum value of `t` calculated in each iteration of the loop, loop iterates over all children in `node[2]`
    node[0] = lcm
    node[1] = max * len(node[2])
#Overall this is what the function does:The function `func_9` processes the input parameters related to a tree structure represented by a `node`. The `node` parameter is an integer within the range 2 to 10^5. The function iterates over the children nodes in `node[2]`, calculates the least common multiple (`lcm`) based on the result of `func_7`, and updates the maximum value (`max`) based on calculations involving `lcm`. The function then assigns the calculated `lcm` to `node[0]` and the product of `max` and the number of children in `node[2]` to `node[1]`. The function does not return anything. The annotations mention the input parameters and tree structure but don't accurately reflect the calculation and assignment operations performed by the function.

