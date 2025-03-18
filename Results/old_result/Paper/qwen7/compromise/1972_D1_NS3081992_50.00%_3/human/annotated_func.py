#State of the program right berfore the function call: None of the variables in the function `func_1()` are described in the provided code snippet. The function reads an integer from standard input but does not take any parameters.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from standard input
#Overall this is what the function does:The function reads an integer from standard input and returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns two integers, n and m, read from standard input, where 1 ≤ n, m ≤ 2 ⋅ 10^6.
#Overall this is what the function does:The function reads two integers, n and m, from standard input, ensuring they are within the range 1 ≤ n, m ≤ 2 ⋅ 10^6, and returns these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers [n, m] read from standard input, where n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
#Overall this is what the function does:The function reads two integers, `n` and `m`, from standard input, splits them based on whitespace, converts them to integers, and returns them as a list `[n, m]`. Both `n` and `m` must satisfy the condition 1 ≤ n, m ≤ 2 ⋅ 10^6.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases. Each test case consists of two positive integers n and m, where 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list of results from calling func_3() for each test case, where each result is determined by func_3() and there are 'rows_number' such results in the list.
#Overall this is what the function does:The function accepts a positive integer `rows_number` representing the number of test cases. For each test case, it calls another function `func_3()` with two positive integers `n` and `m` (where 1 ≤ n, m ≤ 2⋅10^6), and collects the results in a list. After processing all test cases, it returns a list containing `rows_number` results.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given code snippet. The function `func_5` reads input from standard input but does not take any parameters.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a line of text read from standard input, with trailing whitespace removed.
#Overall this is what the function does:The function reads a line of text from standard input, removes any trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: None of the variables in the function `func_6()` are documented within the provided code snippet. However, it reads a line from standard input, decodes it from bytes to a string, removes the trailing newline character, and returns the result. This suggests that `func_6()` is likely part of a larger program that handles input reading, but no specific variables or their relationships are defined in this function's signature.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program reads a line from standard input, decodes it from bytes to a string, removes the trailing newline character, and returns the result.
#Overall this is what the function does:The function reads a line from standard input, decodes it from bytes to a string, removes the trailing newline character, and returns the result.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two space-separated integers n and m such that 1 ≤ n, m ≤ 2⋅10^6 and the sum of n and the sum of m over all test cases do not exceed 2⋅10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, each pair of integers (n, m) separated by a space in the input.
#Overall this is what the function does:The function reads a series of integer pairs (n, m) from input, where each pair is separated by a space, and returns them as a list of integers. The list contains all the integer pairs provided in the input, maintaining their order.

#State of the program right berfore the function call: rows is a non-negative integer representing the number of rows for which to generate results using func_7().
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list containing the results of calling func_7() for each row in the range from 0 to rows-1
#Overall this is what the function does:The function `func_8` accepts a non-negative integer `rows` and returns a list containing the results of calling `func_7()` for each row in the range from 0 to `rows-1`.

#State of the program right berfore the function call: There is no precondition provided for the function `func_9` based on the variables in its signature, as it does not have any parameters. However, given the context of the problem, we can infer that the function should read input for the number of test cases `t`, followed by `t` pairs of integers `n` and `m`.
def func_9():
    return input()
    #The program returns input from the user, which includes the number of test cases 't', followed by 't' pairs of integers 'n' and 'm'.
#Overall this is what the function does:The function reads input from the user, including the number of test cases 't', followed by 't' pairs of integers 'n' and 'm'.

#State of the program right berfore the function call: None of the variables in the function signature are present, implying that the function does not take any input parameters. However, it returns an integer which represents the number of test cases.
def func_10():
    return int(input())
    #The program returns an integer input by the user, representing the number of test cases.
#Overall this is what the function does:The function accepts no parameters and returns an integer input by the user, representing the number of test cases.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6.
def func_11():
    return input().split()
    #The program returns a list of strings containing the values of `n` and `m` for each test case as split from user input.
#Overall this is what the function does:The function reads input from the user, splits it into a list of strings, each string containing the values of `n` and `m` for each test case, and returns this list.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of length equal to the maximum key in d, initially filled with zeros; da is an integer which is a key in the dictionary d; rank is a list of integers with the same length as the maximum key in d, used to store the results of recursive calls.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers; `processing` is a list of length equal to the maximum key in `d`, initially filled with zeros; `da` is an integer which is a key in the dictionary `d`; `rank` is a list of integers with the same length as the maximum key in `d`, used to store the results of recursive calls; `tmp` is 1000000000; the length of `d[da]` is greater than 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: Output State: `d` is a dictionary where keys are integers and values are lists of integers; `processing` is a list of length equal to the maximum key in `d`, with each element set to 0 exactly once for each `di` in `d[da]`; `da` is an integer which is a key in the dictionary `d`; `rank` is a list of integers with the same length as the maximum key in `d`, used to store the results of recursive calls; `tmp` is 1000000000; the length of `d[da]` is greater than 1.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns 1000000001
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers and values are lists of integers, a list `processing` of the same length as the maximum key in `d` initially filled with zeros, an integer `da` which is a key in the dictionary `d`, and a list `rank` of integers with the same length as the maximum key in `d`. If the length of `d[da]` is 1, the function returns 1. Otherwise, it recursively processes each element in `d[da]`, updating the `processing` list and tracking the minimum value in `tmp`. After processing, it updates `rank[da - 1]` with `tmp + 1` and returns this value. The function can return either 1 or 1000000001 based on the conditions met during its execution.

#State of the program right berfore the function call: a and b are positive integers such that 1 <= a, b <= 2 * 10^6 and b != 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x which is 1, y which is 0, and a which is a positive integer such that 1 <= a <= 2 * 10^6
    #State: a and b are positive integers such that 1 <= a, b <= 2 * 10^6 and b != 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, and g, where y, x, and g are the results of the function call func_13(b, a % b)
#Overall this is what the function does:The function `func_13` accepts two parameters, `a` and `b`, both of which are positive integers within the range [1, 2 * 10^6] and `b` is not zero. Depending on the value of `b`, the function either returns `x` as 1, `y` as 0, and `a` unchanged, or it recursively calls itself with `b` and `a % b` to compute `y`, `x - a // b * y`, and `g`. In both cases, the function returns three values: `y`, `x - a // b * y`, and `g`.

#State of the program right berfore the function call: a is a list of integers, n and m are positive integers such that 0 <= n <= len(a) and 1 <= m <= max(a), and k is an integer such that k >= 0.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: a is a list of integers where each element a[i] that was less than m has been increased by the difference m - a[i], and k is decreased by the sum of these differences for all elements a[i] in the range of n that were less than m.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: a is a list of integers where each element a[i] that was less than m has been increased by the difference m - a[i], and k is decreased by the sum of these differences for all elements a[i] in the range of n that were less than m. Additionally, k is less than 0.
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `a`, two positive integers `n` and `m` where 0 <= n <= len(a) and 1 <= m <= max(a), and an integer `k` where k >= 0. It iterates through the first `n` elements of `a` and increases any element less than `m` by the difference `m - a[i]`. If `k` remains non-negative after this adjustment, the function returns 1; otherwise, it returns -1.

