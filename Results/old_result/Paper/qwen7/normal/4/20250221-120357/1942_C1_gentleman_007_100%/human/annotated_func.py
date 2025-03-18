#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 * 10^5), and y = 0. The input for each test case consists of the first line containing n, x, and y, followed by the second line containing x distinct integers from 1 to n representing the chosen vertices. The sum of x over all test cases does not exceed 2 * 10^5.
def func_1():
    return map(int, input().split())
    #The program returns three integers: n, x, and y, where n is between 4 and 10^9, x is between 2 and the minimum of n or 2 * 10^5, and y is 0.
#Overall this is what the function does:The function reads input from the standard input, specifically three integers \( n \), \( x \), and \( y \) for each test case. These integers satisfy the conditions \( 4 \leq n \leq 10^9 \), \( 2 \leq x \leq \min(n, 2 \times 10^5) \), and \( y = 0 \). The function then returns these three integers as a result.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 * 10^5), and y = 0; the input for each test case consists of x distinct integers representing the vertices Bessie has chosen, where each integer is in the range from 1 to n; the sum of x over all test cases does not exceed 2 * 10^5.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of x distinct integers, each in the range from 1 to n, as input by the user.
#Overall this is what the function does:The function reads a series of test cases from user input. For each test case, it returns a list containing x distinct integers, each ranging from 1 to n, as specified by the user.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, v is a list of integers representing the vertices Bessie has chosen, and y is an integer representing the maximum number of other vertices that can be chosen.
def func_3(n, v):
    return [v for i in range(n)]
    #A list containing the elements of list 'v', repeated 'n' times
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing the number of sides of a polygon, and `v`, a list of integers representing the vertices Bessie has chosen. After executing, it returns a new list where the elements of list `v` are repeated `n` times.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, m is an integer representing the number of vertices Bessie has chosen (which is equal to x), and v is a list of m distinct integers representing the vertices Bessie has chosen.
def func_4(n, m, v):
    return [[v for i in range(m)] for i in range(n)]
    #A 2D list where each row contains the same m integers from the list v, repeated n times.
#Overall this is what the function does:The function accepts three parameters: `n` (representing the number of sides of a polygon), `m` (representing the number of vertices Bessie has chosen), and `v` (a list of `m` distinct integers representing the vertices Bessie has chosen). It returns a 2D list where each row contains the same `m` integers from the list `v`, repeated `n` times.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, m is an integer representing the number of vertices Bessie has chosen, and l is a list of empty lists with indices from 0 to n. The function `func_1()` is called m times, and for each call, it returns a pair of integers (x, y) where x and y are integers between 1 and n (inclusive), representing the vertices Bessie has chosen. These pairs are added to the corresponding lists in l, effectively creating an adjacency list representation of the graph formed by the chosen vertices.
def func_5(n, m):
    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x].append(y)
        
        l[y].append(x)
        
    #State: Output State: After the loop executes all its iterations, `l[y]` will contain `x` for each iteration where `i` ranges from 0 to `m-1`. The variable `n` remains an integer representing the number of sides of the polygon, `m` is an integer representing the number of vertices Bessie has chosen (and must be greater than 0), `i` will be equal to `m-1` after the last iteration, `x` will be the return value of `func_1()` for the current iteration, and `y` will be the second return value of `func_1()` for the current iteration.
    #
    #In simpler terms, after the loop completes, each list in `l` (from index 0 to `n`) will contain all the vertices that are connected to the corresponding index through the function `func_1()`. The variable `m` will reflect the total number of such connections made, and `i` will be set to `m-1`, indicating the last iteration of the loop.
    return l
    #The program returns a list `l` where each element `l[i]` (for i ranging from 0 to `n`), contains a list of tuples `(x, y)`, with `x` being the return value of `func_1()` and `y` being the second return value of `func_1()` for the current iteration of the loop. The variable `m` represents the number of vertices Bessie has chosen, which is also the length of each sublist in `l`, and `i` is set to `m-1`, indicating the last iteration of the loop.
