#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 * 10^5), and y = 0. The input for each test case consists of n, x, and y followed by x distinct integers from 1 to n representing the chosen vertices. The sum of x over all test cases does not exceed 2 * 10^5.
def func_1():
    return map(int, input().split())
    #The program returns three values: t (an integer between 1 and 10^4), n (an integer between 4 and 10^9), and x (an integer between 2 and the minimum of n or 2 * 10^5). The third value, y, is 0.
#Overall this is what the function does:The function reads input data consisting of t, n, x, and y from standard input. It processes this input where t is an integer between 1 and 10^4, n is an integer between 4 and 10^9, x is an integer between 2 and the minimum of n or 2 * 10^5, and y is always 0. After processing, the function returns three values: t, n, and x.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 * 10^5), and y = 0. The vertices chosen by Bessie are represented as x distinct integers from 1 to n, and the sum of x over all test cases does not exceed 2 * 10^5.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers representing the vertices chosen by Bessie for each test case.
#Overall this is what the function does:The function reads input from the user, which includes multiple test cases. For each test case, it processes integers representing the number of vertices (n), the range limit for vertex selection (x), and an initial value (y). It then returns a list of integers, where each integer represents a unique vertex chosen by Bessie within the specified range for each test case.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, v is a list of x distinct integers representing the vertices Bessie has chosen, and y is an integer representing the maximum number of other vertices you can choose (in this specific function, y is always 0).
def func_3(n, v):
    return [v for i in range(n)]
    #The program returns a list containing n copies of the list v
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing the number of sides of a polygon, and `v`, a list of distinct integers representing the vertices Bessie has chosen. After executing, the function returns a new list containing `n` copies of the original list `v`.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, m is an integer representing the number of vertices Bessie has chosen (which is equal to x), and v is an integer representing the number of vertices you can choose (which is equal to y). Note that y is always 0 in this problem, so v will always be 0.
def func_4(n, m, v):
    return [[v for i in range(m)] for i in range(n)]
    #A 2D list with n rows and m columns, where each element in the list is 0
#Overall this is what the function does:The function accepts three parameters \( n \), \( m \), and \( v \), where \( n \) represents the number of sides of a polygon, \( m \) represents the number of vertices Bessie has chosen, and \( v \) represents the number of vertices you can choose (which is always 0). It returns a 2D list with \( n \) rows and \( m \) columns, where each element in the list is 0.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, m is an integer representing the number of vertices Bessie has chosen, and the function `func_1()` returns a pair of integers representing the vertices that can be connected by a diagonal.
def func_5(n, m):
    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x].append(y)
        
        l[y].append(x)
        
    #State: Output State: `l` is a list of lists where each sublist contains exactly two elements, which are indices of other sublists that are connected to it, based on the values returned by `func_1()` for each iteration of the loop. The loop runs `m` times, and in each iteration, it appends one of the indices returned by `func_1()` to the corresponding sublist in `l`. Additionally, the same index is appended to the sublist corresponding to the other index returned by `func_1()`, ensuring that the connections are bidirectional.
    return l
    #The program returns a list of lists 'l', where each sublist contains exactly two elements. These elements are indices of other sublists in 'l' and are connected bidirectionally. The loop runs 'm' times, and in each iteration, it appends one of the indices returned by `func_1()` to the corresponding sublist in 'l'. The same index is also appended to the sublist corresponding to the other index returned by `func_1()`, ensuring that the connections are bidirectional.
