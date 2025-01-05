#State of the program right berfore the function call: n and m are integers such that 1 <= n <= 10^5, 0 <= m <= min((n(n-1))/(2),10^5).**
def func_1():
    n, m = func_4()
    p = list(range(n))
    r = func_7(int, n)
    sg = func_7(set, n)
    for _ in range(m):
        x, y = func_5(-1)
        
        sg[x].add(y)
        
        sg[y].add(x)
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers such that 1 <= n <= 10^5, 0 <= m <= min((n(n-1))/(2),10^5; `p` is a list containing elements from 0 to n-1, `sg` is the value returned by calling the function `func_7` with arguments `set` and `n. The loop will execute `m` times, and after all iterations, `sg` will contain the updated sets after adding corresponding `y` values to `x` sets and vice versa from the function `func_5(-1)`
    v = min(range(n), key=lambda i: len(sg[i]))
    for i in range(n):
        if i not in sg[v]:
            union(i, v)
        else:
            for j in range(n):
                if j not in sg[i]:
                    union(i, j)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `n`, `m`, `p`, `sg`, and `v` have been updated based on the conditions within the loop. If `i` is not in the set at index `v` in `sg`, then all variables remain the same except the set at index `v` in `sg` is updated by adding the set at index `i` to it. If `i` is in the set at index `v` in `sg`, then all elements in `sg[i]` are unioned with `i`.
    roots = set()
    for i in range(n):
        roots.add(find(i))
        
    #State of the program after the  for loop has been executed: `roots` contains the result of `find(i)` for each `i` in the range of `n`, where `n` is a non-negative integer
    print(len(roots) - 1)
#Overall this is what the function does:The function does not accept any parameters. It calculates and prints the maximum number of edges in a graph with `n` nodes and `m` connected components based on the given constraints. It initializes values, forms sets, updates sets based on input, finds the node with the minimum connections, performs unions on sets, finds roots, and finally prints the result by counting the number of unique roots minus 1. The code lacks clarity on the functions `func_4`, `func_5`, `func_7`, `union`, and `find`, which are used but not defined within the provided code. Additionally, the purpose of the `print` statement at the end is unclear.

#State of the program right berfore the function call: 
def find(v):
    vc = v
    while v != p[v]:
        v = p[v]
        
    #State of the program after the loop has been executed: `vc` is assigned the value of `v`, `v` is equal to `p[v]` after all iterations of the loop have executed
    while vc != v:
        p[vc], vc = v, p[vc]
        
    #State of the program after the loop has been executed: `vc` is equal to `p[p[v]]`, `v` remains unchanged
    return v
    #The program returns the value of variable 'v' without any changes
#Overall this is what the function does:The function accepts a parameter `v`, assigns the value of `v` to `vc`, and then iterates through a loop to update the values of `v` and `vc` based on the values in array `p`. Finally, it returns the updated value of `v` without any changes.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.**
def union(u, v):
    u, v = find(u), find(v)
    if (u == v) :
        return
        #The program returns the value of u or v, which are equal
    #State of the program after the if block has been executed: *n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i. The values of u and v are not equal.
    if (r[u] < r[v]) :
        u, v = v, u
    #State of the program after the if block has been executed: *n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i. The values of u and v are not equal. If r[u] < r[v], then u holds the initial value of v and v holds the initial value of u.
    p[u] = v
    if (r[u] == r[v]) :
        r[u] += 1
    #State of the program after the if block has been executed: *p[u] is assigned the value of v, r[u] and r[v] are equal. After the execution, p[u] will be equal to v and r[u] will be incremented by 1 if r[u] is equal to r[v].
#Overall this is what the function does:The function `union` takes two integer parameters `u` and `v`, finds their respective roots using the `find` function, and performs union operation on them. If the roots of `u` and `v` are equal, the function returns without performing any further action. If the rank of the root of `u` is less than the rank of the root of `v`, the function swaps `u` and `v`. Then, it updates the parent array `p` by setting the parent of `u` to `v`. If the ranks of the roots `u` and `v` are equal, the rank of `u` is incremented by 1. The function does not handle the case where the roots of `u` and `v` are not equal, which might be a missing edge case.

#State of the program right berfore the function call: **
def func_2(x):
    return pow(x, MOD - 2, MOD)
    #The program returns the result of calculating x raised to the power of MOD - 2, modulo MOD
#Overall this is what the function does:The function `func_2` accepts an integer parameter `x` and returns the result of calculating x raised to the power of MOD - 2, modulo MOD.

#State of the program right berfore the function call: x and y are integers such that 1 ≤ x ≤ 10^5, 0 ≤ y ≤ min((x(x-1))/(2),10^5).**
def func_3(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` and `y` are updated integers satisfying the given conditions where `y` is 0, indicating the loop has finished executing.
    return x
    #The program returns the updated integer value of 'x' after the loop has finished executing. The value of 'y' is 0, indicating the loop has finished.
#Overall this is what the function does:The function func_3 accepts two parameters, x and y, where x is an integer between 1 and 10^5, and y is an integer between 0 and min((x(x-1))/(2),10^5). The function then updates the values of x and y based on a loop until y becomes 0. Finally, it returns the updated integer value of x after the loop has finished executing. If the loop does not properly update x and y according to the annotations, the functionality should reflect the actual behavior of the code.

#State of the program right berfore the function call: n and m are non-negative integers such that 1 ≤ n ≤ 10^5 and 0 ≤ m ≤ min((n(n-1))/(2),10^5).**
def func_4():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by mapping the input values
#Overall this is what the function does:The function func_4 does not accept any explicit parameters. It reads input values from the user, maps them to integers, and returns a list of these integers. The code does not enforce the constraints specified for n and m in the annotations, potentially allowing input values outside the specified ranges.

#State of the program right berfore the function call: **
def func_5(o):
    return list(map(lambda x: int(x) + o, input().split()))
    #The program returns a list of integers obtained by adding 0 to each element of the input list after converting them to integers
#Overall this is what the function does:The function accepts a list `o`, converts the elements to integers, and returns a new list with 0 added to each element. The code does exactly what the annotations describe, converting each element of the input list to an integer and adding 0 to it before returning the new list.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ m ≤ min((n(n-1))/(2),10^5).**
def func_6(n, m):
    return [func_4() for _ in range(n)]
    #The program returns a list of length n, where each element is the result of the function func_4() called in a loop n times
#Overall this is what the function does:The function `func_6` accepts two parameters `n` and `m`, both of which are integers satisfying the constraints 1 ≤ n ≤ 10^5 and 0 ≤ m ≤ min((n(n-1))/(2),10^5). The function returns a list of length n, where each element is the result of calling the function `func_4()` in a loop n times.

#State of the program right berfore the function call: **
def func_7(f):
    return [func_7(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list of values obtained by calling 'func_7' with arguments from 'dim' list after the first element for a number of times specified by the first element of 'dim'. If 'dim' is empty, then the program returns the result of calling 'f'.
#Overall this is what the function does:The function `func_7` accepts a parameter `f`, which represents a function. It also expects a list `dim` as input. If the `dim` list is empty, the function returns the result of calling the function `f`. If the `dim` list is not empty, the function calls the function `f` with arguments from the `dim` list after the first element for a number of times specified by the first element of the `dim` list, and returns a list of values obtained from these function calls.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i.**
def func_8(start, step, count):
    return range(start, start + step * count, step)
    #The program returns a range starting from 'start' with a step size of 'step' and 'count' number of elements
#Overall this is what the function does:The function `func_8` accepts three parameters: `start`, `step`, and `count`, which are integers. It returns a range starting from `start` with a step size of `step` and containing `count` number of elements. The function generates a range based on the input parameters.

#State of the program right berfore the function call: l is a list of tuples where each tuple contains two integers representing the endpoints of an edge in the graph. start and end are integers representing the start and end vertices of the graph.**
def func_9(l, start, end):
    return range(start, len(l) + end)
    #The program returns a range starting from the 'start' vertex to the end of the list 'l' plus the 'end' vertex.
#Overall this is what the function does:The function func_9 accepts a list of tuples 'l' representing edges in a graph, as well as start and end vertices. It returns a range starting from the 'start' vertex to the end of the list 'l' plus the 'end' vertex. One potential issue is that the code does not handle cases where 'start' or 'end' are out of bounds compared to the length of the list 'l'. It also does not consider cases where 'start' is greater than 'end'.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the graph.**
def func_10(n):
    """ [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] """
    return 2 ** (n - 1).bit_length()
    #The program returns the position of the highest set bit in the binary representation of 2 raised to the power of (n - 1)
#Overall this is what the function does:The function accepts a positive integer n, representing the number of vertices in a graph, and returns the position of the highest set bit in the binary representation of 2 raised to the power of (n - 1). The function correctly calculates the position of the highest set bit as described in the code.

#State of the program right berfore the function call: **
def func_11(x, r):
    """ = ceil(x / r) """
    return (x + r - 1) // r
    #The program returns the value of `(x + r - 1) // r` where `x` and `r` are known variables.
#Overall this is what the function does:The function func_11 calculates the ceiling value of the division of x by r. It accepts two known variables x and r, and returns the result of the expression (x + r - 1) // r, which represents the ceiling value of x divided by r.

