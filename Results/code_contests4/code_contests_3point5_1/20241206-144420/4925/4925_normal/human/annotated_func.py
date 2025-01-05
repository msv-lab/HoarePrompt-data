#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5).**
def func_1():
    n, m = func_4()
    p = list(range(n))
    r = func_7(int, n)
    sg = func_7(set, n)
    for _ in range(m):
        x, y = func_5(-1)
        
        sg[x].add(y)
        
        sg[y].add(x)
        
    #State of the program after the  for loop has been executed: n and m are integers satisfying 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5); p is a list containing integers from 0 to n-1; sg is a list of sets where sg[i] contains all elements that have been added to sg at index i
    v = min(range(n), key=lambda i: len(sg[i]))
    for i in range(n):
        if i not in sg[v]:
            union(i, v)
        else:
            for j in range(n):
                if j not in sg[i]:
                    union(i, j)
        
    #State of the program after the  for loop has been executed: n and m are integers satisfying 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5); p is a list containing integers from 0 to n-1; sg is a list of sets where sg[i] contains all elements that have been added to sg at index i; v is the index with the minimum length of the set in sg. After all iterations of the loop have finished, the sets in sg will be merged and updated according to the union(i, j) function. All elements will be present in sg as per the function's logic. All other variables will remain unchanged.
    roots = set()
    for i in range(n):
        roots.add(find(i))
        
    #State of the program after the  for loop has been executed: `v` is the index with the minimum length of the set in sg, `roots` contains the result of calling find(i) for all i in the range of n, `p` is a list containing integers from 0 to n-1, `n` is greater than or equal to 1
    print(len(roots) - 1)
#Overall this is what the function does:The function `func_1` initializes variables based on the output of other functions and processes them to find the set with the minimum length, then merges sets based on certain conditions. It calculates the number of unique roots found and outputs the count minus one. The function does not accept any parameters and does not return any value.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and no edge appears twice in the input.**
def find(v):
    vc = v
    while v != p[v]:
        v = p[v]
        
    #State of the program after the loop has been executed: `vc` is assigned the value of the root node that `v` belongs to after all iterations have executed, `v` is updated to the root node of the current node it is pointing to
    while vc != v:
        p[vc], vc = v, p[vc]
        
    #State of the program after the loop has been executed: `vc` is now equal to the root node that `v` is pointing to after all iterations have executed, `v` is updated to the root node of the current node it is pointing to, `p` is updated accordingly
    return v
    #The program returns the root node that variable `v` is pointing to after all iterations have executed. Variable `v` is updated to the root node of the current node it is pointing to, and variable `p` is updated accordingly.
#Overall this is what the function does:The function `find` accepts a parameter `v` that represents a node in a graph. It iteratively finds and updates `v` to point to the root node it belongs to, and returns the root node. The variable `p` is also updated during the process. However, there is a missing edge case where the function does not handle the scenario when `v` is not a valid node index.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i.**
def union(u, v):
    u, v = find(u), find(v)
    if (u == v) :
        return
        #The program returns u which is equal to v
    #State of the program after the if block has been executed: *n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i. The values of u and v are not equal.
    if (r[u] < r[v]) :
        u, v = v, u
    #State of the program after the if block has been executed: *n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i. The values of u and v are not equal. If r[u] < r[v], then the values of u and v are swapped.
    p[u] = v
    if (r[u] == r[v]) :
        r[u] += 1
    #State of the program after the if block has been executed: *`n` and `m` are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). `a_i` and `b_i` are integers such that 1 ≤ `a_i`, `b_i` ≤ n, `a_i` ≠ `b_i`. The values of `u` and `v` are not equal. If `r[u]` < `r[v]`, then the values of `u` and `v` are swapped. `p[u]` is assigned the value `v`. After the execution of the if else block, if `r[u]` is equal to `r[v]`, then `r[u]` is incremented by 1.
#Overall this is what the function does:The function `union` accepts two integer parameters `u` and `v`. It checks if `u` is equal to `v` and returns `u`. If `u` is not equal to `v`, it swaps the values of `u` and `v` based on the conditions specified. The functionality of the function is to perform the union operation on the input integers `u` and `v`.

#State of the program right berfore the function call: **
def func_2(x):
    return pow(x, MOD - 2, MOD)
    #The program returns the result of raising 'x' to the power of (MOD - 2) modulo MOD
#Overall this is what the function does:The function accepts a parameter x and calculates the result of raising 'x' to the power of (MOD - 2) modulo MOD, returning the result.

