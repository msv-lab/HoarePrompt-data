#State of the program right berfore the function call: None of the variables in the provided function have any input parameters or preconditions mentioned. However, it appears that the function should be part of a larger program that reads input and prints output based on the problem description. The function `func_1` reads an integer from standard input.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from standard input.
#Overall this is what the function does:The function reads an integer from standard input and returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers read from the standard input, split by spaces.
#Overall this is what the function does:The function reads integers from the standard input, splits them based on spaces, and returns a map object containing these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, where the first integer is the value of n and the second integer is the value of m for each test case.
#Overall this is what the function does:The function reads a line of input from the standard buffer, splits it into two integers, and returns them as a list. Specifically, it returns a list containing the values of n and m, where both n and m are integers satisfying 1 ≤ n, m ≤ 2 ⋅ 10^6 for each test case.

#State of the program right berfore the function call: rows_number is a non-negative integer representing the number of test cases.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the result of func_3() called `rows_number` times
#Overall this is what the function does:The function accepts a non-negative integer `rows_number` representing the number of times to call `func_3()`. It returns a list containing the results of calling `func_3()` exactly `rows_number` times.

#State of the program right berfore the function call: `t` is an integer representing the number of test cases, and for each test case, `n` and `m` are integers such that 1 ≤ n, m ≤ 2 * 10^6. The values of `n` and `m` are read from standard input using `func_5()` which returns a string that needs to be stripped of trailing whitespace.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that represents the number of test cases (`t`) stripped of any trailing whitespace.
#Overall this is what the function does:The function reads the number of test cases (`t`) from standard input, strips any trailing whitespace from the input string, and returns this value as a string. This function effectively initializes the number of test cases for subsequent processing.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string decoded from bytes read from standard input buffer, which is stripped of trailing whitespace.
#Overall this is what the function does:The function reads a line of input from the standard input buffer, decodes it from bytes to a string, and removes any trailing whitespace before returning the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is obtained from splitting the input string on spaces and converting each element to an integer.
#Overall this is what the function does:The function reads a space-separated list of integers from standard input and returns it as a list. The input must be formatted as a single line of integers separated by spaces.

#State of the program right berfore the function call: rows is a non-negative integer such that 0 <= rows.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list containing the result of func_7() called `rows` times
#Overall this is what the function does:The function accepts a non-negative integer `rows` and returns a list containing the result of calling the function `func_7()` exactly `rows` times.

#State of the program right berfore the function call: There is no input parameter for the function, and it is expected to handle multiple test cases as described in the problem statement. Each test case consists of two integers n and m, where 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6. The function should read the number of test cases from standard input, followed by the values of n and m for each test case, and print the number of valid pairs for each test case.
def func_9():
    return input()
    #The program returns the number of test cases from standard input, followed by the values of n and m for each test case.
#Overall this is what the function does:The function reads the number of test cases from standard input, then for each test case, it reads the values of n and m. It does not perform any calculations or print any results within the function itself; instead, it waits for the input values and returns them as specified.

#State of the program right berfore the function call: None of the variables in the function `func_10()` are described in the function signature or used within the function itself. This suggests that the function does not take any parameters and returns an integer obtained from user input.
def func_10():
    return int(input())
    #The program returns an integer entered by the user.
#Overall this is what the function does:The function accepts no parameters and returns an integer value entered by the user.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6, and the sum of n or m over all test cases does not exceed 2⋅10^6.
def func_11():
    return input().split()
    #The program returns a list of strings obtained from splitting the input string at whitespace boundaries.
#Overall this is what the function does:The function accepts no parameters and returns a list of strings obtained from splitting an input string at whitespace boundaries.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of length equal to the maximum key in d, containing only 0s and 1s indicating whether a node has been processed; da is an integer representing a key in the dictionary d; rank is a list of integers with the same length as the maximum key in d, initialized to 0s.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: Postcondition: `tmp` is 1000000000, `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of length equal to the maximum key in `d`, containing only 0s and 1s indicating whether a node has been processed, `da` is an integer representing a key in the dictionary `d`, `rank` is a list of integers with the same length as the maximum key in `d`, initialized to 0s, and the length of `d[da]` is not equal to 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `tmp` is the minimum value obtained from `func_12(d, processing, di, rank)` for all `di` in `d[da]` where `processing[di - 1]` was initially 0. The `processing` list is modified during the loop but reverts back to its original state at the end of each iteration. The `rank` list remains unchanged, and all other variables retain their initial states.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of `rank[da - 1]` which is `tmp + 1`
#Overall this is what the function does:The function processes a dictionary `d` where keys are integers and values are lists of integers, a list `processing` indicating whether nodes have been processed, an integer `da` representing a key in `d`, and a list `rank` initialized to zeros. It returns 1 if the length of `d[da]` is 1, otherwise, it recursively calculates the minimum value of `tmp + 1` for all unprocessed nodes connected to `da`, updates the `rank` list accordingly, and returns the calculated value.

#State of the program right berfore the function call: a and b are positive integers such that 1 <= a, b <= 2 * 10^6 and b != 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x which is 1, y which is 0, and a which is a positive integer.
    #State: a and b are positive integers such that 1 <= a, b <= 2 * 10^6 and b != 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, and g, where y, x, and g are the results of the func_13(b, a % b) function call.
#Overall this is what the function does:The function `func_13` accepts two positive integers `a` and `b` (1 ≤ a, b ≤ 2 * 10^6 and b ≠ 0) and returns three values: `x`, `y`, and `g`. If `b` is 0, it returns `x` as 1, `y` as 0, and `a` unchanged. Otherwise, it recursively calls itself with `b` and `a % b`, then returns `y`, `x - a // b * y`, and `g`, where `y`, `x`, and `g` are the results of the recursive call.

#State of the program right berfore the function call: a is a list of integers, n and m are non-negative integers, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: k is reduced by the sum of (m - a[i]) for all i in range(n) where a[i] < m.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: k is reduced by the sum of (m - a[i]) for all i in range(n) where a[i] < m, and k is less than 0
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `a`, two non-negative integers `n` and `m`, and an integer `k`. It calculates the reduction of `k` based on the values in `a` compared to `m`. If `k` is greater than or equal to zero after the calculation, it returns 1; otherwise, it returns -1.

