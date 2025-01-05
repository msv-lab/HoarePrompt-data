#State of the program right berfore the function call: **Precondition**: 
- n and m are integers such that 1 <= n <= 10^5 and 0 <= m <= min((n(n-1))/(2),10^5).
- a_i and b_i are integers such that 1 <= a_i, b_i <= n and a_i ≠ b_i.
def func_1():
    n, m = func_4()
    p = list(range(n))
    r = func_7(int, n)
    sg = func_7(set, n)
    for _ in range(m):
        x, y = func_5(-1)
        
        sg[x].add(y)
        
        sg[y].add(x)
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers, `p` is a list containing numbers from 0 to n-1, `sg` is a dictionary where each key is a number from 0 to n-1 and the corresponding value is a set containing numbers that have been added to `sg[key]` during the loop execution.
    v = min(range(n), key=lambda i: len(sg[i]))
    for i in range(n):
        if i not in sg[v]:
            union(i, v)
        else:
            for j in range(n):
                if j not in sg[i]:
                    union(i, j)
        
    #State of the program after the  for loop has been executed: All sets in `sg` are fully populated with elements from 0 to n-1. Each set contains all the numbers from 0 to n-1. The index `v` of the set in `sg` with the minimum length will be any index since all sets have the same length.
    roots = set()
    for i in range(n):
        roots.add(find(i))
        
    #State of the program after the  for loop has been executed: All sets in `sg` are fully populated with elements from 0 to n-1, index `v` of the set in `sg` with the minimum length can be any index, `roots` contains the result of `find(n-1)`
    print(len(roots) - 1)
#Overall this is what the function does:Functionality: The function `func_1` initializes variables based on the return values of other functions and then populates sets in a dictionary. It then finds the set with the minimum length, performs union operations based on the elements in the sets, and finally calculates the number of unique roots. The function does not return any value.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). Each pair of integers a_i and b_i (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i) represents the endpoints of an edge of weight 1 in the graph.**
def find(v):
    vc = v
    while v != p[v]:
        v = p[v]
        
    #State of the program after the loop has been executed: `vc` is assigned the same value as `v`, `v` is equal to `p[v]`
    while vc != v:
        p[vc], vc = v, p[vc]
        
    #State of the program after the loop has been executed: vc` is equal to `v`, `v` is equal to `p[v]`, `p[vc]` is equal to `p[v]`
    return v
    #The program returns the value of variable `v`, which is equal to `p[v]` and `p[vc]` is equal to `p[v`]`.
#Overall this is what the function does:The function `find` accepts a parameter `v` representing a vertex in a graph. It iterates through the parent array `p` to find the root node using path compression technique. The function then returns the root node of the input vertex `v`. The code does not cover edge cases where `p` is not properly initialized or where `v` is out of bounds.

#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 1 <= n <= 10^5 and 0 <= m <= min((n(n-1))/(2),10^5). The input edges are represented as pairs of integers where each integer is between 1 and n, inclusive, and the two integers are not equal to each other.**
def union(u, v):
    u, v = find(u), find(v)
    if (u == v) :
        return
        #The program returns the value of variable `u` which is equal to variable `v`
    #State of the program after the if block has been executed: *u and v are not equal
    if (r[u] < r[v]) :
        u, v = v, u
    #State of the program after the if block has been executed: *u and v are not equal. If r[u] < r[v], u and v have swapped values while r[u] and r[v] remain integers.
    p[u] = v
    if (r[u] == r[v]) :
        r[u] += 1
    #State of the program after the if block has been executed: *`u` and `v` are integers and `u` is not equal to `v`. If `r[u]` is equal to `r[v]`, then `u` and `v` have swapped values while `r[u]` and `r[v]` remain integers with `r[u]` being one more than `r[v]`. Additionally, `p[u]` is `v`.
#Overall this is what the function does:Functionality: The function `union` takes two parameters `u` and `v` and ensures that they are connected in a union-find data structure. It finds the root of each parameter and compares their ranks. If the ranks are equal, one of the roots becomes the parent of the other, and the rank of the new parent increases by 1. If the ranks are not equal, the root with the lower rank becomes the child of the other root. The function does not return anything explicitly, but it modifies the parent array `p` and rank array `r` accordingly to perform the union operation. The precondition specifies the valid ranges for `u` and `v`, ensuring that they are within acceptable bounds.

#State of the program right berfore the function call: x is an integer greater than or equal to 0.**
def func_2(x):
    return pow(x, MOD - 2, MOD)
    #The program returns the result of calculating x raised to the power of (MOD - 2) modulo MOD
#Overall this is what the function does:The function accepts a parameter x, which is an integer greater than or equal to 0, and calculates x raised to the power of (MOD - 2) modulo MOD.

