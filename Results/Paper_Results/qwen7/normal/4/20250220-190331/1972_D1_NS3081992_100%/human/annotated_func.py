#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from standard input within the range 1 to 10^4.
#Overall this is what the function does:The function reads an integer from standard input within the range 1 to 10^4 and returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns two integers, `n` and `m`, read from standard input, where both `n` and `m` are within the range 1 to 2 * 10^6.
#Overall this is what the function does:The function reads two integers, `n` and `m`, from standard input, where both `n` and `m` are within the range 1 to 2 * 10^6, and returns these two integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, where the first integer is the value of 'n' and the second integer is the value of 'm' for each test case.
#Overall this is what the function does:The function reads a line of input from the standard buffer, splits it into two integers, and returns them as a list. Specifically, it returns a list containing the values of 'n' and 'm' for each test case, where both 'n' and 'm' are integers within the specified range.

#State of the program right berfore the function call: rows_number is a positive integer such that 1 ≤ rows_number ≤ 10^4.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the result of func_3() called `rows_number` times
#Overall this is what the function does:The function accepts a positive integer `rows_number` (where 1 ≤ rows_number ≤ 10^4) and returns a list containing the result of calling another function `func_3()` exactly `rows_number` times.

#State of the program right berfore the function call: None of the variables in the function `func_5()` are defined or used within the provided function signature or body. The function reads a single line from standard input, trims the whitespace from the end of the line, and returns it.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program reads a line from standard input, trims the whitespace from the end of the line, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string read from standard input, stripped of trailing whitespace, and decoded from bytes to a string.
#Overall this is what the function does:The function reads a line of input from the standard input, removes any trailing whitespace, and decodes it from bytes to a string before returning it. This process ensures that the returned value is a clean string suitable for further processing.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is obtained by splitting a space-separated string input from the user.
#Overall this is what the function does:The function reads a space-separated string of integers from the user input and returns a list containing these integers.

#State of the program right berfore the function call: rows is a non-negative integer representing the number of rows for which to generate results using func_7().
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list containing the results of calling func_7() for each row in the range from 0 to rows-1
#Overall this is what the function does:The function `func_8` accepts a non-negative integer `rows` and generates a list containing the results of calling `func_7()` for each row in the range from 0 to `rows-1`. The final state of the program is a list of these results.

#State of the program right berfore the function call: There is no input parameter for the function, and it is expected to read input from the standard input stream. The input consists of multiple lines, where the first line contains the number of test cases t, followed by t lines, each containing two space-separated integers n and m.
def func_9():
    return input()
    #The program reads and returns t lines of input, each containing two space-separated integers n and m.
#Overall this is what the function does:The function reads and processes input from the standard input stream. Specifically, it reads the first line to determine the number of test cases \( t \), and then reads \( t \) additional lines, each containing two space-separated integers \( n \) and \( m \). The function does not accept any parameters and returns nothing.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given code snippet. The function `func_10` does not take any parameters.
def func_10():
    return int(input())
    #The program returns an integer input provided by the user.
#Overall this is what the function does:The function `func_10` accepts no parameters and returns an integer input provided by the user.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_11():
    return input().split()
    #The program returns a list of strings containing the values of `n` and `m` separated by spaces.
#Overall this is what the function does:The function reads input from the standard input, splits it into two parts, and returns them as a list of strings. The list contains the values of `n` and `m`, which are separated by spaces.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of length max(da) containing only 0s and 1s indicating whether a node has been processed or not; da is an integer representing a key in the dictionary d; rank is a list of integers with the same length as the maximum value in d's keys, initialized to 0s.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: Postcondition: `tmp` is 1000000000, `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of length max(da) containing only 0s and 1s indicating whether a node has been processed or not, `da` is an integer representing a key in the dictionary `d`, `rank` is a list of integers with the same length as the maximum value in `d`'s keys, initialized to 0s, and the length of `d[da]` is not equal to 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: Postcondition: `tmp` is updated to the minimum value between its current value and the result of `func_12(d, processing, di, rank)` for every `di` in `d[da]`, and all elements in `processing` are set to 0.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of `tmp + 1`, where `tmp` was used to update `rank[da - 1]` to `tmp + 1` and all elements in `processing` were set to 0.
#Overall this is what the function does:The function processes a dictionary `d` where keys are integers and values are lists of integers, a list `processing` indicating processed nodes, an integer `da` as a key in `d`, and a list `rank` initialized to zeros. It returns either 1 or `tmp + 1`. If the length of `d[da]` is 1, it returns 1 immediately. Otherwise, it recursively updates `tmp` to the minimum value among the results of calling itself for each node in `d[da]` that hasn't been processed, then sets `rank[da - 1]` to `tmp + 1` and all elements in `processing` to 0 before returning `tmp + 1`.