#Overall this is what the function does:The function `func_5` accepts two parameters, `n` and `m`. `n` represents the number of sides of a polygon, and `m` represents the number of vertices Bessie has chosen. The function returns a list of lists `l`, where each sublist contains exactly two elements. These elements are indices of other sublists in `l` and are connected bidirectionally. The function constructs these connections by iterating `m` times, appending one of the indices returned by `func_1()` to the corresponding sublist in `l` and ensuring the same index is added to the corresponding sublist, thus creating bidirectional connections.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, m is an integer representing the number of vertices Bessie has chosen, and the function `func_1()` returns two integers x and y which represent the vertices Bessie has chosen such that 1 ≤ x, y ≤ n and x ≠ y. Additionally, 4 ≤ n ≤ 10^9, 2 ≤ m ≤ min(n, 2 * 10^5), and m is the length of the list returned by `func_1()`.
def func_6(n, m):
    l = [[(0) for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x][y] = 1
        
        l[y][x] = 1
        
    #State: A 2D list of size (n+1) x (n+1) where each element l[x][y] is 1 if there is an edge between vertex x and vertex y among the m chosen vertices, and 0 otherwise. The diagonal elements l[x][x] are always 0 since no vertex is connected to itself.
    return l
    #The program returns a 2D list of size (n+1) x (n+1), where each element l[x][y] is 1 if there is an edge between vertex x and vertex y among the m chosen vertices, and 0 otherwise. The diagonal elements l[x][x] are always 0 since no vertex is connected to itself.
#Overall this is what the function does:The function accepts two parameters, `n` and `m`, where `n` represents the number of sides of a polygon and `m` represents the number of vertices Bessie has chosen. It returns a 2D list of size (n+1) x (n+1). Each element `l[x][y]` in this list is set to 1 if there is an edge between vertex `x` and vertex `y` among the `m` chosen vertices, and 0 otherwise. The diagonal elements `l[x][x]` are always 0, indicating that no vertex is connected to itself.

#State of the program right berfore the function call: l is a list of integers where each integer represents a vertex chosen by Bessie, and the length of the list is equal to x.
def func_7(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    #State: Output State: `d` is a dictionary where each key is a vertex from the list `l` and its value is the count of how many times that vertex appears in the list.
    return d
    #The program returns a dictionary 'd' where each key is a vertex from the list 'l' and its value is the count of how many times that vertex appears in the list 'l'.
#Overall this is what the function does:The function accepts a list of integers `l` representing vertices chosen by Bessie and returns a dictionary `d`. Each key in the dictionary is a vertex from the list `l`, and the corresponding value is the count of how many times that vertex appears in the list `l`.

#State of the program right berfore the function call: 
def func_8(l):
    n = len(l)
    m = len(l[0])
    p = [[(0) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
        
    #State: Output State: `m` is equal to the length of the first element in list `l`, `n` is equal to the length of list `l`, `p` is a 2D list with dimensions `(n + 1) x (m + 1)` where each element `p[i][j]` is the sum of all elements in the submatrix of `l` from `(0,0)` to `(i-1,j-1)`.
    return p
    #The program returns a 2D list 'p' with dimensions (n + 1) x (m + 1), where each element p[i][j] is the sum of all elements in the submatrix of 'l' from (0,0) to (i-1,j-1)
#Overall this is what the function does:The function accepts a 2D list `l`. It calculates a 2D list `p` with dimensions (n + 1) x (m + 1), where each element `p[i][j]` represents the sum of all elements in the submatrix of `l` from (0,0) to (i-1,j-1). The function then returns this 2D list `p`.

#State of the program right berfore the function call: x is an integer representing the number of vertices Bessie has chosen, and y is 0 (meaning no additional vertices can be chosen).
def func_9(x):
    return max(1 - (x & x - 1), 0)
    #The program returns 1 if x is a power of 2, otherwise it returns 0
#Overall this is what the function does:The function accepts an integer `x` and returns 1 if `x` is a power of 2, otherwise it returns 0.

#State of the program right berfore the function call: l is a list of integers where each integer is between 1 and n (inclusive), and gcd(a, i) represents the greatest common divisor of two integers a and i.
def func_10(l):
    a = 0
    for i in l:
        a = gcd(a, i)
        
    #State: Output State: `a` is the greatest common divisor (GCD) of all numbers in list `l`.
    return a
    #The program returns the greatest common divisor (GCD) of all numbers in list `l`
#Overall this is what the function does:The function accepts a list of integers `l`, where each integer is between 1 and n (inclusive), and returns the greatest common divisor (GCD) of all numbers in the list. After executing, the program state is such that it outputs the GCD of all elements in the input list `l`.

