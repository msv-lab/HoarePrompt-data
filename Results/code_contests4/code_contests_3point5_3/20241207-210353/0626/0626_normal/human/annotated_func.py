#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5.**
def func_1(n):
    return [raw_input().strip() for i in range(n)]
    #The program returns a list of n strings inputted by the user, where n is an integer between 2 and 10^5
#Overall this is what the function does:The function func_1 accepts an integer n between 2 and 10^5 as a parameter. It then prompts the user for n inputs and returns a list containing these n strings. The function accurately captures the user input as strings and returns them in a list, adhering to the specified input range.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8, and xi, yi are integers such that 1 <= xi, yi <= n and xi != yi.
def func_2():
    return raw_input().strip()
    #The program returns the input after stripping any leading or trailing whitespaces.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an input and returns the input after stripping any leading or trailing whitespaces. The function does not handle any error cases or invalid inputs.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. The list a contains n integers where each integer ai (0 <= ai <= 10^8) represents the number of apples in the vertex i. The input tree has n - 1 edges connecting the vertices.**
def func_3():
    return map(int, func_2().split())
    #The program returns a map object with integers after splitting the output of func_2()
#Overall this is what the function does:The function func_3 does not explicitly take any parameters but internally calls func_2 to get a string of integers, splits that string, converts the elements to integers, and returns a map object containing those integers. The function assumes that func_2 returns a string with space-separated integers. It does not handle any exceptions or edge cases related to the input data or the map object.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. The list of integers a contains n elements where each element ai is an integer such that 0 <= ai <= 10^8. The input tree edges are represented as pairs of integers xi, yi where 1 <= xi, yi <= n and xi != yi. Vertex 1 is the root of the tree.
def func_4():
    return func_3()[0]
    #The program returns the first element of the result of function func_3()
#Overall this is what the function does:The function `func_4` does not accept any parameters. It calls another function `func_3` and returns the first element of the result returned by `func_3`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, and ai are integers such that 0 <= ai <= 10^8 for 1 <= i <= n.**
def func_5(o):
    print(o)
#Overall this is what the function does:The function `func_5` accepts an integer `n` within the range 2 <= n <= 10^5, and a list `o` containing integers ai within the range 0 <= ai <= 10^8 for 1 <= i <= n. It simply prints the input parameter `o` provided to the function. The function does not have a specific return value.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, a is a list of n integers where 0 <= ai <= 10^8, a1 to an represent the number of apples in each vertex, and b is a list of (n-1) tuples representing the tree edges. Each tuple consists of two integers xi and yi where 1 <= xi, yi <= n and xi != yi.**
def func_6(a, b):
    while b != 0:
        a %= b
        
        a, b = b, a
        
    #State of the program after the loop has been executed: `a` is a list of n integers, `b` is a list of (n-1) tuples representing tree edges, the loop control variable `b` is 0
    return a
    #The program returns the list of n integers 'a'
#Overall this is what the function does:The function func_6 accepts a list of n integers 'a' and a list of (n-1) tuples 'b'. It then performs a series of operations on 'a' and 'b' within a while loop. The function calculates the modulus of 'a' with 'b', swaps the values of 'a' and 'b', and continues this process until 'b' becomes 0. Finally, the function returns the modified list of n integers 'a'. However, the functionality described in the annotations might not be accurate as the code performs operations with 'a' and 'b' but the purpose behind these operations is not explicitly stated.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 105. a is a list of n integers where 0 <= ai <= 10^8. The input forms a valid rooted tree with n vertices and n-1 edges.**
def func_7(a, b):
    return a / func_6(a, b) * b
    #The program returns the result of dividing the list 'a' by the result of calling function 'func_6' with arguments 'a' and 'b', and then multiplying the result by 'b'
