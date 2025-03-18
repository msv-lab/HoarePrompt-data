#State of the program right berfore the function call: None of the variables in the function signature are used, but the function is expected to read an integer from the standard input, which should be a valid integer.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns the integer value read from the standard input.
#Overall this is what the function does:The function `func_1` reads an integer value from the standard input and returns this integer value. The function does not modify any external state or variables. After the function concludes, the program has the integer value that was read from the standard input available as the return value.

#State of the program right berfore the function call: This function does not take any input arguments. It reads a line from standard input, splits it into parts, converts each part into an integer, and returns a map object of integers.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object that contains integers converted from the parts of a line read from standard input, where each part is separated by whitespace.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads a line from standard input, splits the line into parts based on whitespace, converts each part into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads input from stdin, expecting a line of space-separated integers.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers obtained from the input line of space-separated integers read from stdin.
#Overall this is what the function does:The function reads a line of space-separated integers from standard input (stdin) and returns a list of integers. The function does not modify any external variables or state. After the function concludes, the user will have a list of integers derived from the input line.

#State of the program right berfore the function call: rows_number is a non-negative integer.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing `rows_number` elements, where each element is the result of calling `func_3()`. Since the specific output of `func_3()` is not provided, the list will contain `rows_number` instances of whatever `func_3()` returns.
#Overall this is what the function does:The function `func_4` accepts a non-negative integer `rows_number` and returns a list containing `rows_number` elements, where each element is the result of calling `func_3()`. The final state of the program after the function concludes is that the returned list has `rows_number` instances of whatever `func_3()` returns, and `rows_number` remains unchanged.

#State of the program right berfore the function call: None of the variables in the function signature are used, and the function does not take any input parameters.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns the next line of input from the standard input (stdin) as a byte string with trailing whitespace removed.
#Overall this is what the function does:The function `func_5` reads the next line from standard input (stdin) and returns it as a byte string with trailing whitespace removed. It does not take any input parameters and does not modify any external state.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads a line from standard input, strips the trailing newline, decodes it from bytes to a string, and returns it.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is the result of reading a line from standard input, removing the trailing newline, and decoding it from bytes to a string.
#Overall this is what the function does:The function `func_6` reads a line from standard input, removes the trailing newline character, decodes the line from bytes to a string, and returns this string.

#State of the program right berfore the function call: None of the variables are used in the function signature. The function reads input from the standard input, expecting a line of space-separated integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is derived from converting the space-separated string inputs into integer values.
#Overall this is what the function does:The function `func_7` reads a line of space-separated integers from the standard input and returns a list of integers, where each integer is derived from converting the space-separated string inputs into integer values.

#State of the program right berfore the function call: rows is a non-negative integer.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list containing the results of calling `func_7()` `rows` times, where `rows` is a non-negative integer.
#Overall this is what the function does:The function `func_8` accepts a non-negative integer `rows` and returns a list containing the results of calling `func_7()` `rows` times. The final state of the program includes the returned list, and the input parameter `rows` remains unchanged.

#State of the program right berfore the function call: None of the variables in the function signature are used, and the function does not take any input parameters.
def func_9():
    return input()
    #The program returns a value that is input by the user.
#Overall this is what the function does:The function `func_9` does not accept any parameters and returns a value that is input by the user. After the function concludes, the program state includes a returned value that is the user's input.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read an integer input, which is expected to be the number of test cases t.
def func_10():
    return int(input())
    #The program returns an integer value that represents the number of test cases t, which is provided by the user as input.
#Overall this is what the function does:The function `func_10` does not accept any parameters. It reads an integer input from the user, which is expected to represent the number of test cases, and returns this integer value. After the function concludes, the program has an integer value that was provided by the user.

#State of the program right berfore the function call: None of the variables in the function signature are used, and the function does not take any input parameters.
def func_11():
    return input().split()
    #The program returns a list of strings split from the input provided by the user.
#Overall this is what the function does:The function `func_11` does not accept any parameters. It reads a line of input from the user and returns a list of strings, where each string is a substring of the input line split by whitespace.

#State of the program right berfore the function call: d is a dictionary where each key maps to a list of integers, processing is a list of integers of length at least max(d.keys()), da is an integer that is a key in d, and rank is a list of integers of length at least max(d.keys()).
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1.
    #State: `d` is a dictionary where each key maps to a list of integers, `processing` is a list of integers of length at least max(d.keys()), `da` is an integer that is a key in `d`, `rank` is a list of integers of length at least max(d.keys()), `tmp` is 1000000000, and the list `d[da]` has a length greater than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` remains unchanged, `processing` has some elements set to 1 and then reset to 0, `da` remains unchanged, `rank` remains unchanged, `tmp` is updated to the minimum value returned by `func_12` for the elements in `d[da]` where `processing[di - 1]` was initially 0.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the minimum value returned by `func_12` for the elements in `d[da]` where `processing[di - 1]` was initially 0, plus 1.
#Overall this is what the function does:The function `func_12` accepts a dictionary `d` where each key maps to a list of integers, a list `processing` of integers, an integer `da` that is a key in `d`, and a list `rank` of integers. It modifies the `rank` list by setting `rank[da - 1]` to a value that is one more than the minimum value returned by recursive calls to `func_12` for elements in `d[da]` where the corresponding `processing` value was initially 0. If `d[da]` contains only one element, the function returns 1. Otherwise, it returns the minimum value returned by the recursive calls plus 1.

#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m, where n and m are positive integers provided in the problem description.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns the values (1, 0, a), where `a` is a positive integer such that 1 <= `a` <= `n`.
    #State: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m, where n and m are positive integers provided in the problem description, and b is not equal to 0.
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns a tuple containing the values `y`, `x - a // b * y`, and `g`, where `x`, `y`, and `g` are the values returned by `func_13(b, a % b)`.
#Overall this is what the function does:The function `func_13` accepts two positive integers `a` and `b` within specified ranges (1 <= a <= n and 1 <= b <= m, where n and m are positive integers). It returns a tuple `(x, y, g)` such that if `b` is 0, the tuple is `(1, 0, a)`. Otherwise, it recursively calls itself with the arguments `(b, a % b)` and returns a tuple containing the values `y`, `x - a // b * y`, and `g`, where `x`, `y`, and `g` are the results of the recursive call. The final state of the program is that it has computed and returned these values, which are related to the Extended Euclidean Algorithm.

#State of the program right berfore the function call: a is a list of integers, n is a non-negative integer such that 0 <= n <= len(a), m is a positive integer, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: a is a list of integers, n is a non-negative integer such that 0 <= n <= len(a), m is a positive integer, and k is an integer that has been decremented by the total of (m - a[i]) for all i in range(n) where a[i] < m.
    if (k >= 0) :
        return 1
        #The program returns 1.
    #State: a is a list of integers, n is a non-negative integer such that 0 <= n <= len(a), m is a positive integer, and k is an integer that has been decremented by the total of (m - a[i]) for all i in range(n) where a[i] < m. Additionally, k is less than 0.
    return -1
    #The program returns -1.
#Overall this is what the function does:The function `func_14` accepts a list of integers `a`, a non-negative integer `n` (where 0 <= n <= len(a)), a positive integer `m`, and an integer `k`. It decrements `k` by the total of (m - a[i]) for all elements a[i] in the list `a` up to index `n-1` where a[i] is less than `m`. After processing, the function returns 1 if `k` is non-negative, otherwise it returns -1. The list `a`, integer `n`, and positive integer `m` remain unchanged, while `k` is modified as described.

