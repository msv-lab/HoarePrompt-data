#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The input for each test case consists of the first line containing n, x, and y, followed by the second line containing x distinct integers from 1 to n representing the chosen vertices. The sum of x over all test cases does not exceed 2⋅10^5.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing three integers: n, x, and y, where n is between 4 and 10^9, x is between 2 and the minimum of n or 2*10^5, and y is 0.
#Overall this is what the function does:The function processes input data consisting of integers n, x, and y, where n is between 4 and 10^9, x is between 2 and the minimum of n or 2*10^5, and y is 0. It returns a map object containing these three integers n, x, and y.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 * 10^5), and y = 0; vertices is a list of x distinct integers from 1 to n.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers read from user input, split by spaces.
#Overall this is what the function does:The function reads a line of space-separated integers from user input and returns them as a list of integers.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, v is a list of x distinct integers representing the vertices Bessie has chosen, and y is an integer representing the maximum number of other vertices that can be chosen (in this specific function, y is always 0).
def func_3(n, v):
    return [v for i in range(n)]
    #The program returns a list containing 'v' repeated 'n' times.
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing the number of sides of a polygon, and `v`, a list of distinct integers representing the vertices. It returns a list containing the elements of `v` repeated `n` times.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, m is an integer representing the number of vertices Bessie has chosen (which is equal to x), and v is a list of m distinct integers representing the vertices Bessie has chosen.
def func_4(n, m, v):
    return [[v for i in range(m)] for i in range(n)]
    #A nested list where each of the n rows contains m elements, each element being a reference to one of the integers in the list v.
#Overall this is what the function does:The function accepts three parameters: `n` (the number of sides of a polygon), `m` (the number of vertices Bessie has chosen), and `v` (a list of `m` distinct integers representing the vertices). It returns a nested list where each of the `n` rows contains `m` elements, each of which is a reference to one of the integers in the list `v`.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, m is an integer representing the number of vertices Bessie has chosen, and the function `func_1()` returns a pair of integers (x, y) where x and y are distinct integers between 1 and n inclusive. Additionally, y = 0 and 4 ≤ n ≤ 10^9, 2 ≤ m ≤ min(n, 2 * 10^5).
def func_5(n, m):
    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x].append(y)
        
        l[y].append(x)
        
    #State: Output State: The list `l` will contain `n + 1` lists. Each list at index `i` (where `i` ranges from 1 to `n`) will have exactly two elements, which are the two vertices Bessie has chosen using the function `func_1()`. These two vertices will always be distinct for each call to `func_1()` within the loop. The first element in each list corresponds to the vertex `x` returned by `func_1()`, and the second element corresponds to the vertex `y` (which is always 0 in the given code but seems to be a typo and should be a distinct integer between 1 and `n`). The list `l[0]` remains empty throughout the process.
    return l
    #The program returns a list `l` that contains `n + 1` lists. Each list at index `i` (where `i` ranges from 1 to `n`) contains two elements: the first element is the vertex `x` returned by the function `func_1()`, and the second element is the vertex `y` (which is always 0 in the given code but seems to be a typo and should be a distinct integer between 1 and `n`). The list `l[0]` remains empty throughout the process.
#Overall this is what the function does:The function `func_5` accepts two parameters, `n` and `m`. `n` represents the number of sides of a polygon, and `m` represents the number of vertices Bessie has chosen. The function generates a list `l` of size `n + 1`, where each sublist at index `i` (from 1 to `n`) contains two elements: the first element is a vertex `x` returned by the function `func_1()`, and the second element is a distinct integer `y` between 1 and `n`. The list `l[0]` remains empty.

#State of the program right berfore the function call: 
def func_6(n, m):
    l = [[(0) for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x][y] = 1
        
        l[y][x] = 1
        
    #State: Output State: The 2D list `l` will have `1`s at positions `(x, y)` and `(y, x)` for every pair `(x, y)` returned by `func_1()` during the `m` iterations of the loop. All other elements in the list will remain `0`.
    return l
    #The 2D list `l` will have 1s at positions `(x, y)` and `(y, x)` for every pair `(x, y)` returned by `func_1()` during the `m` iterations of the loop. All other elements in the list will remain 0.
#Overall this is what the function does:The function `func_6` accepts two parameters, `n` and `m`. It returns a 2D list `l` of size `(n+1) x (n+1)` where, for each pair `(x, y)` generated by `func_1()` over `m` iterations, the positions `(x, y)` and `(y, x)` in the list are set to 1. All other positions in the list remain 0.

#State of the program right berfore the function call: l is a list of integers where each integer represents a vertex chosen by Bessie. The length of l is equal to x, and each vertex is an integer between 1 and n (inclusive).
def func_7(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    #State: Output State: `d` is a dictionary where each key is a vertex from the list `l` and the value for each key is the number of times that vertex appears in the list `l`.
    return d
    #The program returns a dictionary 'd' where each key is a vertex from the list 'l' and the value for each key is the number of times that vertex appears in the list 'l'.
#Overall this is what the function does:The function accepts a list of integers `l`, where each integer represents a vertex chosen by Bessie. It returns a dictionary `d` where each key is a vertex from the list `l` and the value for each key is the count of how many times that vertex appears in the list `l`.

#State of the program right berfore the function call: l is a 2D list of integers where each sublist has the same length m, representing a matrix, and n is the number of rows in the matrix.
def func_8(l):
    n = len(l)
    m = len(l[0])
    p = [[(0) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
        
    #State: Output State: `p` is a 2D list where each element `p[i][j]` represents the sum of all elements in the submatrix `l[0:i][0:j]`. The dimensions of `p` are `(n + 1) x (m + 1)`.
    return p
    #The program returns a 2D list `p` where each element `p[i][j]` represents the sum of all elements in the submatrix `l[0:i][0:j]`, with dimensions `(n + 1) x (m + 1)`
#Overall this is what the function does:The function accepts a 2D list `l` of integers, where each sublist has the same length `m`, representing a matrix. It constructs and returns a 2D list `p` of dimensions `(n + 1) x (m + 1)`, where each element `p[i][j]` represents the sum of all elements in the submatrix `l[0:i][0:j]`.

#State of the program right berfore the function call: x is an integer such that 2 ≤ x ≤ min(n, 2 ⋅ 10^5), where n is the number of sides of the polygon.
def func_9(x):
    return max(1 - (x & x - 1), 0)
    #The program returns 0
#Overall this is what the function does:The function accepts an integer \( x \) within the range \([2, \min(n, 200000)]\), and returns 0 regardless of the input value.

#State of the program right berfore the function call: l is a list of integers where the greatest common divisor (GCD) of the elements is to be found, and the length of the list is at least 1.
def func_10(l):
    a = 0
    for i in l:
        a = gcd(a, i)
        
    #State: Output State: `a` is the greatest common divisor of all numbers in list `l`.
    return a
    #The program returns the greatest common divisor of all numbers in list 'l'
#Overall this is what the function does:The function accepts a list of integers and returns the greatest common divisor (GCD) of all the numbers in the list. After executing the function, the program state is such that the variable `a` holds the GCD of all integers in the input list `l`.