#State of the program right berfore the function call: a and b are positive integers such that \(1 \leq a \leq n\), \(1 \leq b \leq m\), and \(b \neq 0\).
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x which is 1, y which is 0, and a which is within the range 1 to n.
    #State: a and b are positive integers such that \(1 \leq a \leq n\), \(1 \leq b \leq m\), and \(b \neq 0\)
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, g
#Overall this is what the function does:The function accepts two parameters, `a` and `b`, both of which are positive integers with specific constraints (1 ≤ a ≤ n, 1 ≤ b ≤ m, and b ≠ 0). It returns either (1, 0, a) if `b` is 0, or (y, x - a // b * y, g) where `x` and `y` are calculated based on the Extended Euclidean Algorithm.

#State of the program right berfore the function call: a is a list of integers, n and m are non-negative integers such that 0 <= n and 0 <= m, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: Output State: After the loop executes all its iterations, `i` will be equal to `n`, `k` will be updated by subtracting `m - a[j]` for each `j` from `0` to `n-1` if `a[j] < m`, and `n` must have been greater than 0 for the loop to execute.
    #
    #In simpler terms, after the loop completes all its iterations, the variable `i` will have the value `n`, indicating that the loop has processed all elements in the list `a`. The variable `k` will have been adjusted by subtracting `m - a[j]` for each element `a[j]` in the list `a` where `a[j]` is less than `m`. Additionally, the loop would only run if `n` was initially greater than 0.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: `i` will be equal to `n`, `k` will be updated by subtracting `m - a[j]` for each `j` from `0` to `n-1` if `a[j] < m`, and `n` must have been greater than 0 for the loop to execute, but `k` is less than 0
    return -1
    #The program returns -1
#Overall this is what the function does:The function processes a list of integers `a` and updates the integer `k` based on the values in `a` compared to `m`. If `k` is non-negative after processing all elements in `a`, the function returns 1; otherwise, it returns -1.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6 and the product of n and m does not exceed 2⋅10^6.
def func_15():
    n, m = func_7()
    i = 1
    ans = 0
    while i <= m and i * i <= n + i:
        ans += (n + i) // (i * i)
        
        i += 1
        
    #State: Output State: `i` is greater than `m` or `i * i > n + i`, `n` is a positive integer, `m` is a positive integer, `ans` is the sum of `(n + j) // (j * j)` for all `j` from 2 to the final value of `i` (inclusive).
    #
    #To explain this output state in natural language:
    #After the loop has executed all its iterations, the variable `i` will either be greater than `m` or `i * i` will be greater than `n + i`. The variable `n` remains a positive integer, and `m` remains a positive integer. The variable `ans` contains the cumulative sum of the expression `(n + j) // (j * j)` for each `j` starting from 2 up to the final value of `i` that satisfies the loop condition.
    return ans - 1
    #The program returns the sum of `(n + j) // (j * j)` for all `j` from 2 to the final value of `i` that satisfies `i > m` or `i * i > n + i`, minus 1.
#Overall this is what the function does:The function takes no parameters and returns the sum of \((n + j) // (j * j)\) for all integers \(j\) from 2 to the largest integer \(i\) such that \(i \leq m\) and \(i * i \leq n + i\), minus 1.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_16():
    for _ in range(func_10()):
        sys.stdout.write(str(func_15()) + '\n')
        
    #State: Output State: The loop will execute a total number of times equal to the value returned by `func_10()`. For each iteration, `func_15()` will return a positive integer, which will be written to the standard output followed by a newline character. After all iterations, the standard output will contain each positive integer returned by `func_15()` on a new line, with the number of lines being equal to the value returned by `func_10()`.
    #
    #This means that if `func_10()` returns a value `k`, then the standard output will consist of `k` lines, each containing a positive integer as returned by `func_15()`.
#Overall this is what the function does:The function processes an unspecified number of test cases. For each test case, it calls `func_10()` to determine the number of iterations. Then, for each iteration, it calls `func_15()` to get a positive integer, which is printed to the standard output followed by a newline. After processing all test cases, the standard output contains multiple lines, each with a positive integer generated by `func_15()`, with the number of lines corresponding to the sum of the values returned by `func_10()` across all test cases.

