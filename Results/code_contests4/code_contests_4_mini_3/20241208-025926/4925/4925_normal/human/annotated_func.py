#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph (1 ≤ n ≤ 10^5), m is an integer representing the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2),10^5)), and for each of the m edges, a_i and b_i are integers (1 ≤ a_i, b_i ≤ n) representing the endpoints of the edge, with a_i ≠ b_i.
def func_1():
    n, m = func_4()
    p = list(range(n))
    r = func_7(int, n)
    sg = func_7(set, n)
    for _ in range(m):
        x, y = func_5(-1)
        
        sg[x].add(y)
        
        sg[y].add(x)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `m` is the number of edges added, `p` is a list containing integers from 0 to `n-1`, `sg` is a list of sets where each set contains the vertices connected by edges, reflecting all connections established from the loop's executions.
    v = min(range(n), key=lambda i: len(sg[i]))
    for i in range(n):
        if i not in sg[v]:
            union(i, v)
        else:
            for j in range(n):
                if j not in sg[i]:
                    union(i, j)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `sg` contains the updated connections based on the union operations, `v` is the index of the vertex with the minimum number of connections in the modified `sg`.
    roots = set()
    for i in range(n):
        roots.add(find(i))
        
    #State of the program after the  for loop has been executed: `roots` is a set containing the unique results of `find(i)` for all integers `i` from 0 to `n-1`, `n` is a non-negative integer.
    print(len(roots) - 1)
#Overall this is what the function does:The function processes a graph defined by `n` vertices and `m` edges, creating a union of connected components. It calculates the number of connected components in the graph and prints the count of these components minus one. The function does not accept parameters directly but relies on external function calls to initialize the graph structure. It assumes valid input ranges for `n` and `m`. If there are no edges, it will create a fully disconnected graph, resulting in `n-1` components.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the graph (1 ≤ n ≤ 10^5), m is a non-negative integer representing the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2),10^5)), and the input consists of m pairs of integers (a_i, b_i) where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i, indicating the endpoints of edges with weight 1.
def find(v):
    vc = v
    while v != p[v]:
        v = p[v]
        
    #State of the program after the loop has been executed: `n` is a positive integer, `m` is a non-negative integer, `v` is equal to the value that p points to for the original value of `v` such that `v` is now equal to a representative or root in the structure defined by `p`, and `p[v]` is equal to `v`.
    while vc != v:
        p[vc], vc = v, p[vc]
        
    #State of the program after the loop has been executed: `n` is a positive integer, `m` is a non-negative integer, `v` is equal to the representative or root in the structure defined by `p`, and `vc` is equal to `v` after all iterations of the loop. After the loop, `vc` is equal to a value that points to `v`, and `p[vc]` is equal to `v`, indicating that `vc` has reached the representative of the structure.
    return v
    #The program returns the representative or root value 'v' from the structure defined by 'p'
#Overall this is what the function does:The function accepts an integer `v` representing a vertex in a disjoint set structure and returns the representative or root value of that vertex from the structure defined by the array `p`. The function implements path compression to optimize future queries by updating the parent of nodes along the path to point directly to the root.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph (1 ≤ n ≤ 10^5), m is an integer representing the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2),10^5)), and each edge is defined by two distinct integers a_i and b_i (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i) for 1 ≤ i ≤ m.
def union(u, v):
    u, v = find(u), find(v)
    if (u == v) :
        return
        #The program returns None, as there is no value specified to return.
    #State of the program after the if block has been executed: *`u` and `v` are assigned the values returned from the function `find(u)` and `find(v)`, respectively. `u` is not equal to `v`.
    if (r[u] < r[v]) :
        u, v = v, u
    #State of the program after the if block has been executed: *`u` and `v` are assigned the values returned from the function `find(u)` and `find(v)`, respectively; `u` is not equal to `v`; the value of `r` at index `u` is less than the value of `r` at index `v`. However, after execution, `u` takes the value of `v` and `v` takes the value of `u`, resulting in a contradiction as `u` becomes equal to `v`, violating the precondition that `u` is not equal to `v`.
    p[u] = v
    if (r[u] == r[v]) :
        r[u] += 1
    #State of the program after the if block has been executed: *`u` and `v` are assigned values returned from `find(u)` and `find(v)`, respectively, with `u` not equal to `v`. If `r[u]` equals `r[v]`, then `r[u]` is incremented by 1, leading to a contradiction as `p[u]` is assigned the value of `v`, which would violate the precondition that `u` is not equal to `v`.
