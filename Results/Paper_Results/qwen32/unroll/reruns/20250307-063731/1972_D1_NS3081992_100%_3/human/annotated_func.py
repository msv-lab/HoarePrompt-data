#State of the program right berfore the function call: No variables in the function signature. The function `func_1` is expected to read an integer from the standard input.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer that was read from the standard input.
#Overall this is what the function does:The function reads an integer from the standard input and returns that integer.

#State of the program right berfore the function call: No variables are present in the function signature, thus no precondition can be derived from the function signature alone.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object that contains integers obtained by splitting a line of input read from standard input.
#Overall this is what the function does:The function `func_2` reads a line of input from standard input, splits it into components, converts these components into integers, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature. This function is likely responsible for reading input from standard input, and it returns a list of integers.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers that are read from standard input, split by whitespace.
#Overall this is what the function does:The function `func_3` reads a line of input from standard input, splits it into substrings based on whitespace, converts each substring into an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing the result of `func_3()` called `rows_number` times.
#Overall this is what the function does:The function accepts a positive integer `rows_number` and returns a list containing the result of calling `func_3()` `rows_number` times.

#State of the program right berfore the function call: This function does not use the variables n and m directly from the problem description. It appears to be a utility function to read input from standard input. No specific precondition can be derived from the variables n and m based on the given function signature alone.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that is the next line of input from standard input, with any trailing newline characters removed.
#Overall this is what the function does:The function `func_5` reads a line from standard input and returns it as a string with any trailing newline characters removed.

#State of the program right berfore the function call: This function does not have any parameters. It reads a line from the standard input, presumably to be used in processing test cases for the problem.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is the line read from the standard input, with any trailing whitespace removed.
#Overall this is what the function does:The function reads a line from the standard input, removes any trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature. The function `func_7` is not directly related to the problem description provided. However, based on the example usage, it can be inferred that `func_7` is expected to read a line of input, split it into components, convert them to integers, and return the list of these integers. This function likely serves to read input for a test case, where the input consists of two integers `n` and `m`.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of two integers, `n` and `m`, which are the components of the input line split and converted to integers.
#Overall this is what the function does:The function `func_7` reads a line of input, splits it into two components, converts these components to integers, and returns them as a list.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list with 'rows' number of elements, where each element is the result of calling the function `func_7()`.
#Overall this is what the function does:The function accepts a positive integer `rows` representing the number of test cases and returns a list containing `rows` number of elements, where each element is the result of calling the function `func_7()`.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_9():
    return input()
    #The program returns the value provided by the user input.
#Overall this is what the function does:The function accepts no parameters and returns the value provided by the user input.

#State of the program right berfore the function call: No variables are present in the function signature, thus no precondition can be derived from the given function.
def func_10():
    return int(input())
    #The program returns an integer value that is provided by the user input.
#Overall this is what the function does:The function `func_10` accepts no parameters and returns an integer value provided by the user input.

#State of the program right berfore the function call: No variables are present in the function signature provided. The function `func_11` does not take any parameters and thus has no preconditions based on input variables.
def func_11():
    return input().split()
    #The program returns a list of strings, each string being a word from the input provided by the user.
#Overall this is what the function does:The function `func_11` prompts the user for input, splits the input into words, and returns a list of these words.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer, and rank is a list of integers; tmp is 1000000000. The length of the list d[da] is not equal to 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers all set to 0, da is an integer, and rank is a list of integers; tmp is the minimum value returned by func_12(d, processing, di, rank) for any di in d[da].
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` is the minimum value returned by `func_12(d, processing, di, rank)` for any `di` in `d[da]`.
#Overall this is what the function does:The function `func_12` calculates a rank for a given integer `da` based on the structure of the dictionary `d` and the list `processing`. If the list associated with `da` in `d` contains only one element, it returns 1. Otherwise, it recursively calculates the minimum rank for all elements in the list `d[da]` and updates the `rank` list at index `da - 1` with this minimum rank plus one. The function ultimately returns this calculated rank.

#State of the program right berfore the function call: a and b are non-negative integers where a >= 0 and b >= 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns the tuple (1, 0, a) where `a` is a non-negative integer.
    #State: a and b are non-negative integers where a ≥ 0 and b ≥ 0. Additionally, b is not equal to 0.
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns (y, x - a // b * y, g)
#Overall this is what the function does:The function `func_13` takes two non-negative integers `a` and `b` as input and returns a tuple. If `b` is 0, it returns `(1, 0, a)`. Otherwise, it recursively computes and returns a tuple `(y, x - a // b * y, g)`, where `y`, `x`, and `g` are values determined by the function's logic.

#State of the program right berfore the function call: a is a list of integers, n is the length of the list a, m is a positive integer, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: `a` is a list of integers, `n` is the length of the list `a`, `m` is a positive integer, and `k` is an integer decreased by the sum of `m - a[i]` for all `i` such that `a[i] < m`.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: `a` is a list of integers, `n` is the length of the list `a`, `m` is a positive integer, and `k` is an integer decreased by the sum of `m - a[i]` for all `i` such that `a[i] < m`. Additionally, `k` is less than 0.
    return -1
    #The program returns -1.
#Overall this is what the function does:The function `func_14` takes a list of integers `a`, its length `n`, a positive integer `m`, and an integer `k`. It adjusts `k` by decreasing it with the sum of `m - a[i]` for all elements `a[i]` in `a` that are less than `m`. The function returns 1 if the adjusted `k` is non-negative; otherwise, it returns -1.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_15():
    n, m = func_7()
    i = 1
    ans = 0
    while i <= m and i * i <= n + i:
        ans += (n + i) // (i * i)
        
        i += 1
        
    #State: `i` is the smallest integer such that `i > m` or `i * i > n + i`, and `ans` is the sum of `(n + i) // (i * i)` for all `i` from 1 up to the final value of `i` minus 1.
    return ans - 1
    #- The program returns `ans - 1`.
    #
    #Output State:
#Overall this is what the function does:The function `func_15` calculates a specific sum based on the values returned from `func_7`, and returns the result minus one.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_16():
    for _ in range(func_10()):
        sys.stdout.write(str(func_15()) + '\n')
        
    #State: The output consists of `k` lines, each containing the value `v`. The values of `n` and `m` remain unchanged.
#Overall this is what the function does:The function `func_16` prints `k` lines, each containing the value `v`. The values of `n` and `m` remain unchanged.

