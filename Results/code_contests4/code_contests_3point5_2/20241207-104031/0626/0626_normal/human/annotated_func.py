#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5.**
def func_1(n):
    return [raw_input().strip() for i in range(n)]
    #The program returns a list of n strings after stripping any leading or trailing whitespaces entered by the user for each string in the list.
#Overall this is what the function does:The function func_1 accepts an integer n between 2 and 10^5 as a parameter. It then prompts the user n times to input a string and returns a list of n strings after stripping any leading or trailing whitespaces from each input string. The function does not handle any exceptions related to user input errors such as empty strings or non-string inputs.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. The list of integers a1, a2, ..., an is of length n and each ai is an integer such that 0 <= ai <= 10^8. The tree edges are given as pairs of integers xi, yi where 1 <= xi, yi <= n and xi != yi.**
def func_2():
    return raw_input().strip()
    #The program returns the input string after stripping any leading or trailing whitespaces
#Overall this is what the function does:The function does not accept any parameters and simply returns the input string after removing any leading or trailing whitespaces.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. ai is an integer such that 0 <= ai <= 10^8.**
def func_3():
    return map(int, func_2().split())
    #The program returns a map object containing integers after splitting the result of func_2()
#Overall this is what the function does:The function func_3 does not accept any parameters. It calls func_2, splits the result, and returns a map object containing integers. The code does not specify any handling for exceptions that might arise from calling func_2 or splitting the result, which could potentially lead to errors if the result is not in the expected format.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8 for each 1 <= i <= n, and xi, yi are integers such that 1 <= xi, yi <= n and xi != yi.**
def func_4():
    return func_3()[0]
    #The program returns the first element of the result of calling the function func_3()
#Overall this is what the function does:The function func_4 calls func_3 and returns the first element of the result. The annotations mention specific constraints on the input parameters, but the function itself does not take any parameters and relies on the output of func_3. It does not handle any edge cases or additional logic beyond calling func_3 and returning the first element of its result.

#State of the program right berfore the function call: o is a tuple of an integer n followed by a list of n integers representing the number of apples in each vertex of the tree, followed by n-1 tuples of two integers representing the edges in the tree.
def func_5(o):
    print(o)
#Overall this is what the function does:The function `func_5` accepts a parameter `o`, which is a tuple consisting of an integer `n`, followed by a list of `n` integers representing the number of apples in each vertex of the tree, and then followed by `n-1` tuples of two integers representing the edges in the tree. The function simply prints the input tuple `o` and does not have any specific return value mentioned.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. a is a list of n integers where each element ai is an integer such that 0 <= ai <= 10^8.**
def func_6(a, b):
    while b != 0:
        a %= b
        
        a, b = b, a
        
    #State of the program after the loop has been executed: `n` is an integer such that 2 <= n <= 10^5, `a` is a list of n integers modified after all iterations of the loop, `b` is 0 after all iterations
    return a
    #The program returns the list 'a' of n integers modified after all iterations of the loop
#Overall this is what the function does:The function `func_6` accepts a list of integers `a` and another unspecified parameter `b`. It then performs a series of operations on `a` and `b` within a loop. After all iterations of the loop, the function returns the modified list `a` of integers. The function implements a specific algorithm that involves modifying the list `a` based on the values of `a` and `b` during each iteration of the loop. It is crucial to note that the function swaps the values of `a` and `b` in each iteration, which is a key aspect of the algorithm.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, and ai is an integer such that 0 <= ai <= 10^8 for 1 <= i <= n.**
def func_7(a, b):
    return a / func_6(a, b) * b
    #The program returns the result of dividing variable 'a' by the return value of function func_6(a, b), multiplied by variable 'b'.
#Overall this is what the function does:The function `func_7` accepts two parameters, `a` and `b`, where `a` and `b` are integers. The function calculates the result of dividing `a` by the return value of function `func_6(a, b)` and then multiplies the result by `b`. The function returns this final calculated value.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, and ai is an integer such that 0 <= ai <= 10^8 for i = 1 to n. The input forms a valid rooted tree structure.**
def func_8(node, parent):
    ii = -1
    for i in range(len(node[2])):
        if node[2][i] != parent:
            func_8(node[2][i], node)
        else:
            ii = i
        
    #State of the program after the  for loop has been executed: n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8 for i = 1 to n forming a valid rooted tree structure, ii is an integer value representing the last index where `node[2][i]` is equal to the parent.
    if (ii >= 0) :
        node[2].pop(ii)
    #State of the program after the if block has been executed: *n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8 for i = 1 to n forming a valid rooted tree structure, ii is an integer value representing the last index where `node[2][i]` is equal to the parent. If ii >= 0, all the conditions mentioned hold true.
#Overall this is what the function does:The function `func_8` traverses a rooted tree structure represented by nodes and parents. It iterates through the children of a node, and if a child is not the parent node, it recursively calls itself on that child. If a child is the parent node, it removes that child from the list of children. The function does not return any specific value, and the postconditions do not provide information on what happens if ii is negative, potentially missing a condition where ii is negative.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. ai is an integer such that 0 <= ai <= 10^8. xi and yi are integers such that 1 <= xi, yi <= n and xi != yi.
def func_9(node):
    if (node[1] >= 0) :
        return
        #The program does not perform any operations and returns nothing
    #State of the program after the if block has been executed: *n is an integer such that 2 <= n <= 10^5. ai is an integer such that 0 <= ai <= 10^8. xi and yi are integers such that 1 <= xi, yi <= n and xi != yi. node[1] is less than 0
    lcm = 1
    max = -1
    for child in node[2]:
        func_9(child)
        
        lcm = func_7(lcm, child[0])
        
    #State of the program after the  for loop has been executed: lcm is updated by calling func_7 with parameters lcm and the last child in node[2], max is -1
    for child in node[2]:
        t = child[1] / lcm * lcm
        
        if max < 0 or max > t:
            max = t
        
    #State of the program after the  for loop has been executed: `lcm` is updated by calling func_7 with parameters `lcm` and the last child in node[2], `max` is the maximum value of `t` calculated in each iteration of the loop, `child` is the last child in node[2], `t` is the result of dividing the second element of `child` by `lcm` and then multiplying by `lcm`.
    node[0] = lcm
    node[1] = max * len(node[2])
#Overall this is what the function does:The function func_9 accepts a parameter `node`, where n is an integer between 2 and 10^5, ai is an integer between 0 and 10^8, and xi, yi are integers between 1 and n (xi != yi). However, the function does not perform any operations as indicated in the annotations, returning nothing. The code does not execute any logic beyond the initial if statement check.