#Overall this is what the function does:The function `func_5` accepts two parameters, `n` and `m`. `n` represents the number of sides of a polygon, while `m` represents the number of vertices Bessie has chosen. The function constructs an adjacency list representation of a graph based on the vertices chosen by Bessie. For each of the `m` iterations, `func_1()` is called to obtain a pair of integers `(x, y)` representing the vertices. These pairs are added to the corresponding lists in `l`, creating an adjacency list where `l[i]` contains all vertices connected to vertex `i`. The function returns the resulting adjacency list `l`, along with the value of `m` indicating the number of vertices chosen and `i` set to `m-1` to indicate the last iteration.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, m is an integer representing the number of vertices Bessie has chosen, and the function `func_1()` returns two integers x and y which are indices of the chosen vertices (1 ≤ x, y ≤ n and x ≠ y).
def func_6(n, m):
    l = [[(0) for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x][y] = 1
        
        l[y][x] = 1
        
    #State: Output State: After the loop executes all its iterations, `m` must be equal to the total number of iterations `k + 3`; `i` will be equal to `k + 3`; `x` and `y` will be the last pair of indices returned by `func_1()`, where `x` and `y` are between 1 and `n` and `x ≠ y`; `l[x][y]` and `l[y][x]` will both be set to 1.
    #
    #This means that the entire 2D list `l` will have `m` pairs of indices marked as 1, indicating that these pairs of vertices have been chosen. The final state of the list `l` will reflect all the pairs `(x, y)` that were returned by `func_1()` during the loop's execution.
    return l
    #The program returns a 2D list `l` with dimensions `k + 3` by `k + 3`, where `m` pairs of indices (x, y) are marked as 1, indicating that these pairs of vertices have been chosen. The value of `m` is equal to the total number of iterations `k + 3`. The variables `x` and `y` represent the last pair of indices returned by `func_1()`, where `x` and `y` are between 1 and `n` and `x ≠ y`.
#Overall this is what the function does:The function `func_6` accepts two parameters, `n` and `m`. `n` represents the number of sides of a polygon, and `m` represents the number of vertices Bessie has chosen. The function iterates `m` times, each time calling `func_1()` to get a pair of vertex indices `(x, y)` (where `1 ≤ x, y ≤ n` and `x ≠ y`). It then marks these pairs in a 2D list `l` by setting `l[x][y]` and `l[y][x]` to 1. After completing the iterations, the function returns the 2D list `l` with dimensions `m + 3` by `m + 3`, where `m` pairs of indices are marked as 1, indicating the chosen vertex pairs. The variables `x` and `y` represent the last pair of indices returned by `func_1()`.

#State of the program right berfore the function call: l is a list of integers where each integer represents a vertex chosen by Bessie, and the length of l is equal to x. The values in l are distinct and within the range from 1 to n.
def func_7(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    #State: The dictionary `d` contains keys for each unique element in the original list `l`, with the corresponding values being the count of how many times each element appeared in `l`. The list `l` is now an empty list since all its elements have been processed.
    return d
    #The program returns an empty dictionary 'd', since the list 'l' is now empty and there are no elements left to process.
#Overall this is what the function does:The function accepts a list of integers `l` and processes each integer by counting their occurrences, storing these counts in a dictionary `d`. After processing all elements in `l`, it returns the dictionary `d`, which contains each unique integer from `l` as keys and their respective counts as values. Finally, the function returns an empty dictionary because the original list `l` is emptied during the process.

#State of the program right berfore the function call: **
def func_8(l):
    n = len(l)
    m = len(l[0])
    p = [[(0) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
        
    #State: Output State: `j` is `m + 1`, `m` is at least 3, `p[i][j]` is the cumulative sum of all elements in the 2D list `p` up to the last row and column after the loop has executed all iterations.
    #
    #Explanation: The loop iterates over all possible values of `j` from 1 to `m + 1`. After completing all iterations, the variable `j` will reach `m + 1`, and the variable `i` will reach `n`. Each cell `p[i][j]` in the 2D list `p` is updated according to the formula `p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]`. This formula ensures that `p[i][j]` accumulates the sum of all elements in the 2D list `p` up to the current position `(i, j)`. Given that the loop runs for all values of `i` from 1 to `n` and `j` from 1 to `m + 1`, the final value of `p[i][j]` will be the total sum of all elements in the 2D list `p` up to the last row and column.
    return p
    #The program returns a 2D list `p` where each element `p[i][j]` (with `i` ranging from 1 to `n` and `j` ranging from 1 to `m + 1`) is the cumulative sum of all elements in the 2D list `p` up to the last row and column.
#Overall this is what the function does:The function accepts a 2D list `l` and returns a 2D list `p` where each element `p[i][j]` (with `i` ranging from 1 to `n` and `j` ranging from 1 to `m + 1`) is the cumulative sum of all elements in the 2D list `l` up to the last row and column.

#State of the program right berfore the function call: x is an integer such that 2 ≤ x ≤ min(n, 2 ⋅ 10^5), where n is the number of sides of the polygon.
def func_9(x):
    return max(1 - (x & x - 1), 0)
    #The program returns 0 if x is a power of 2, otherwise it returns 1.
#Overall this is what the function does:The function accepts an integer x within the range [2, min(n, 200000)], where n is the number of sides of a polygon. It checks whether x is a power of 2. If x is a power of 2, the function returns 0; otherwise, it returns 1.

#State of the program right berfore the function call: l is a list of positive integers, and the length of l is equal to x (the number of vertices Bessie has chosen).
def func_10(l):
    a = 0
    for i in l:
        a = gcd(a, i)
        
    #State: Output State: `a` is the greatest common divisor (gcd) of 0 and all elements in the list `l`; `i` is the last element in the list `l`.
    #
    #Explanation: After the loop has executed all its iterations, `a` will hold the gcd of 0 and all elements in the list `l`. Since the gcd of any number and 0 is 0 (except when the number itself is 0), and given that `a` starts as 0, `a` will remain 0 throughout the loop unless there is a non-zero element in `l` that changes it. However, since the initial value of `a` is 0, and the gcd of 0 with any positive integer is 0, `a` will stay 0 after all iterations. The variable `i`, which takes on each element of the list `l` in sequence, will be the last element of the list `l` after the loop completes.
    return a
    #The program returns 0, and the value of i is the last element in the list l.
#Overall this is what the function does:The function accepts a list of positive integers and calculates the greatest common divisor (GCD) of all elements in the list, starting with an initial value of 0. After the loop completes, the function returns 0, and the variable `i` holds the last element in the list `l`.

#State of the program right berfore the function call: num is a non-negative integer.
def func_11(num):
    prime = [(True) for i in range(num + 1)]
    Highest_Prime = [(0) for i in range(num + 1)]
    Lowest_Prime = [(0) for i in range(num + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p <= num:
        if prime[p] == True:
            Lowest_Prime[p] = p
            Highest_Prime[p] = p
            for i in range(2 * p, num + 1, p):
                prime[i] = False
                Highest_Prime[i] = p
                if Lowest_Prime[i] == 0:
                    Lowest_Prime[i] = p
        
        p += 1
        
    #State: Output State: `num`, `p`, `prime`, `Highest_Prime`, and `Lowest_Prime` retain their final states after the loop completes its execution; `p` is set to `num + 1`.
    #
    #In Natural Language: After all iterations of the loop, the variable `p` will be set to `num + 1` because the loop continues to increment `p` until it exceeds `num`. All indices `i` for which `2 * p` is less than or equal to `i` and `i` is less than or equal to `num` will have their corresponding `prime[i]` value set to `False`. For these indices, `Highest_Prime[i]` will be set to the last value of `p` that satisfied `p + 1 <= num` during the loop's execution, and `Lowest_Prime[i]` will be set to `p` if it was `0` previously; otherwise, it remains unchanged. The variables `prime`, `Highest_Prime`, and `Lowest_Prime` will be fully updated according to the loop's operations, with `prime[i]` being `False` for all composite numbers up to `num` and `True` for all primes, and `Highest_Prime[i]` and `Lowest_Prime[i]` reflecting the highest and lowest prime factors of `i` respectively.
    p = []
    for i in range(num + 1):
        if prime[i]:
            p.append(i)
        
    #State: After all iterations of the loop, `p` will contain all prime numbers less than or equal to `num`. The variable `i` will be equal to `num + 1`, and `prime`, `Highest_Prime`, and `Lowest_Prime` will be fully updated according to the loop's operations.
    return p
    #The program returns a list 'p' containing all prime numbers less than or equal to 'num', with 'i' set to 'num + 1'
#Overall this is what the function does:The function accepts a non-negative integer `num` and returns a list `p` containing all prime numbers less than or equal to `num`. After processing, the variable `i` (which is `num + 1`) is set to `num + 1`.

#State of the program right berfore the function call: num is a positive integer, and Prime_array is a dictionary where keys are prime numbers and values are the corresponding prime factors of num.
def func_12(num, Prime_array):
    d = {}
    while num != 1:
        x = Prime_array[num]
        
        d[x] = d.get(x, 0) + 1
        
        num //= x
        
    #State: Output State: `num` equals 1, `Prime_array` is a dictionary where keys are prime numbers and values are the corresponding prime factors of the original `num`, `d` is a dictionary where each key is a prime factor of the original `num` and its value is the total count of that prime factor in the prime factorization of the original `num`.
    #
    #Explanation: After the loop completes all its iterations, `num` will eventually become 1 because the loop continues as long as `num` is not equal to 1. During each iteration, the code updates the dictionary `d` to keep track of the count of each prime factor found in `Prime_array[num]`. The variable `x` is updated to the next prime factor of `num` until `num` is reduced to 1. Therefore, when the loop finishes, `d` contains the complete prime factorization of the original `num`, with each prime factor's count accurately recorded.
    return d
    #The program returns a dictionary `d` where each key is a prime factor of the original `num` and its value is the total count of that prime factor in the prime factorization of the original `num`.
#Overall this is what the function does:The function accepts two parameters: `num`, a positive integer, and `Prime_array`, a dictionary where keys are prime numbers and values are the corresponding prime factors of `num`. It returns a dictionary `d` where each key is a prime factor of the original `num` and its value is the total count of that prime factor in the prime factorization of the original `num`. After executing, the function fully decomposes `num` into its prime factors and counts their occurrences, storing these in the returned dictionary `d`.

#State of the program right berfore the function call: n is an integer such that 4 <= n <= 10^9, x is an integer such that 2 <= x <= min(n, 2 * 10^5), and y is an integer such that y = 0.
def func_13(n):
    d = {}
    x = 2
    while x * x <= n:
        while n % x == 0:
            d[x] = d.get(x, 0) + 1
            n //= x
        
        x += 1
        
    #State: Output State: `x` is greater than the largest prime factor of the initial `n`, `n` is 1, `y` is 0, and `d` contains the count of each prime factor of the initial `n`.
    #
    #Explanation: The loop continues to increment `x` starting from 2 and checks if `x` is a factor of `n`. If `x` divides `n` evenly, it updates the dictionary `d` to keep track of the count of divisions by `x` and then reduces `n` by dividing it by `x`. This process repeats until `x * x` is no longer less than or equal to `n`. Since the loop increments `x` to the next integer each time, it will eventually check all integers up to the largest prime factor of `n`. Once `x` exceeds the largest prime factor and `n` is reduced to 1 (since all factors have been divided out), the loop terminates. At this point, `d` will contain the prime factorization of the initial `n`, with each prime factor's count as its value.
    if (n > 1) :
        d[n] = d.get(n, 0) + 1
    #State: `x` is greater than the largest prime factor of the initial `n`, `n` is 1, `y` is 0, and `d` contains the prime factorization of the initial `n` with each prime factor's count as its value.
    return d
    #The program returns a dictionary 'd' which contains the prime factorization of the initial 'n', where 'n' is 1. Since 1 does not have any prime factors, the dictionary 'd' is empty.
#Overall this is what the function does:The function accepts an integer `n` within the range of 4 to \(10^9\) and returns a dictionary `d`. This dictionary contains the prime factorization of the initial `n`, where each key is a prime factor and its corresponding value is the count of that prime factor in the factorization. If `n` is reduced to 1 after the factorization process, the dictionary `d` will be empty, indicating that 1 has no prime factors.

#State of the program right berfore the function call: d is a dictionary where keys are integers from 1 to n and values are non-negative integers. The sum of x over all test cases does not exceed 2 * 10^5.
def func_14(d):
    s = 0
    for i in d:
        s += pow(i, d[i] - 1) * (i - 1)
        
    #State: Output State: The final value of `s` will be the sum of `pow(i, d[i] - 1) * (i - 1)` for every key `i` in the dictionary `d`.
    #
    #In more detail, after the loop has executed all its iterations, the variable `s` will hold the cumulative result of applying the expression `pow(i, d[i] - 1) * (i - 1)` to each key `i` in the dictionary `d`. This means `s` will be the sum of these computed values for all keys from 1 to `n`.
    return s
    #The program returns the sum of `pow(i, d[i] - 1) * (i - 1)` for every key `i` in the dictionary `d`
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers from 1 to `n` and values are non-negative integers. It calculates and returns the sum of `pow(i, d[i] - 1) * (i - 1)` for every key `i` in the dictionary `d`.

#State of the program right berfore the function call: n is an integer such that 4 <= n <= 10^9, x is an integer such that 2 <= x <= min(n, 2 * 10^5), and y is an integer such that y = 0.
def func_15(n, mod):
    f = [1]
    for i in range(1, n + 1):
        f.append(f[i - 1] * i % mod % mod)
        
    #State: Output State: The list `f` will contain `n+1` elements, with each element `f[i]` being equal to `(i! % mod)`, where `i` ranges from `0` to `n`. The variable `i` will be equal to `n+1`.
    #
    #Explanation: After the loop completes all its iterations, the variable `i` will be set to `n + 1` because the loop runs from `1` to `n` inclusive. The list `f` will have been updated to include the factorial of each integer from `0` to `n`, modulo `mod`, as specified by the loop body. Each iteration appends `f[i-1] * i % mod % mod` to the list `f`, effectively building up the factorial sequence modulo `mod`.
    return f
    #The program returns a list `f` containing `n+1` elements, where each element `f[i]` is equal to `(i! % mod)` for `i` ranging from `0` to `n`. Additionally, the variable `i` is set to `n + 1`.
#Overall this is what the function does:The function accepts two parameters, `n` and `mod`. It calculates the factorial of each integer from `0` to `n` (inclusive), taking the result modulo `mod`, and stores these values in a list `f`. After completing the calculations, the function returns the list `f`. Additionally, the loop variable `i` is set to `n + 1`.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, x is an integer representing the number of vertices Bessie has chosen, and y is an integer representing the maximum number of additional vertices that can be chosen. Additionally, n, x, and y satisfy the constraints 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 ⋅ 10^5), and y = 0.
def func_16(n, mod):
    if (mod == -1) :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) * (dearr[i - 1] + dearr[i - 2]))
            
        #State: Output State: The list `dearr` contains elements calculated based on the loop iterations until `i` equals `n + 1`. Specifically, each element in `dearr` from index 2 up to `n` is computed as `(i - 1) * (dearr[i - 1] + dearr[i - 2])`. The final state of `dearr` will have `n` elements, starting with `[1, 0]` and then each subsequent element following the given formula.
        #
        #For example, if `n` is 5, the final `dearr` list would be `[1, 0, 1, 1, 3]`, where:
        #- `dearr[0]` is 1,
        #- `dearr[1]` is 0,
        #- `dearr[2]` is `1 * (dearr[1] + dearr[0]) = 1`,
        #- `dearr[3]` is `2 * (dearr[2] + dearr[1]) = 1`,
        #- `dearr[4]` is `3 * (dearr[3] + dearr[2]) = 3`.
        #
        #This pattern continues until the loop completes, resulting in a list of length `n + 1` with the initial two elements being `[1, 0]` and the rest following the recursive formula provided.
    else :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod)
            
        #State: Output State: The list `dearr` will contain `n` elements, starting from `[1, 0]` and each subsequent element calculated as \((i - 1) \% \text{mod} \times (\text{dearr}[i - 1] + \text{dearr}[i - 2]) \% \text{mod} \% \text{mod}\), where `i` ranges from 3 to `n`. The final value of `i` will be `n + 1`, and `n` must be greater than or equal to 4.
        #
        #In simpler terms, after the loop completes all its iterations, the list `dearr` will have `n` elements, starting with `[1, 0]` and each following element is computed based on the formula given in the loop body. The loop runs until `i` reaches `n + 1`, meaning it will run `n - 1` times if `n` is greater than or equal to 4.
    #State: `dearr` is a list of length `n + 1`, starting with `[1, 0]` and each subsequent element from index 2 to `n` is computed as `(i - 1) \% \text{mod} \times (\text{dearr}[i - 1] + \text{dearr}[i - 2]) \% \text{mod}`, where `i` ranges from 3 to `n + 1`.
    return dearr
    #The program returns a list `dearr` of length `n + 1`, starting with `[1, 0]` and each subsequent element from index 2 to `n` is computed as `(i - 1) \% \text{mod} \times (\text{dearr}[i - 1] + \text{dearr}[i - 2]) \% \text{mod}`, where `i` ranges from 3 to `n + 1`.
#Overall this is what the function does:The function `func_16` accepts two parameters, `n` and `mod`. It returns a list `dearr` of length `n + 1`, starting with `[1, 0]`. For each index `i` from 3 to `n + 1`, the value of `dearr[i]` is calculated as `(i - 1) \% mod \times (dearr[i - 1] + dearr[i - 2]) \% mod`. The final state of the program after the function concludes is that it returns this list `dearr`.

#State of the program right berfore the function call: p is a sorted list of integers, x is an integer such that 1 <= x <= n where n is the number of sides of the polygon.
def func_17(p, x):
    i = bisect_left(p, x)
    if (i != len(p) and p[i] == x) :
        return i
        #The program returns the index `i` where the integer `x` is currently located in the sorted list `p`.
    else :
        return -1
        #The program returns -1
#Overall this is what the function does:The function accepts a sorted list of integers `p` and an integer `x`. It searches for the integer `x` in the list `p` and returns the index `i` where `x` is found, or returns `-1` if `x` is not present in `p`.

#State of the program right berfore the function call: p is a sorted list of integers, x is an integer such that 1 ≤ x ≤ max(p), and the length of p is n (2 ≤ n ≤ 200000).
def func_18(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[0] > x) :
        return -1
        #The program returns -1
    #State: Postcondition: `l` is 0, `r` is `n - 1`, `p` is a sorted list of integers, `x` is an integer such that 1 ≤ `x` ≤ max(`p`), and `n` is the length of `p`. The first element of `p` is less than or equal to `x`.
    while l <= r:
        mid = (l + r) // 2
        
        if p[mid] <= x:
            if mid != n - 1:
                if p[mid + 1] > x:
                    break
                else:
                    l = mid + 1
            else:
                mid = n - 1
                break
        else:
            r = mid - 1
        
    #State: Output State: `l` is an integer, `r` is an integer, and `mid` is (0 + `r`) // 2. The loop continues to execute until either `l` exceeds `r` or the conditions inside the while loop no longer satisfy the given criteria. At the end of the loop, one of two scenarios will occur:
    #
    #- The loop breaks when `p[mid] <= x` and either `mid` is `n - 1` or `p[mid + 1] > x`.
    #- The loop breaks when `p[mid] > x` and `mid` is `n - 1`.
    #
    #In both cases, the final value of `l` will be the index where `p[l]` is the largest value less than or equal to `x`, or `l` will be `n` if no such value exists. The value of `r` will be the index just before the first element in `p` that is greater than `x`, or `r` will be `-1` if no such value exists. The variable `mid` will hold the last computed midpoint during the loop's execution.
    return mid
    #The program returns `mid`, which is the last computed midpoint during the loop's execution, and satisfies the condition that `p[mid]` is the largest value less than or equal to `x`, or `mid` is `n - 1` if no such value exists.
#Overall this is what the function does:The function accepts a sorted list of integers `p` and an integer `x` where 1 ≤ x ≤ max(p). It searches for the largest value in `p` that is less than or equal to `x`. If such a value exists, it returns its index; otherwise, it returns -1.

#State of the program right berfore the function call: p is a list of integers representing the chosen vertices, x is an integer representing the target value, and the length of p is equal to x.
def func_19(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[-1] < x) :
        return n
        #The program returns the integer `n`
    #State: `l` is 0; `r` is `n - 1`; `p` is a list of integers representing the chosen vertices; `x` is an integer representing the target value; `p[-1]` is greater than or equal to `x`
    while l <= r:
        mid = (l + r) // 2
        
        if p[mid] >= x:
            if mid != 0:
                if p[mid - 1] < x:
                    break
                else:
                    r = mid - 1
            else:
                mid = 0
                break
        else:
            l = mid + 1
        
    #State: Output State: `l` is 0, `r` is `n - 1`, `mid` is the final calculated midpoint, `p` is a list of integers representing the chosen vertices, `x` is an integer representing the target value, and `p[mid]` is either the smallest element in `p` that is greater than or equal to `x` or `r` becomes less than `l` indicating the target value `x` is not present in the list `p`.
    #
    #Explanation: After all iterations of the loop, the variable `l` will be greater than `r` because the loop condition `l <= r` will no longer hold true. The variable `mid` will be the last calculated midpoint during the loop's execution. The list `p` and the integer `x` will retain their values from the last iteration. The value of `p[mid]` will be the smallest element in the list `p` that is greater than or equal to `x`, or the loop will terminate when `l` exceeds `r`, indicating that `x` is not found in the list `p`.
    return mid
    #`mid` is the last calculated midpoint during the loop's execution, and the program returns this value.
#Overall this is what the function does:The function accepts a list `p` of integers and an integer `x`. If the last element of the list `p` is less than `x`, it returns the length of the list `p`. Otherwise, it performs a binary search to find the smallest element in the list `p` that is greater than or equal to `x`, and returns the index of this element.

#State of the program right berfore the function call: x is a non-negative integer.
def func_20(x):
    if (x == 0 or x == 1) :
        return x
        #The program returns 0 or 1
    #State: x is a non-negative integer larger than 1
    l = 1
    r = x
    while l <= r:
        mid = (l + r) / 2
        
        y = mid * mid
        
        if y > x:
            r = mid - 1
        elif y == x:
            return mid
        elif (mid + 1) * (mid + 1) > x:
            return mid
        else:
            l = mid + 1
        
    #State: Output State: `x` is a non-negative integer larger than 1; `l` is either 1 or any value between `mid + 1` and `mid + k` where `k` is a non-negative integer; `r` is either `x` or `x - 1`; `mid` is now `(l + r) / 2`; `y` is `mid * mid`. If `y > x`, then `r` is set to `x - 1`. If `y == x`, the function returns `mid`. Otherwise, if `(mid + 1) * (mid + 1) > x`, the function returns `mid`. If none of the above conditions are met, `l` is set to `mid + 1`, `mid` is now `(l + r) / 2`, and `y` is `mid * mid`.
    #
    #In simpler terms, after the loop has executed all its iterations, `x` remains a non-negative integer larger than 1. The variable `l` will be within a certain range depending on the final adjustments made during the loop, and `r` will be either `x` or `x - 1`. The value of `mid` will be recalculated as `(l + r) / 2` in each iteration until it meets one of the stopping conditions: either `y` equals `x`, in which case `mid` is returned, or `y` is greater than `x` and `(mid + 1) * (mid + 1)` is not greater than `x`, in which case `mid` is also returned. If neither condition is met, the loop continues adjusting `l` and `r` until it terminates.
#Overall this is what the function does:The function accepts a non-negative integer x and returns either 0 or 1 if x is 0 or 1. Otherwise, it returns the largest integer whose square is less than or equal to x. This is achieved through a binary search-like process where the function adjusts the search range (using variables l and r) to find the appropriate integer. The function guarantees that upon completion, it will have found and returned the correct integer value based on the conditions specified.

#State of the program right berfore the function call: a is an integer, b is a non-negative integer, and mod is a positive integer.
def func_21(a, b, mod):
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        
        a = a * a % mod
        
        b >>= 1
        
    #State: Output State: `a` is now `(a * a) % mod` raised to the power of the binary representation of `b` (i.e., `a^b % mod`), `b` is now `0`, `ans` is the final result of multiplying `ans` by `a` modulo `mod` for each odd bit in the binary representation of `b`.
    #
    #This means that after the loop completes all its iterations, `a` will be `a` raised to the power of `b` modulo `mod`, and `b` will be reduced to `0` since the loop continues as long as `b` is non-zero. The variable `ans` will hold the product of `a` raised to the power of each bit position in `b` where the bit is `1`, all taken modulo `mod`.
    return ans
    #`ans` is the result of multiplying `a` raised to the power of each bit position in `b` where the bit is 1, all taken modulo `mod`. Since `b` is 0, `a` remains `(a * a) % mod` and `ans` is 1 because any number raised to the power of 0 is 1.
#Overall this is what the function does:The function accepts three parameters: `a`, an integer; `b`, a non-negative integer; and `mod`, a positive integer. It calculates the result of raising `a` to the power of each bit position in `b` where the bit is 1, all taken modulo `mod`. If `b` is 0, the function returns 1 because any number raised to the power of 0 is 1. The final result is stored in `ans` and returned by the function.

#State of the program right berfore the function call: a is a string representing the vertices Bessie has chosen, b is a list of integers representing the vertices that can be used to form diagonals, and y is an integer representing the maximum number of other vertices you can choose.
def func_22(a, b):
    dp = [([0] * (len(b) + 1)) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
    #State: Output State: The loop will execute until `i` reaches `len(a) + 1` and `j` reaches `len(b) + 1`. After all iterations, `i` will be `len(a) + 1`, `j` will be `len(b) + 1`, and the `dp` table will be completely filled. Each cell `dp[i][j]` will contain the length of the longest common subsequence (LCS) between the first `i-1` elements of list `a` and the first `j-1` elements of list `b`. Specifically, `dp[len(a) + 1][len(b) + 1]` will hold the length of the LCS of the entire strings `a` and `b`. All other cells in the `dp` table will reflect the lengths of common subsequences up to the indices `i-1` and `j-1` of lists `a` and `b`, respectively.
    i, j = len(a), len(b)
    l = []
    while i != 0 and j != 0:
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            i -= 1
            j -= 1
            l.append(a[i])
        
    #State: Output State: `i` and `j` are both zero, and `l` is a list containing elements from `a` that correspond to the path traced by decrementing `i` and `j` according to the conditions inside the loop until both `i` and `j` reach zero.
    #
    #In more detail, the loop continues to run as long as both `i` and `j` are non-zero. Each iteration of the loop either decrements `i` and/or `j` based on the comparison of `dp[i][j]` with its neighboring cells (`dp[i][j - 1]` and `dp[i - 1][j]`). The list `l` accumulates elements from `a` corresponding to the indices where `i` was decremented. Once both `i` and `j` become zero, the loop terminates, leaving `i` and `j` as zero and `l` as the final list constructed during the loop's execution.
    s = ''.join(l)
    return s[::-1]
    #The program returns the reversed string 's' which is formed by joining the elements of list 'l'
#Overall this is what the function does:The function accepts a string `a` and a list of integers `b`. It calculates the longest common subsequence (LCS) between the string `a` and the sequence represented by the list `b`. After constructing a list `l` containing elements from `a` that form part of the LCS, it reverses the list `l` and returns the reversed string.

#State of the program right berfore the function call: arr is a list of integers.
def func_23(arr):
    l = []
    for i in arr:
        pos = bisect_left(l, i)
        
        if pos == len(l):
            l.append(i)
        else:
            l[pos] = i
        
    #State: The list `arr` is fully processed, and `l` is a sorted version of `arr`.
    return len(l)
    #The program returns the length of the sorted list 'l', which is the number of elements in the original list 'arr'
#Overall this is what the function does:The function accepts a list of integers `arr` and returns the count of unique, sorted elements from `arr`. It achieves this by iterating through each element in `arr`, maintaining a sorted list `l` of encountered elements, and updating `l` to ensure it remains sorted. Finally, it returns the length of `l`, which represents the number of unique elements in the original list `arr`.

#State of the program right berfore the function call: ver is an integer representing a vertex of the polygon, and graph is a dictionary where keys are vertices and values are lists of adjacent vertices. Additionally, vis is a list or array of boolean values indicating whether a vertex has been visited, with the same length as the number of sides of the polygon (n).
def func_24(ver):
    stack = []
    stack.append(ver)
    vis[ver] = 1
    while len(stack):
        ver = stack.pop()
        
        print(ver, end=' ')
        
        for node in graph[ver]:
            if not vis[node]:
                stack.append(node)
                vis[node] = 1
        
    #State: All nodes in the graph have been visited, `stack` is empty, `vis[node]` is set to 1 for every node in the graph.
#Overall this is what the function does:The function processes a polygon represented by a graph, starting from a given vertex. It performs a depth-first search (DFS) traversal, visiting all vertices connected to the initial vertex and marking them as visited. After completing the traversal, all vertices in the graph are marked as visited, and the function prints the order in which the vertices were visited.

#State of the program right berfore the function call: ver is an integer representing a vertex in the graph, and graph is a dictionary where keys are vertices and values are lists of adjacent vertices. The variable vis is a list or array of boolean values used to keep track of visited vertices, with the same length as the number of vertices in the graph.
def func_25(ver):
    q = deque()
    q.append(ver)
    vis[ver] = 1
    while len(q):
        ver = q.popleft()
        
        print(ver, end=' ')
        
        for node in graph[ver]:
            if not vis[node]:
                q.append(node)
                vis[node] = 1
        
    #State: Output State: All nodes that are reachable from the starting node (`ver`) have been visited (`vis[node] == 1` for all reachable nodes), and the queue `q` is empty. The graph `graph[ver]` does not contain any unvisited nodes, indicating that the entire connected component of the starting node has been fully processed.
#Overall this is what the function does:The function performs a breadth-first search (BFS) starting from the given vertex `ver`. It marks all vertices reachable from `ver` as visited in the `vis` list and prints the visited vertices in the order they were visited. The function does not return any value but modifies the `vis` list to indicate visited nodes.

