#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, where 1 ≤ n ≤ 100,000, and m is an integer representing the number of edges with weight 1, where 0 ≤ m ≤ min((n(n-1))/2, 100,000). For each of the next m lines, a_i and b_i are integers representing the endpoints of the edges with weight 1, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_1():
    n, m = func_4()
    p = list(range(n))
    r = func_7(int, n)
    sg = func_7(set, n)
    for _ in range(m):
        x, y = func_5(-1)
        
        sg[x].add(y)
        
        sg[y].add(x)
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of vertices in the graph; `m` is the number of edges added; `sg` is a list of sets where each set `sg[i]` contains the vertices connected to vertex `i`; `sg` contains edges as defined by the pairs (x, y) returned from `func_5(-1)` for all iterations of the loop.
    v = min(range(n), key=lambda i: len(sg[i]))
    for i in range(n):
        if i not in sg[v]:
            union(i, v)
        else:
            for j in range(n):
                if j not in sg[i]:
                    union(i, j)
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of vertices, `m` is the number of edges added, `sg` is a list of sets representing the connections after unions, `v` is the index of the vertex with the minimum connections in `sg`.
    roots = set()
    for i in range(n):
        roots.add(find(i))
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of vertices, `roots` is a set containing the unique roots from `find(i)` for all `i` in range `n`, `m` is unchanged, `sg` is unchanged, and `v` is unchanged.
    print(len(roots) - 1)
#Overall this is what the function does:The function processes a graph defined by an integer number of vertices `n` and edges `m`, constructing the graph using sets to represent connections between vertices. It then performs union operations to determine connected components in the graph and prints the number of unique connected components minus one. The function assumes all inputs are valid according to specified constraints and does not handle cases where `n` or `m` are outside the defined limits.

#State of the program right berfore the function call: v is a tuple containing two integers n and m, where n is the number of vertices (1 ≤ n ≤ 10^5) and m is the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2),10^5)). Additionally, there are m pairs of integers (a_i, b_i) representing the endpoints of the edges with weight 1, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def find(v):
    vc = v
    while v != p[v]:
        v = p[v]
        
    #State of the program after the loop has been executed: `v` is equal to `p[v]`, indicating that the final value of `v` is a stable state defined by the mapping of `p`.
    while vc != v:
        p[vc], vc = v, p[vc]
        
    #State of the program after the loop has been executed: `v` is equal to the stable value defined by the mapping `p`, `vc` is also equal to `v`.
    return v
    #The program returns the stable value defined by the mapping `p`, which is equal to `v`.
#Overall this is what the function does:The function accepts a parameter `v`, which is expected to be an integer representing a vertex in a union-find (disjoint-set) structure. It follows the union-find algorithm to find the representative or root of the set containing `v` by traversing through a mapping `p`. The function returns the stable value (or root) of the set for the given vertex, based on the mapping defined by `p`. The input parameter `v` is not a tuple containing two integers; rather, it should be a single integer corresponding to a vertex.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the graph (1 ≤ n ≤ 10^5), m is a non-negative integer representing the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2),10^5)), and for each of the m edges, a_i and b_i are integers (1 ≤ a_i, b_i ≤ n) representing the endpoints of the edges, with a_i ≠ b_i.
def union(u, v):
    u, v = find(u), find(v)
    if (u == v) :
        return
        #The program returns None because there is no value specified to return.
    #State of the program after the if block has been executed: *`u` and `v` are assigned the values returned by the `find` function when called with their current values. `u` is not equal to `v`. Other variables remain unaffected.
    if (r[u] < r[v]) :
        u, v = v, u
    #State of the program after the if block has been executed: *`u` and `v` are assigned the values returned by the `find` function when called with their current values, and `u` is not equal to `v`. If the value of `r[u]` is less than the value of `r[v]`, then the values of `u` and `v` are swapped. Otherwise, the values of `u` and `v` remain unchanged.
    p[u] = v
    if (r[u] == r[v]) :
        r[u] += 1
    #State of the program after the if block has been executed: *`u` and `v` are assigned the values returned by the `find` function when called with their current values, `u` is not equal to `v`, and `p[u]` is assigned the value of `v`. If the values at index `u` and `v` in array `r` are equal, then `r[u]` is incremented by 1.
#Overall this is what the function does:The function accepts two integer parameters, `u` and `v`, which represent endpoints of an edge in a graph. It performs a union operation on the sets containing `u` and `v`, effectively connecting them in a disjoint-set data structure. If `u` and `v` are already in the same set, the function returns None without making any changes. If they are in different sets, it updates the parent of one set to the other and adjusts the rank if necessary, but does not return any value.