#State of the program right berfore the function call: x and y are non-negative integers such that 1 ≤ x ≤ 10^5, 0 ≤ y ≤ min((x(x-1))/(2),10^5).**
def func_3(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: x and y are non-negative integers satisfying the given constraints, with x being the greatest common divisor of the initial values of x and y, and y being 0
    return x
    #The program returns the greatest common divisor of the initial values of x and y, which is x.
#Overall this is what the function does:The function `func_3` accepts two non-negative integers x and y where 1 ≤ x ≤ 10^5 and 0 ≤ y ≤ min((x(x-1))/(2),10^5). It calculates the greatest common divisor of the initial values of x and y using the Euclidean algorithm and returns the result as x.

#State of the program right berfore the function call: n and m are non-negative integers such that 1 <= n <= 10^5 and 0 <= m <= min((n(n-1))/(2),10^5).**
def func_4():
    return list(map(int, input().split()))
    #The program returns a list of integers by mapping the input values after splitting them.
#Overall this is what the function does:The function func_4 does not accept any parameters. It reads input values, splits them, maps them to integers, and returns a list of integers. The function does not handle any edge cases or validate the input.

#State of the program right berfore the function call: **Precondition**: **n and m are non-negative integers such that 1 <= n <= 10^5 and 0 <= m <= min((n*(n-1))/2, 10^5). a_i and b_i are integers representing the endpoints of each edge with 1 <= a_i, b_i <= n and a_i != b_i.**
def func_5(o):
    return list(map(lambda x: int(x) + o, input().split()))
    #The program returns a list where each element is the integer value of the input split by spaces plus the value of variable 'o'
#Overall this is what the function does:The function func_5 accepts a parameter 'o' and returns a list where each element is the integer value of the input split by spaces plus the value of variable 'o'. The function reads input from the console, splits it by spaces, converts each element to an integer, adds 'o' to each element, and returns the resulting list. The function does not handle any exceptions that may arise from invalid input or missing values.

#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 1 <= n <= 10^5 and 0 <= m <= min((n(n-1))/(2),10^5).**
def func_6(n, m):
    return [func_4() for _ in range(n)]
    #The program returns a list of results from calling func_4() n times
#Overall this is what the function does:The function `func_6` accepts two integer parameters `n` and `m` where 1 <= n <= 10^5 and 0 <= m <= min((n(n-1))/(2),10^5). It then returns a list containing the results of calling `func_4()` n times.

#State of the program right berfore the function call: **
def func_7(f):
    return [func_7(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list of values obtained by calling function `func_7` with arguments `f` and unpacked `dim[1:]` for each value in the range of `dim[0]` if `dim` is not empty. Otherwise, it returns the result of calling function `f`.
#Overall this is what the function does:The function `func_7` accepts a parameter `f` and a list `dim`. If `dim` is not empty, the function returns a list of values obtained by calling function `func_7` with arguments `f` and unpacked `dim[1:]` for each value in the range of `dim[0]`. If `dim` is empty, the function simply returns the result of calling function `f`.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i.**
def func_8(start, step, count):
    return range(start, start + step * count, step)
    #The program returns a range starting from 'start' with a step size of 'step' and containing 'count' elements
#Overall this is what the function does:The function `func_8` accepts three parameters: `start`, `step`, and `count`, all of which are integers. The function returns a range starting from the `start` value with a step size of `step` and containing `count` elements. The code accurately implements this functionality without missing logic or edge cases.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10^5, 0 ≤ m ≤ min((n(n-1))/(2),10^5). a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i.**
def func_9(l, start, end):
    return range(start, len(l) + end)
    #The program returns a range starting from index 'start' up to the length of list 'l' plus 'end'.
#Overall this is what the function does:The function `func_9` accepts a list `l`, and two integers `start` and `end`. It then returns a range starting from index `start` up to the length of list `l` plus `end`. The function ensures that `start` and `end` fall within the valid range for indexing the list `l`.

#State of the program right berfore the function call: n is a tuple of two integers where the first integer represents the number of vertices (1 ≤ n ≤ 10^5) and the second integer represents the number of edges of weight 1 in the graph (0 ≤ m ≤ min((n(n-1))/(2),10^5)).**
def func_10(n):
    """ [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] """
    return 2 ** (n - 1).bit_length()
    #The program returns the smallest power of 2 that is greater than or equal to the number of vertices in the graph
#Overall this is what the function does:The function func_10 accepts a tuple of two integers representing the vertices and edges in a graph. It then calculates and returns the smallest power of 2 that is greater than or equal to the number of vertices in the graph. The function uses a bitwise operation to find the nearest power of 2.

#State of the program right berfore the function call: x and r are integers such that 1 ≤ x ≤ 10^5 and 0 ≤ r ≤ min((x(x-1))/(2),10^5).**
def func_11(x, r):
    """ = ceil(x / r) """
    return (x + r - 1) // r
    #The program returns the result of the expression (x + r - 1) divided by r, rounded up to the nearest integer
#Overall this is what the function does:The function `func_11` accepts two parameters `x` and `r`, both integers satisfying the constraints 1 ≤ x ≤ 10^5 and 0 ≤ r ≤ min((x(x-1))/(2),10^5). The function calculates the result of the expression (x + r - 1) divided by r, rounded up to the nearest integer and returns that result.

