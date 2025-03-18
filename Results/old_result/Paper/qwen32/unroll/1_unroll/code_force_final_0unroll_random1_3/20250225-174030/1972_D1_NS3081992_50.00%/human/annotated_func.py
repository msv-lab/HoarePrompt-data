#State of the program right berfore the function call: No variables in the function signature. The function `func_1` is likely responsible for reading input, and based on the provided code, it returns a single integer read from the standard input.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns a single integer read from the standard input.
#Overall this is what the function does:The function `func_1` reads a single integer from the standard input and returns it.

#State of the program right berfore the function call: No variables are present in the function signature. The function `func_2` reads input from standard input and returns a map object containing integers, which suggests it is used to read multiple integers from a single line of input.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers, which are the integers read from a single line of input provided to the standard input.
#Overall this is what the function does:The function `func_2` reads a single line of input from the standard input, which is expected to contain multiple integers separated by spaces, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables in the provided function signature. The function `func_3` is not directly related to the problem's main logic based on the given code snippet. However, based on the context, it seems to read two integers from the standard input, which could be `n` and `m` for each test case. Therefore, it is reasonable to infer that the function returns a list containing two integers, `n` and `m`, where `n` and `m` are positive integers such that 1 ≤ n, m ≤ 2 · 10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list containing two integers, `n` and `m`, where `n` and `m` are positive integers such that 1 ≤ n, m ≤ 2 · 10^6.
#Overall this is what the function does:The function reads two integers from the standard input and returns them as a list of two integers, where each integer is a positive number between 1 and 2,000,000 inclusive.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing the results of `func_3()` called `rows_number` times.
#Overall this is what the function does:The function accepts a positive integer `rows_number` and returns a list containing the results of calling `func_3()` `rows_number` times.

#State of the program right berfore the function call: The function `func_5` does not have any parameters. It reads a single line from the standard input, removes any trailing newline characters, and returns the result as a byte string.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a byte string that is a single line read from the standard input, with any trailing newline characters removed.
#Overall this is what the function does:The function reads a single line from the standard input, removes any trailing newline characters, and returns the result as a byte string.

#State of the program right berfore the function call: No variables are present in the function signature. The function `func_6` does not take any parameters and is not related to the problem description provided.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is the next line of input from the standard input, with any trailing newline characters removed and decoded to a regular string.
#Overall this is what the function does:The function reads the next line from the standard input, removes any trailing newline characters, decodes it to a regular string, and returns this string.

#State of the program right berfore the function call: There are no variables in the function signature. This function reads input from the standard input and returns a list of integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers that are obtained by splitting the input string by whitespace and converting each split substring to an integer.
#Overall this is what the function does:The function `func_7` reads a string from the standard input, splits the string by whitespace, converts each split substring to an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases, where each test case consists of two positive integers n and m (1 ≤ n, m ≤ 2 · 10^6).
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list of results from `func_7()` called `rows` times. Each element in the list corresponds to the output of `func_7()` for each of the `rows` test cases.
#Overall this is what the function does:The function `func_8` takes a single parameter `rows`, which is a positive integer representing the number of test cases. It returns a list containing the results of calling `func_7()` `rows` times, with each element in the list corresponding to the output of `func_7()` for each test case.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_9():
    return input()
    #The program returns whatever input is provided by the user, as the `input()` function reads a line from input, converts it into a string (stripping a trailing newline), and returns that.
#Overall this is what the function does:The function `func_9` reads a line of input from the user, converts it into a string (removing any trailing newline), and returns that string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_10()`. The function does not take any input parameters and returns an integer, which is presumably read from standard input.
def func_10():
    return int(input())
    #The program returns an integer that is read from standard input.
#Overall this is what the function does:The function `func_10` does not accept any input parameters and returns an integer that is read from standard input.

#State of the program right berfore the function call: The function `func_11` does not have any parameters, and it returns a list of strings, which are the space-separated values from the input.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a space-separated value from the input provided to the function.
#Overall this is what the function does:The function `func_11` takes no input parameters and returns a list of strings, where each string is a space-separated value from the input provided by the user.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers initialized to 0, da is an integer key present in the dictionary d, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers initialized to 0, `da` is an integer key present in the dictionary `d`, and `rank` is a list of integers; `tmp` is 1000000000. The length of the list `d[da]` is more than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers all initialized to 0, `da` is an integer key present in the dictionary `d`, `rank` is a list of integers, and `tmp` is the minimum value returned by `func_12` during the loop iterations.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` is the minimum value returned by `func_12` during the loop iterations.
#Overall this is what the function does:The function `func_12` calculates and returns a rank value for a given key `da` in the dictionary `d`. It recursively explores the list of integers associated with `da` in `d`, updating a `processing` list to avoid cycles and using a `rank` list to store the computed rank. If the list associated with `da` contains only one element, it returns 1. Otherwise, it returns the minimum rank value obtained from recursive calls plus one.

#State of the program right berfore the function call: a and b are non-negative integers, with b being zero in the base case of the recursion, and a being any non-negative integer in that case. In the recursive calls, a and b are the result of the modulo operation between the previous values of a and b, respectively.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns (1, 0, a)
    #State: a and b are non-negative integers. b is not zero. a is the result of the modulo operation between the previous values of a and b, and b is the new remainder of that operation.
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns `y`, `x`, and `g` where `x`, `y`, and `g` are the values returned by `func_13(b, 0)`
#Overall this is what the function does:The function `func_13` calculates the coefficients of Bézout's identity and the greatest common divisor (GCD) of two non-negative integers `a` and `b`. It returns a tuple containing these coefficients and the GCD. Specifically, it returns `(1, 0, a)` if `b` is zero, otherwise it returns `(y, x - a // b * y, g)` where `x`, `y`, and `g` are the results of the recursive call `func_13(b, a % b)`.

#State of the program right berfore the function call: a is a list of integers, n is a non-negative integer such that 0 <= n <= len(a), m is a positive integer, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: a is a list of integers, n is a non-negative integer such that 0 <= n <= len(a), m is a positive integer, and k is an integer decreased by the sum of (m - a[i]) for all i where a[i] < m.
    if (k >= 0) :
        return 1
        #The program returns 1.
    #State: a is a list of integers, n is a non-negative integer such that 0 <= n <= len(a), m is a positive integer, and k is an integer decreased by the sum of (m - a[i]) for all i where a[i] < m. Additionally, k is less than 0.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_14` checks a list of integers `a` up to the `n`-th element, decreasing `k` by the difference between `m` and each element in `a` that is less than `m`. It returns 1 if `k` remains non-negative after these adjustments, and -1 otherwise.

