#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from the standard input.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input and returns it.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. This function is expected to read integers from standard input and return them as a map object of integers.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers read from standard input.
#Overall this is what the function does:The function `func_2` reads a line of input from standard input, splits it into components, converts each component to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables in the function signature. This function reads integers from standard input and returns them as a list of integers.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers that were read from the standard input.
#Overall this is what the function does:The function `func_3` reads a line of integers from the standard input, splits them, converts them to integers, and returns them as a list.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases, where each test case consists of two positive integers n and m such that 1 <= n, m <= 2 * 10^6.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list of values, where each value is the result of calling the function `func_3()` for each of the `rows_number` test cases.
#Overall this is what the function does:The function `func_4` takes a positive integer `rows_number` as input, representing the number of test cases. It returns a list where each element is the result of calling the function `func_3()` once for each test case.

#State of the program right berfore the function call: No variables in the function signature.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that is the next line of input from the standard input, with any trailing newline character removed.
#Overall this is what the function does:The function `func_5` accepts no parameters and returns a string representing the next line of input from the standard input, with any trailing newline character removed.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns the input string read from standard input, stripped of any trailing newline characters and decoded from bytes to a string.
#Overall this is what the function does:The function `func_6` reads an input string from standard input, removes any trailing newline characters, converts the bytes to a string, and returns the resulting string.

#State of the program right berfore the function call: The function `func_7` does not have any parameters. It reads a line of input, splits it into components, converts each component to an integer, and returns the resulting list of integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is a component of the line of input that was split by spaces and converted to an integer.
#Overall this is what the function does:The function reads a line of input from the user, splits it into components based on spaces, converts each component to an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases, where each test case consists of two positive integers n and m such that 1 <= n, m <= 2 * 10^6.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list of results from `func_7()` called `rows` times, where each result corresponds to the output of `func_7()` for each of the `rows` test cases.
#Overall this is what the function does:The function `func_8` takes a positive integer `rows` as input, representing the number of test cases. It returns a list containing the results of calling `func_7()` `rows` times, with each result corresponding to the output of `func_7()` for each test case.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_9():
    return input()
    #The program returns the value provided by the user as input.
#Overall this is what the function does:The function `func_9` accepts no parameters and returns a value provided by the user as input.

#State of the program right berfore the function call: This function does not have any parameters. It reads an integer input from the user and returns it.
def func_10():
    return int(input())
    #The program returns the integer value that the user inputs.
#Overall this is what the function does:The function reads an integer input from the user and returns that integer value.

#State of the program right berfore the function call: No variables are present in the function signature of `func_11`.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a substring from the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_11` takes no input and returns a list of strings, where each string is a substring from the input provided by the user, split by whitespace.

#State of the program right berfore the function call: d is a dictionary where each key is an integer and the corresponding value is a list of integers, processing is a list of integers initialized to 0, da is an integer that is a key in the dictionary d, rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where each key is an integer and the corresponding value is a list of integers, `processing` is a list of integers initialized to 0, `da` is an integer that is a key in the dictionary `d`, `rank` is a list of integers, `tmp` is 1000000000. The length of the list `d[da]` is greater than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is a dictionary where each key is an integer and the corresponding value is a list of integers, `processing` is a list of integers initialized to 0, `da` is an integer that is a key in the dictionary `d`, `rank` is a list of integers, `tmp` is the minimum value returned by `func_12` for any element in `d[da]` that meets the condition `processing[di - 1] == 0`.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the minimum value returned by `func_12` for any element in `d[da]` that meets the condition `processing[di - 1] == 0`, plus 1.
#Overall this is what the function does:The function `func_12` calculates a rank for a given key `da` in a dictionary `d` where each key maps to a list of integers. It uses a list `processing` to track visited elements and updates a list `rank` with the calculated rank. The function returns 1 if the list associated with `da` contains only one element. Otherwise, it recursively calculates the minimum rank among the elements in `d[da]` that have not been processed, adds 1 to this minimum rank, and assigns it to `rank[da - 1]`.

#State of the program right berfore the function call: a and b are non-negative integers where a >= 0 and b >= 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns 1, 0, a where 'a' is a non-negative integer
    #State: a and b are non-negative integers where a >= 0 and b >= 0. Additionally, b is not equal to 0.
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns `y`, `x - a // b * y`, and `g`. Here, `g` is the GCD of `b` and `a % b`, and `x` and `y` are the coefficients such that `g = b * x + (a % b) * y`.
#Overall this is what the function does:The function `func_13` accepts two non-negative integers `a` and `b` and returns three values. If `b` is 0, it returns 1, 0, and `a`. Otherwise, it returns coefficients `y`, `x - a // b * y`, and the greatest common divisor `g` of `b` and `a % b`, where `g = b * x + (a % b) * y`.

#State of the program right berfore the function call: a is a list of integers, n and m are positive integers such that 1 <= n <= len(a) and 1 <= m <= 2 * 10^6, k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: a is a list of integers, n and m are positive integers such that 1 <= n <= len(a) and 1 <= m <= 2 * 10^6, k is an integer that has been decreased by the sum of (m - a[i]) for all i in the range [0, n-1] where a[i] < m.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: a is a list of integers, n and m are positive integers such that 1 <= n <= len(a) and 1 <= m <= 2 * 10^6, k is an integer that has been decreased by the sum of (m - a[i]) for all i in the range [0, n-1] where a[i] < m, and k is less than 0.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_14` takes a list of integers `a`, and three integers `n`, `m`, and `k`. It adjusts `k` by subtracting the difference between `m` and each element of `a` that is less than `m`, up to the first `n` elements. It returns `1` if `k` is non-negative after these adjustments, otherwise it returns `-1`.