#Overall this is what the function does:The function `union` accepts two integer parameters `u` and `v`, which represent vertices in a graph. It attempts to unite the sets containing these vertices based on their roots, updating a parent array `p` and a rank array `r`. However, if `u` and `v` are already in the same set (i.e., their roots are equal), the function returns None and does not perform any union operation. There is an implicit assumption that `find(u)` and `find(v)` return valid indices, and if the ranks of `u` and `v` are equal, the rank of `u` is incremented, which could lead to a logical inconsistency. The function does not return any value.

#State of the program right berfore the function call: x is a tuple containing two integers n and m, where n is the number of vertices (1 ≤ n ≤ 10^5) and m is the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2), 10^5)). Following this, there are m pairs of integers (a_i, b_i) representing the endpoints of the edges with weight 1, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_2(x):
    return pow(x, MOD - 2, MOD)
    #The program returns the modular inverse of the tuple x under modulo MOD
#Overall this is what the function does:The function accepts a tuple `x`, which contains two integers representing the number of vertices `n` and the number of edges `m`. It returns the modular inverse of `x` under a predefined modulo `MOD`. However, it does not check if `x` is valid for modular inversion, such as ensuring that `x` is not zero or does not lead to a division by zero error.

#State of the program right berfore the function call: x is an integer representing the number of vertices in the graph (1 ≤ x ≤ 10^5), and y is an integer representing the number of edges with weight 1 (0 ≤ y ≤ min((x(x-1))/(2), 10^5)).
def func_3(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `y` is 0, `x` is the greatest common divisor (GCD) of the original values of `x` and `y`.
    return x
    #The program returns the greatest common divisor (GCD) of the original values of x and y, where y is 0. Since the GCD of any number and 0 is the number itself, it returns the value of x.
#Overall this is what the function does:The function accepts two integer parameters `x` and `y`, representing the number of vertices and edges in a graph, respectively. It calculates and returns the greatest common divisor (GCD) of the original values of `x` and `y`. If `y` is initially zero, the function will return the value of `x` as the GCD. The function handles the case where `y` is zero correctly, but there are no explicit checks or handling for cases where `x` or `y` might be negative or exceed the specified bounds.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph (1 ≤ n ≤ 10^5), m is an integer representing the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2),10^5)), and for each of the next m lines, a_i and b_i are integers representing the endpoints of the edges (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i).
def func_4():
    return list(map(int, input().split()))
    #The program returns a list of integers derived from the input provided, which represents the endpoints of the edges in the graph.
#Overall this is what the function does:The function does not accept any parameters and returns a list of integers derived from the input provided. The integers represent the endpoints of the edges in a graph. However, it does not handle any validation for the input format or values, which means it could potentially return an incorrect or malformed list if the input does not meet the expected criteria (e.g., non-integer inputs or exceeding the defined limits).

#State of the program right berfore the function call: o is a tuple containing two integers n and m, where n (1 ≤ n ≤ 10^5) is the number of vertices, and m (0 ≤ m ≤ min((n(n-1))/(2),10^5)) is the number of edges with weight 1. Additionally, the following m lines contain pairs of integers (a_i, b_i) where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i, representing the endpoints of the edges with weight 1.
def func_5(o):
    return list(map(lambda x: int(x) + o, input().split()))
    #The program returns a list of integers where each integer is the sum of the respective input value and the tuple `o` containing the number of vertices and edges.
#Overall this is what the function does:The function accepts a tuple `o` containing two integers (n, m) and returns a list of integers where each integer is the sum of the respective input value and the first element of the tuple `o` (n). It takes input from the user, which is split into individual values, and each of these values is added to `n`, not the entire tuple. The function does not handle cases where the input may not be valid integers or if there are no inputs provided, which could lead to errors.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), m is a non-negative integer (0 ≤ m ≤ min((n(n-1))/(2), 10^5)), and for each of the next m lines, a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_6(n, m):
    return [func_4() for _ in range(n)]
    #The program returns a list of n elements, each being the result of func_4() called n times. The specific values of the elements depend on the implementation of func_4().
#Overall this is what the function does:The function accepts two parameters, `n` (a positive integer) and `m` (a non-negative integer). It returns a list containing `n` elements, each being the result of calling `func_4()` exactly `n` times. The specific values of the elements in the list depend entirely on the implementation of `func_4()`, which is not defined in the provided code. There are no additional conditions or logic directly pertaining to `m` in the function's execution.

#State of the program right berfore the function call: f is a callable function representing the edges of a complete undirected graph, dim is a tuple containing two integers n and m where 1 ≤ n ≤ 10^5 and 0 ≤ m ≤ min((n(n-1))/(2),10^5), followed by m pairs of integers (a_i, b_i) indicating the endpoints of the edges with weight 1, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_7(f):
    return [func_7(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list generated by calling func_7 with the second element of the tuple dim repeated dim[0] times if dim is not empty; otherwise, it returns the result of calling f()
#Overall this is what the function does:The function accepts a callable function `f` and a tuple `dim`. If `dim` contains elements, it returns a list where `func_7` is called with `f` and the second element of `dim` repeated `dim[0]` times. If `dim` is empty, it returns the result of calling `f()`. However, the expected usage of `dim` is not clear from the provided code snippet, as the variable `dim` needs to be defined in the function's scope for this logic to execute properly, which is not evident from the code. This could lead to a potential NameError if `dim` is not defined.

#State of the program right berfore the function call: start is an integer representing the number of vertices (n) in the graph, step is an integer representing the number of edges of weight 1 (m) such that 0 ≤ m ≤ min((n(n-1))/(2),10^5), and count is a list of tuples where each tuple contains two integers representing the endpoints of the edges of weight 1 (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i).
def func_8(start, step, count):
    return range(start, start + step * count, step)
    #The program returns a range starting from 'start' and extending to 'start + step * count' with an interval of 'step'
#Overall this is what the function does:The function `func_8` accepts an integer `start`, an integer `step`, and a list of tuples `count`. It returns a range starting from `start` and extending to `start + step * count` with an interval of `step`. However, there is a critical error in the code: `count` is treated as an integer representing the number of tuples in the list, but it is passed as a list. Thus, the actual implementation will raise a `TypeError` when trying to multiply `step` by `count` since `count` is not an integer. The intended behavior is to use the length of the `count` list to determine the number of steps, which is not correctly implemented. Therefore, the function fails to execute as expected.

#State of the program right berfore the function call: l is a list of tuples where each tuple contains two integers representing the endpoints of edges of weight 1 in an undirected complete graph, start and end are non-negative integers such that 0 <= start <= end <= len(l). The first element of l contains two integers n and m, where 1 ≤ n ≤ 100000 and 0 ≤ m ≤ min((n(n-1))/2, 100000).
def func_9(l, start, end):
    return range(start, len(l) + end)
    #The program returns a range from start to the length of list 'l' plus end, which is a range object representing the integers from start to len(l) + end.
#Overall this is what the function does:The function accepts a list of tuples `l` and two non-negative integers `start` and `end`, returning a range object representing integers from `start` to `len(l) + end`. The function does not validate the values of `start` and `end`, so if `start` is greater than `len(l) + end`, the resulting range will be empty. Additionally, if `start` is negative or if `end` is negative, this may lead to unintended behavior, though Python will not raise an error.

#State of the program right berfore the function call: n is an integer representing the number of vertices in a complete undirected weighted graph, where 1 ≤ n ≤ 10^5. The input also includes m, the number of edges with weight 1, satisfying 0 ≤ m ≤ min((n(n-1))/2, 10^5), and for each of the m edges, two integers a_i and b_i (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i) representing the endpoints of the edges.
def func_10(n):
    """ [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] """
    return 2 ** (n - 1).bit_length()
    #The program returns 2 raised to the power of the bit length of (n - 1), which represents the smallest power of 2 that is greater than or equal to n.
#Overall this is what the function does:The function accepts an integer `n`, and it returns the smallest power of 2 that is greater than or equal to `n`. This is done by calculating `2` raised to the power of the bit length of `(n - 1)`. The function handles the edge case where `n` is 1, returning 1, which is the expected smallest power of 2 in that case.

#State of the program right berfore the function call: x is an integer representing the number of vertices in the graph (1 ≤ x ≤ 10^5), and r is an integer representing the number of edges of weight 1 (0 ≤ r ≤ min((x(x-1))/(2), 10^5)).
def func_11(x, r):
    """ = ceil(x / r) """
    return (x + r - 1) // r
    #The program returns the result of the integer division of (x + r - 1) by r, which is defined when r > 0; if r = 0, the division by zero is undefined.
#Overall this is what the function does:The function accepts two integer parameters `x` (the number of vertices in the graph) and `r` (the number of edges of weight 1). It returns the result of the integer division of `(x + r - 1)` by `r`, which effectively computes the ceiling of `x / r`. If `r` is 0, the function does not handle this case explicitly, leading to a potential division by zero error, which is not addressed in the code. Therefore, the function is designed to calculate a value based on the number of vertices and edges but may raise an error if `r` is zero.