#State of the program right berfore the function call: x and y are integers such that 1 <= x <= 10^5 and 0 <= y <= min((x(x-1))/2, 10^5).**
def func_3(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: 'x' and 'y' have new values based on the initial conditions, 'y' is 0 as it becomes falsy after the loop finishes
    return x
    #The program returns the final value of 'x' after the loop finishes. 'y' becomes 0 after the loop.
#Overall this is what the function does:The function func_3 accepts two integers x and y, where x is between 1 and 10^5, and y is between 0 and min((x(x-1))/2, 10^5). It then performs a loop to update the values of x and y until y becomes 0. Finally, it returns the final value of x after the loop finishes.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5).**
def func_4():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by splitting the input and converting each element to an integer.
#Overall this is what the function does:The function does not accept any parameters and returns a list of integers obtained by splitting the input and converting each element to an integer. The program assumes the input consists of space-separated integers. It does not consider any error handling or validation of the input data.

#State of the program right berfore the function call: **
def func_5(o):
    return list(map(lambda x: int(x) + o, input().split()))
    #The program returns a list of integers obtained by adding 0 to each element after converting it to an integer from the input string split by spaces.
#Overall this is what the function does:The function accepts a parameter `o`, converts each element in the input string to an integer, adds `o` to each integer, and returns a list of these modified integers. The function does not handle any potential errors or edge cases related to input validation or unexpected input types.

#State of the program right berfore the function call: n and m are non-negative integers such that 1 ≤ n ≤ 10^5 and 0 ≤ m ≤ min((n(n-1))/(2),10^5).**
def func_6(n, m):
    return [func_4() for _ in range(n)]
    #The program returns a list of length 'n', where each element is the result of calling the function func_4(). The values of 'n' and 'm' are non-negative integers such that 1 ≤ n ≤ 10^5 and 0 ≤ m ≤ min((n(n-1))/(2),10^5).
#Overall this is what the function does:The function func_6 accepts two non-negative integers n and m, and then returns a list of length 'n' where each element is the result of calling the function func_4(). The values of 'n' and 'm' are constrained to be non-negative integers such that 1 ≤ n ≤ 10^5 and 0 ≤ m ≤ min((n(n-1))/(2),10^5).

#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). The input edges are distinct pairs of integers a_i and b_i where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.**
def func_7(f):
    return [func_7(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list of values generated by calling func_7 with arguments f and the remaining dimensions of dim for each element in the range of dim[0], or the result of calling f if dim is empty.
#Overall this is what the function does:The function func_7 accepts a parameter `f` and returns a list of values generated by calling func_7 with arguments `f` and the remaining dimensions of `dim` for each element in the range of `dim[0]`. If `dim` is empty, it returns the result of calling `f`. The function is intended to handle recursion with the given parameters, but there is a missing implementation for the variable `dim` which may cause unexpected behavior or errors.

#State of the program right berfore the function call: n and m are integers such that 1 <= n <= 10^5, 0 <= m <= min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 <= a_i, b_i <= n and a_i ≠ b_i.**
def func_8(start, step, count):
    return range(start, start + step * count, step)
    #The program returns a range starting from 'start' with a step size of 'step' and containing 'count' elements
#Overall this is what the function does:The function func_8 accepts three parameters: start, step, and count, where start is the starting point of the range, step is the step size between elements, and count is the total number of elements in the range. The function then returns a range starting from start with the specified step size and containing the specified count of elements.

#State of the program right berfore the function call: l is a list of tuples where each tuple contains two integers representing the endpoints of an edge in the graph. start and end are integers representing the start and end vertices of the graph. 1 <= start, end <= n, where n is the number of vertices in the graph.**
def func_9(l, start, end):
    return range(start, len(l) + end)
    #The program returns a range starting from 'start' to the length of list 'l' plus 'end'. The range represents the vertices of the graph.
#Overall this is what the function does:The function func_9 accepts a list of tuples 'l' representing edges in a graph, along with start and end vertices. It returns a range starting from the 'start' vertex to the length of list 'l' plus the 'end' vertex. This range represents the vertices of the graph. However, there is a discrepancy between the annotation and the code. The code actually returns a range starting from 'start' to the length of list 'l' plus 'end', which may not accurately represent the vertices of the graph as described in the annotation. It is also unclear how the list of tuples 'l' is utilized in determining the range of vertices.

#State of the program right berfore the function call: **
def func_10(n):
    """ [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] """
    return 2 ** (n - 1).bit_length()
    #The program returns the value of 2 raised to the power of (n - 1), where n is the length of the list [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] minus 1
#Overall this is what the function does:The function func_10 accepts a parameter n and returns the value of 2 raised to the power of (n - 1), where n is the length of the list [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] minus 1.

#State of the program right berfore the function call: x and r are integers such that 1 <= x <= 10^5 and 0 <= r <= min((x(x-1))/2,10^5).**
def func_11(x, r):
    """ = ceil(x / r) """
    return (x + r - 1) // r
    #The program returns the value of (x + r - 1) divided by r, where x and r are integers such that 1 <= x <= 10^5 and 0 <= r <= min((x(x-1))/2,10^5). If the empty string is assigned, it is the ceiling value of x divided by r.
#Overall this is what the function does:The function func_11 accepts two integers x and r within the specified constraints of 1 <= x <= 10^5 and 0 <= r <= min((x(x-1))/2,10^5). It calculates the ceiling value of the division of (x + r - 1) by r and returns the result. The function accurately handles cases where the division does not result in an integer by returning the ceiling value.