#Overall this is what the function does:The function func_7 accepts a list 'a' of n integers and an integer 'b'. It then divides the elements in 'a' by the result of calling func_6 with 'a' and 'b', and multiplies the result by 'b' to return the final value. The function assumes 'a' is a valid list and does not handle potential division by zero errors or other edge cases.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. ai is an integer such that 0 <= ai <= 10^8. Each non-leaf vertex has 0 apples. xi and yi are integers representing vertices connected by an edge, such that 1 <= xi, yi <= n and xi ≠ yi. Vertex 1 is the root.**
def func_8(node, parent):
    ii = -1
    for i in range(len(node[2])):
        if node[2][i] != parent:
            func_8(node[2][i], node)
        else:
            ii = i
        
    #State of the program after the  for loop has been executed: n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8, each non-leaf vertex has 0 apples, xi and yi are integers representing vertices connected by an edge, vertex 1 is the root, ii is either -1 or 0, for the loop to execute len(node[2]) is greater than 0, i is the last index of node[2]. If node[2][i] is not equal to parent, then ii is -1. If node[2][i] is equal to parent, then ii is 0. The program state remains unchanged after the execution of the if else block, ii is assigned the value of i.
    if (ii >= 0) :
        node[2].pop(ii)
    #State of the program after the if block has been executed: *n is an integer such that 2 <= n <= 10^5, ai is an integer such that 0 <= ai <= 10^8, each non-leaf vertex has 0 apples, xi and yi are integers representing vertices connected by an edge, vertex 1 is the root, ii is either -1 or 0, for the loop to execute len(node[2]) is greater than 0, i is the last index of node[2]. If node[2][i] is not equal to parent, then ii is -1. If node[2][i] is equal to parent, then ii is 0. The program state remains unchanged after the execution of the if else block, ii is assigned the value of i. Additionally, ii is greater than or equal to 0
#Overall this is what the function does:The function `func_8` recursively processes a tree structure where each node has a list of children vertices. It iterates through the children vertices, removing the parent vertex if found. The function does not return any specific value.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. The list of integers a1, a2, ..., an contains n integers where 0 <= ai <= 10^8. The tree edges are described by n - 1 pairs of integers xi, yi such that 1 <= xi, yi <= n and xi ≠ yi. Vertex 1 is the root.**
def func_9(node):
    if (node[1] >= 0) :
        return
        #The program does not return anything
    #State of the program after the if block has been executed: *n is an integer such that 2 <= n <= 10^5. The list of integers a1, a2, ..., an contains n integers where 0 <= ai <= 10^8. The tree edges are described by n - 1 pairs of integers xi, yi such that 1 <= xi, yi <= n and xi ≠ yi. Vertex 1 is the root. node[1] is less than 0.
    lcm = 1
    max = -1
    for child in node[2]:
        func_9(child)
        
        lcm = func_7(lcm, child[0])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= n <= 10^5, the list of integers a1, a2, ..., an contains n integers where 0 <= ai <= 10^8, the tree edges are described by n - 1 pairs of integers xi, yi such that 1 <= xi, yi <= n and xi ≠ yi, vertex 1 is the root, node[1] is less than 0, `lcm` is the least common multiple of all the children nodes of node 2, `max` is -1
    for child in node[2]:
        t = child[1] / lcm * lcm
        
        if max < 0 or max > t:
            max = t
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, `max` will hold the maximum value calculated for `t` satisfying the specified conditions. The loop will update `max` based on the comparison with `t` for each child node of node 2. The loop will iterate over all the child nodes, and `t` will be calculated for each iteration using the formula provided.
    node[0] = lcm
    node[1] = max * len(node[2])
#Overall this is what the function does:The function func_9 accepts a parameter node representing a node in a tree structure. It calculates the least common multiple of all the children nodes of node 2 and the maximum value obtained by dividing the second element of each child node by the least common multiple. The function then updates the first and second elements of the input node accordingly. However, the annotations suggest that the function does not return anything, which is not accurate as the code performs calculations and updates the input node. It is important to note that the function does not explicitly return a value but modifies the input node in place.

