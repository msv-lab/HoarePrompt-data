#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, where 1 ≤ n ≤ 100000; m is an integer representing the number of edges with weight 1, where 0 ≤ m ≤ min((n(n-1))/2, 100000); for each of the m edges, a_i and b_i are integers representing the endpoints of the edges, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_1():
    n, m = func_4()
    p = list(range(n))
    r = func_7(int, n)
    sg = func_7(set, n)
    for _ in range(m):
        x, y = func_5(-1)
        
        sg[x].add(y)
        
        sg[y].add(x)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `p` is a list of integers from 0 to `n-1`, `r` is the value returned by func_7(int, n), `sg` contains edges added from the pairs (x, y) returned by func_5(-1) for each of the `m` iterations, where each `x` and `y` are integers representing vertices in the graph.
    v = min(range(n), key=lambda i: len(sg[i]))
    for i in range(n):
        if i not in sg[v]:
            union(i, v)
        else:
            for j in range(n):
                if j not in sg[i]:
                    union(i, j)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `p` is a list of integers from 0 to `n-1`, `sg` contains the edges from the union operations among all indices, `v` is still the index of the vertex with the fewest edges in `sg`, and all indices `0` to `n-1` are connected through the union operations.
    roots = set()
    for i in range(n):
        roots.add(find(i))
        
    #State of the program after the  for loop has been executed: `n` is an integer, `roots` contains the unique results of `find(i)` for all indices `i` from 0 to `n-1`.
    print(len(roots) - 1)
#Overall this is what the function does:The function processes a graph defined by a number of vertices `n` and edges `m` provided through internal function calls. It builds a connection between the vertices based on the edges and performs union-find operations to determine the number of connected components in the graph. Finally, it outputs the number of additional edges needed to connect all components, which is one less than the number of unique roots found in the union operations. The function does not accept parameters directly and relies on the internal definitions for graphs.

#State of the program right berfore the function call: v is a tuple containing two integers n and m, where n is the number of vertices (1 ≤ n ≤ 10^5) and m is the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2), 10^5)).
def find(v):
    vc = v
    while v != p[v]:
        v = p[v]
        
    #State of the program after the loop has been executed: `v` is equal to `p[v]`, indicating convergence; the loop has terminated when `v` equals `p[v]`.
    while vc != v:
        p[vc], vc = v, p[vc]
        
    #State of the program after the loop has been executed: 'v' is equal to 'p[v]', 'vc' is equal to 'v', and the loop has terminated as 'vc' equals 'v'.
    return v
    #The program returns the value of 'v', which is equal to 'p[v]'
#Overall this is what the function does:The function accepts a tuple `v` containing two integers, which represent the number of vertices `n` and the number of edges `m`. It performs path compression on a disjoint set, ultimately returning the root representative of the set containing the vertex `v`. The function does not explicitly handle the initialization of `p`, which should be defined externally; if `p` is not properly initialized, it may lead to incorrect behavior or an error.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the graph, m is a non-negative integer representing the number of edges with weight 1, and for each edge described by a_i and b_i, 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def union(u, v):
    u, v = find(u), find(v)
    if (u == v) :
        return
        #The program returns nothing as the return statement is empty.
    #State of the program after the if block has been executed: *`n` is a positive integer representing the number of vertices in the graph, `m` is a non-negative integer representing the number of edges with weight 1, the values of `u` and `v` are updated to their respective representatives in the union-find structure as determined by the `find` function, and `u` is not equal to `v`.
    if (r[u] < r[v]) :
        u, v = v, u
    #State of the program after the if block has been executed: *`n` is a positive integer representing the number of vertices in the graph, `m` is a non-negative integer representing the number of edges with weight 1, `u` and `v` are updated to their respective representatives in the union-find structure. If `r[u]` is less than `r[v]`, then `u` is assigned the value of `v`, and `v` is assigned the value of `u`.
    p[u] = v
    if (r[u] == r[v]) :
        r[u] += 1
    #State of the program after the if block has been executed: *`n` is a positive integer and `m` is a non-negative integer. If `r[u]` is equal to `r[v]`, then `r[u]` is increased by 1, while `r[v]` remains unchanged. If `r[u]` is not equal to `r[v]`, the state remains unchanged since there is no else part.
