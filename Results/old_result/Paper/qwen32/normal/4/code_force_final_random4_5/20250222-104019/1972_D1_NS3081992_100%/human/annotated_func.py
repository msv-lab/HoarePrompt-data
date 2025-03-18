#State of the program right berfore the function call: No variables in the function signature. This function likely reads an integer from standard input and returns it, presumably the number of test cases or values for n and m in the context of the main solution.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from standard input.
#Overall this is what the function does:The function `func_1` reads an integer from standard input and returns it.

#State of the program right berfore the function call: No variables are present in the function signature. The function `func_2` reads input from standard input and returns a map object containing integers.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers that were read from standard input.
#Overall this is what the function does:The function `func_2` reads a line of input from standard input, splits it into components, converts each component into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: The function does not have any parameters. It reads from standard input, expecting a line of space-separated integers. The returned value is a list of integers parsed from that line.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers parsed from the line read from standard input.
#Overall this is what the function does:The function reads a line of space-separated integers from standard input and returns a list of these integers.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases, where each test case consists of two positive integers n and m such that 1 <= n, m <= 2 * 10^6.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list of results from func_3() called rows_number times.
#Overall this is what the function does:The function `func_4` takes a positive integer `rows_number` as input and returns a list containing the results of calling `func_3()` `rows_number` times.

#State of the program right berfore the function call: This function does not have any parameters in its signature. It reads a single line of input from the standard input buffer, which is expected to be a string of characters, and returns it after stripping any trailing newline characters.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that is the input read from the standard input buffer, with any trailing newline characters removed.
#Overall this is what the function does:The function reads a single line of input from the standard input buffer and returns it as a string with any trailing newline characters removed.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is read from standard input, stripped of any trailing newline characters, and decoded from bytes to a string.
#Overall this is what the function does:The function reads a line of input from standard input, removes any trailing newline characters, decodes it from bytes to a string, and returns the resulting string.

#State of the program right berfore the function call: The function `func_7()` does not have any parameters. It reads a line of input and returns a list of integers. The input is expected to be a space-separated string of integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers that are obtained by converting each space-separated string of integers from the input into individual integers.
#Overall this is what the function does:The function `func_7` reads a line of input, which is expected to be a space-separated string of integers, and returns a list of integers obtained by converting each space-separated string into individual integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list containing the result of `func_7()` called `rows` times.
#Overall this is what the function does:The function `func_8` takes a positive integer `rows` as input and returns a list containing the result of calling `func_7()` `rows` times.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_9():
    return input()
    #The program returns the value provided as input.
#Overall this is what the function does:The function `func_9` does not accept any parameters and returns the value provided as input.

#State of the program right berfore the function call: No variables are present in the function signature provided. The function `func_10` does not take any parameters and is not related to the problem description provided.
def func_10():
    return int(input())
    #The program returns an integer value that is provided as input.
#Overall this is what the function does:The function `func_10` does not accept any parameters and returns an integer value that is provided as input.

#State of the program right berfore the function call: No variables are present in the function signature, thus no precondition can be derived from the given function alone.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a substring from the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_11` accepts no parameters, prompts the user for input, and returns a list of strings where each string is a substring from the input, split by whitespace.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer, `rank` is a list of integers, `tmp` is 10, and the length of `d[da]` is not equal to 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer, `rank` is a list of integers, and `tmp` is the minimum value returned by `func_12(d, processing, di, rank)` for all `di` in `d[da]`.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of `tmp + 1`, where `tmp` is the minimum value returned by `func_12(d, processing, di, rank)` for all `di` in `d[da]`.
#Overall this is what the function does:The function `func_12` calculates a rank for a given integer `da` based on the structure of the dictionary `d` and the list `processing`. It returns 1 if the list associated with `da` in `d` contains only one element. Otherwise, it recursively calculates the rank for each element in the list associated with `da` and returns the minimum rank found plus one. The rank for `da` is stored in the `rank` list at the index `da - 1`.

#State of the program right berfore the function call: a and b are non-negative integers, with b potentially being zero.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns (1, 0, a), where 1 is the value of x, 0 is the value of y, and a is a non-negative integer.
    #State: a and b are non-negative integers, with b potentially being zero, and b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns a tuple (y, x - a // b * y, g)
#Overall this is what the function does:The function `func_13` computes and returns a tuple containing three values. Given two non-negative integers `a` and `b`, if `b` is zero, it returns `(1, 0, a)`. Otherwise, it performs a recursive computation and returns a tuple `(y, x - a // b * y, g)`, where `y`, `x`, and `g` are determined based on the recursive calls and the values of `a` and `b`.

#State of the program right berfore the function call: a is a list of integers, n and m are positive integers such that 0 <= n <= len(a) and m is a positive integer, k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: `a` is a list of integers, `n` is a positive integer such that 0 <= n <= len(a), `m` is a positive integer, and `k` is an integer updated to `k - sum(m - a[i] for i in range(n) if a[i] < m)`
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: `a` is a list of integers, `n` is a positive integer such that 0 <= n <= len(a), `m` is a positive integer, and `k` is an integer updated to `k - sum(m - a[i] for i in range(n) if a[i] < m)`. Additionally, `k` is less than 0.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_14` takes a list of integers `a`, two positive integers `n` and `m` such that `0 <= n <= len(a)`, and an integer `k`. It returns `1` if `k` is non-negative after subtracting the sum of the differences between `m` and each element in `a` that is less than `m`, for the first `n` elements of `a`. Otherwise, it returns `-1`.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_15():
    n, m = func_7()
    i = 1
    ans = 0
    while i <= m and i * i <= n + i:
        ans += (n + i) // (i * i)
        
        i += 1
        
    #State: `i` is the smallest integer greater than `m` or such that `i * i > n + i`, and `ans` is the sum of `(n + i) // (i * i)` for all `i` from 1 to `i_final - 1`.
    return ans - 1
    #The program returns `ans - 1`, where `ans` is the sum of `(n + i) // (i * i)` for all `i` from 1 to `i_final - 1`, and `i_final` is the smallest integer greater than `m` or such that `i * i > n + i`.
#Overall this is what the function does:The function calculates the sum of the expression `(n + i) // (i * i)` for all integers `i` from 1 up to, but not including, `i_final`. Here, `i_final` is the smallest integer that is either greater than `m` or satisfies `i * i > n + i`. The function returns this sum minus one.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_16():
    for _ in range(func_10()):
        sys.stdout.write(str(func_15()) + '\n')
        
    #State: The loop has executed `func_10()` times, and in each of those executions, `func_15()` has been called and its result has been printed.
#Overall this is what the function does:The function `func_16` executes a loop a number of times determined by the return value of `func_10()`. In each iteration, it calls `func_15()` and prints the result. The function itself does not accept any parameters directly from the user and does not return a value explicitly. It outputs the results of `func_15()` to the standard output.