#State of the program right berfore the function call: x is a tuple containing two integers n and m, where n (1 ≤ n ≤ 10^5) is the number of vertices and m (0 ≤ m ≤ min((n(n-1))/(2),10^5)) is the number of edges of weight 1 in the graph. Additionally, the next m lines contain pairs of integers (a_i, b_i) representing the endpoints of the edges of weight 1, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_2(x):
    return pow(x, MOD - 2, MOD)
    #The program returns the result of raising the tuple x to the power of (MOD - 2) modulo MOD
#Overall this is what the function does:The function accepts a tuple `x` containing two integers, which represent the number of vertices `n` and the number of edges `m`. It returns the result of raising the tuple `x` to the power of `(MOD - 2)` modulo `MOD`. However, it is important to note that raising a tuple to a power is not a typical operation in Python, and this may lead to unexpected behavior or errors if `x` is not a numeric type. The function does not handle cases where `x` is not a number and does not check for the validity of the tuple's contents.

#State of the program right berfore the function call: x is an integer representing the number of vertices (1 ≤ x ≤ 10^5), and y is an integer representing the number of edges with weight 1 (0 ≤ y ≤ min((x(x-1))/(2), 10^5)).
def func_3(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `y` is 0, `x` is the greatest common divisor of the initial values of `x` and `y`.
    return x
    #The program returns the greatest common divisor of the initial values of `x` and `y`, which is `x` since `y` is 0.
#Overall this is what the function does:The function accepts two integers `x` and `y`. It calculates and returns the greatest common divisor (GCD) of the initial values of `x` and `y` using the Euclidean algorithm. If `y` is initially 0, it returns `x` as the GCD. If `y` is non-zero, it performs a series of calculations until `y` reaches 0, at which point it returns the GCD. The function handles cases where `x` is 0 or `y` is 0, returning the other value appropriately.

#State of the program right berfore the function call: n is an integer representing the number of vertices in a graph, where 1 ≤ n ≤ 10^5; m is an integer representing the number of edges with weight 1, where 0 ≤ m ≤ min((n(n-1))/(2),10^5); for each edge, a_i and b_i are integers representing the endpoints of the edge, where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_4():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained from the input, which represents the values entered by the user.
#Overall this is what the function does:The function accepts no parameters and returns a list of integers obtained from user input, which represents the values entered by the user. The function does not handle any validation or constraints related to the integers, such as ensuring they are within specified ranges or handling non-integer inputs.

#State of the program right berfore the function call: o is a tuple containing two integers n and m, where n is the number of vertices (1 ≤ n ≤ 10^5) and m is the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/(2), 10^5)). Following this, there are m pairs of integers (a_i, b_i) representing the endpoints of each edge with weight 1, ensuring that 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i, with no duplicate edges.
def func_5(o):
    return list(map(lambda x: int(x) + o, input().split()))
    #The program returns a list of integers, where each integer is the sum of the corresponding input integer and the tuple 'o' containing two integers n and m.
#Overall this is what the function does:The function accepts a tuple `o` containing two integers `n` and `m`, and returns a list of integers where each integer is the sum of the corresponding input integer and the first integer of the tuple `o`. The function does not consider the second integer of the tuple `o` or handle any input validation regarding the number of integers entered, which could lead to unexpected behavior if the input does not match the expected format.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph (1 ≤ n ≤ 100,000), m is an integer representing the number of edges with weight 1 (0 ≤ m ≤ min((n(n-1))/2, 100,000)), and m edges are defined by pairs of integers (a_i, b_i) where 1 ≤ a_i, b_i ≤ n and a_i ≠ b_i.
def func_6(n, m):
    return [func_4() for _ in range(n)]
    #The program returns a list of n elements, each being the result of calling func_4()
#Overall this is what the function does:The function accepts two integer parameters, `n` (representing the number of vertices in a graph) and `m` (representing the number of edges), and returns a list containing `n` elements. Each element in the list is generated by calling the function `func_4()`, which is not defined in the provided code. The function does not utilize the value of `m` or the details regarding edges in its functionality.

#State of the program right berfore the function call: f is a 2D list representing the vertices of a complete undirected weighted graph, where each edge has a weight of either 0 or 1; dim is a tuple containing two integers n and m, where n (1 ≤ n ≤ 10^5) is the number of vertices and m (0 ≤ m ≤ min((n(n-1))/(2),10^5)) is the number of edges with weight 1, and for each edge, the endpoints a_i and b_i (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i) are provided.
def func_7(f):
    return [func_7(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list containing the result of func_7 applied to the second element of dim for each vertex in the complete undirected weighted graph represented by f, repeated dim[0] times, if dim is not empty; otherwise, it returns f()
#Overall this is what the function does:The function accepts a 2D list `f` representing a complete undirected weighted graph and a tuple `dim` that describes the number of vertices and edges. If `dim` is not empty, it returns a list containing the result of recursively applying `func_7` to the second element of `dim`, repeated `dim[0]` times. If `dim` is empty, it returns `f()` directly. It is important to note that the function's behavior depends on the definition of `f` and `dim`, which are not fully detailed in the provided code, leading to potential ambiguity regarding the exact structure and expected input.

#State of the program right berfore the function call: start is an integer representing the number of vertices in the graph (1 ≤ start ≤ 10^5), step is an integer representing the number of edges of weight 1 (0 ≤ step ≤ min((start(start-1))/(2),10^5)), and count is a list of tuples where each tuple contains two integers (a_i, b_i) representing the endpoints of edges with weight 1 (1 ≤ a_i, b_i ≤ start, a_i ≠ b_i).
def func_8(start, step, count):
    return range(start, start + step * count, step)
    #The program returns a range starting from `start` to `start + step * len_count` with a step of `step`, where `len_count` is the number of tuples in the list `count`.
#Overall this is what the function does:The function accepts an integer `start`, an integer `step`, and a list of tuples `count`. It returns a range object starting from `start` to `start + step * len(count)` with a step of `step`, where `len(count)` is the number of tuples in the list. The function does not validate the input parameters, so it assumes they are within the specified constraints. If `count` is empty, the range will start and end at `start`.

#State of the program right berfore the function call: l is a list of pairs of integers representing edges with weight 1 in a complete undirected graph, start and end are integers that represent the range of vertices (1 ≤ start, end ≤ n) where n is the number of vertices in the graph and m is the number of edges in the graph such that 1 ≤ n ≤ 10^5 and 0 ≤ m ≤ min((n(n-1))/(2),10^5).
def func_9(l, start, end):
    return range(start, len(l) + end)
    #The program returns a range object from 'start' to 'len(l) + end', where 'len(l)' is the number of edges in the list 'l' representing pairs of integers.
#Overall this is what the function does:The function accepts a list `l` of pairs of integers representing edges, an integer `start`, and an integer `end`. It returns a range object that starts from `start` and extends to `len(l) + end`, where `len(l)` is the number of edges in the list `l`. There are no checks for the validity of `start` or `end`, which could lead to unexpected results if they are outside the expected bounds or if `start` is greater than `len(l) + end`.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the graph, and m is a non-negative integer representing the number of edges with weight 1 such that 0 ≤ m ≤ min((n(n-1))/2, 10^5). Each of the next m lines contains two distinct integers a_i and b_i (1 ≤ a_i, b_i ≤ n) representing the endpoints of an edge with weight 1.
def func_10(n):
    """ [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] """
    return 2 ** (n - 1).bit_length()
    #The program returns the number of bits required to represent 2 raised to the power of (n - 1), which is equivalent to n - 1 + 1, hence the return value is n.
#Overall this is what the function does:The function accepts a positive integer `n` and returns `n`, which is the number of bits required to represent \(2^{(n-1)}\). It effectively calculates the value of `n` based on the bit length of \(2^{(n-1)}\).

#State of the program right berfore the function call: x is an integer representing the number of vertices in the graph (1 ≤ x ≤ 10^5), and r is a non-negative integer representing the number of edges of weight 1 (0 ≤ r ≤ min((x(x-1))/(2), 10^5)).
def func_11(x, r):
    """ = ceil(x / r) """
    return (x + r - 1) // r
    #The program returns the integer result of the expression (x + r - 1) // r, where x is the number of vertices in the graph and r is the number of edges of weight 1
#Overall this is what the function does:The function accepts an integer `x` representing the number of vertices in a graph and a non-negative integer `r` representing the number of edges of weight 1. It returns the integer result of the expression (x + r - 1) // r, which effectively computes the ceiling of the division x / r. If `r` is 0, it would lead to a division by zero error, which is not handled in the code, indicating a potential edge case that needs attention.