#Overall this is what the function does:The function accepts two integer parameters `u` and `v`, representing vertices in a graph, and performs a union operation to connect these vertices in a union-find structure. If `u` and `v` are already connected, the function does nothing. If they are not connected, it updates the parent pointers and the rank of the trees in the union-find structure but does not return any result. The function does not handle cases where `u` or `v` are out of bounds or invalid.

#State of the program right berfore the function call: x is a tuple containing two integers n and m, where n is the number of vertices (1 ≤ n ≤ 10^5) and m is the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2),10^5)). The next m elements in the input represent pairs of integers (a_i, b_i) indicating the endpoints of edges with weight 1, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_2(x):
    return pow(x, MOD - 2, MOD)
    #The program returns the result of raising the tuple x to the power of MOD - 2, modulo MOD.
#Overall this is what the function does:The function accepts a tuple `x` containing two integers `n` and `m`, and returns the result of raising the tuple `x` to the power of `MOD - 2`, modulo `MOD`. However, this operation may not be meaningful as raising a tuple to a power is not a standard operation in Python, and could lead to unexpected behavior or a TypeError. Therefore, the functionality does not align with the annotations, which imply that it would work as intended.

#State of the program right berfore the function call: x is an integer representing the number of vertices in the graph (1 ≤ x ≤ 10^5), and y is an integer representing the number of edges with weight 1 (0 ≤ y ≤ min((x(x-1))/(2), 10^5)).
def func_3(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `y` is 0, `x` is the GCD of the original values of `x` and `y`.
    return x
    #The program returns the GCD of the original values of `x` and `y`, where `y` is 0. Therefore, the program returns the value of `x`.
#Overall this is what the function does:The function accepts two integers, `x` and `y`, and computes their greatest common divisor (GCD) using the Euclidean algorithm. It continues swapping the values of `x` and `y` until `y` becomes 0. The function then returns the GCD, which is the value of `x` at that point. It handles cases where `y` is initially 0 by directly returning `x` as the GCD.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the graph (1 ≤ n ≤ 10^5), m is a non-negative integer representing the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2),10^5)), and for each of the m edges, a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_4():
    return list(map(int, input().split()))
    #The program returns a list of integers from the input, which are provided as space-separated values
#Overall this is what the function does:The function accepts no parameters and returns a list of integers obtained from user input, where the integers are expected to be provided as space-separated values. It does not handle invalid input cases, such as non-integer values or empty input, which may result in a ValueError when converting the input to integers.

#State of the program right berfore the function call: o is a tuple containing two integers n and m, where n is the number of vertices (1 ≤ n ≤ 100000) and m is the number of edges of weight 1 (0 ≤ m ≤ min((n(n-1))/(2), 100000)). Following this, there are m pairs of integers (a_i, b_i) representing the endpoints of each edge of weight 1, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_5(o):
    return list(map(lambda x: int(x) + o, input().split()))
    #The program returns a list of integers where each integer is the sum of the corresponding integer from the input and the tuple 'o' containing two integers (n, m)
#Overall this is what the function does:The function accepts a tuple `o` containing two integers (n, m) and reads a line of input consisting of integers. It returns a list of integers where each integer is the sum of the corresponding integer from the input and the sum of the tuple `o` (i.e., the sum of n and m). If the input does not contain a sufficient number of integers to match the expected count (which is based on the number of integers provided in the input), the function may raise an error.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices (1 ≤ n ≤ 10^5), m is a non-negative integer representing the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2),10^5)), and for each of the next m lines, there are two integers a_i and b_i (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i) representing the endpoints of the edges with weight 1.
def func_6(n, m):
    return [func_4() for _ in range(n)]
    #The program returns a list containing the results of calling func_4() n times, where n is a positive integer representing the number of vertices.
#Overall this is what the function does:The function accepts two parameters, `n`, a positive integer representing the number of vertices, and `m`, a non-negative integer representing the number of edges. It returns a list containing the results of calling `func_4()` a total of `n` times, regardless of the value of `m`. The function does not utilize the `m` parameter in its execution, which may indicate a potential oversight or missing functionality related to the edges.

#State of the program right berfore the function call: f is a function that accepts two integers n and m, where 1 ≤ n ≤ 10^5 and 0 ≤ m ≤ min((n(n-1))/(2),10^5), and subsequent pairs of integers representing edges of weight 1, where each pair (a_i, b_i) satisfies 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_7(f):
    return [func_7(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list containing the result of calling func_7 with the function f and the subsequent pairs of integers based on the dimensions specified in dim, repeated dim[0] times, or the result of calling f() if dim is empty.
#Overall this is what the function does:The function accepts another function `f` and processes dimensions specified in `dim`. If `dim` is not empty, it returns a list containing the results of calling `func_7` with `f` and the subsequent pairs of integers, repeated `dim[0]` times. If `dim` is empty, it simply returns the result of calling `f()`. However, the function lacks the definition of `dim`, making it unclear how dimensions are provided or initialized, which could lead to potential errors if `dim` is not set before the function is called.

#State of the program right berfore the function call: start is an integer representing the number of vertices in the graph (1 ≤ start ≤ 10^5), step is an integer representing the number of edges of weight 1 in the graph (0 ≤ step ≤ min((start(start-1))/(2),10^5)), and count is a list of tuples where each tuple contains two integers representing the endpoints of the edges of weight 1 (1 ≤ a_i, b_i ≤ start, a_i ≠ b_i).
def func_8(start, step, count):
    return range(start, start + step * count, step)
    #The program returns a range object starting from 'start' to 'start + step * count' with a step of 'step'.
#Overall this is what the function does:The function accepts three parameters: an integer `start`, an integer `step`, and an integer `count`. It returns a range object starting from `start` up to, but not including, `start + step * count`, with increments of `step`. Note that `count` is expected to be an integer, but the code does not validate the input types or values, which may lead to unexpected behavior if `count` is not a non-negative integer. Additionally, if `step` is zero, the range would not progress, leading to an infinite loop if misused.

#State of the program right berfore the function call: l is a list of tuples representing edges in a complete undirected weighted graph, where each tuple contains two distinct integers (a_i, b_i) indicating an edge with weight 1 between vertices a_i and b_i; start is an integer representing the starting vertex (default is 0), and end is an integer representing the ending vertex (default is 0). The number of vertices n is inferred from the maximum value in the tuples and must satisfy 1 ≤ n ≤ 10^5, and the number of edges m must satisfy 0 ≤ m ≤ min((n(n-1))/(2), 10^5).
def func_9(l, start, end):
    return range(start, len(l) + end)
    #The program returns a range object starting from 'start' and ending at the length of the list 'l' plus 'end'
#Overall this is what the function does:The function accepts a list of edges `l`, an integer `start`, and an integer `end`, and returns a range object that starts from `start` and extends to `len(l) + end`. The function does not perform any validation on the inputs, so it can potentially return a range that starts or ends out of bounds depending on the values of `start` and `end`.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, where 1 ≤ n ≤ 10^5. The function does not take in m directly, but m is determined by the number of edges with weight 1, which can be between 0 and min((n(n-1))/(2),10^5). The pairs of integers (a_i, b_i) indicating the endpoints of the edges with weight 1 are provided in the input, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_10(n):
    """ [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] """
    return 2 ** (n - 1).bit_length()
    #The program returns 2 raised to the power of (n - 1) bit length, which represents the smallest power of 2 greater than or equal to n.
#Overall this is what the function does:The function accepts an integer `n` and returns the smallest power of 2 that is greater than or equal to `n`. This is achieved by calculating `2` raised to the power of the bit length of `(n - 1)`.

#State of the program right berfore the function call: x is an integer representing the number of vertices in the graph (1 ≤ x ≤ 10^5) and r is an integer representing the number of edges with weight 1 (0 ≤ r ≤ min((x(x-1))/(2),10^5)).
def func_11(x, r):
    """ = ceil(x / r) """
    return (x + r - 1) // r
    #The program returns the integer result of (x + r - 1) // r, which represents the ceiling of x divided by r
#Overall this is what the function does:The function accepts two parameters, `x` (the number of vertices in a graph) and `r` (the number of edges with weight 1), and returns the ceiling of the division of `x` by `r`. If `r` is 0, the function will still perform the calculation as (x + r - 1) // r, which results in a division by zero in practical terms since it becomes (x - 1) // 0; this scenario is not handled and could lead to an error in a real application. The function, therefore, assumes that `r` is always greater than 0 when performing the division but does not have explicit error handling for the case when `r` is 0.

