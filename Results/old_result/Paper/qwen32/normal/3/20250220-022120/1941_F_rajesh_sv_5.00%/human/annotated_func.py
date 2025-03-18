#State of the program right berfore the function call: func is a function, but the function signature does not provide enough information about its parameters or return type to infer a meaningful precondition.
def func_1(func):
    d = {}
    return wrapper
    #The program returns `wrapper` which is a function.
#Overall this is what the function does:The function `func_1` accepts another function `func` as its parameter and returns a new function `wrapper`.

#State of the program right berfore the function call: args is a variable-length argument list containing values of any type and value.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a variable-length argument list containing values of any type and value. If `args` is not a key in the dictionary `d`, then `d` now includes the key `args` with the value `func(*args)`.
    return d[args]
    #The program returns the value of `func(*args)` if `args` was not a key in the dictionary `d` before the execution, or it returns the value already associated with the key `args` in the dictionary `d`.
#Overall this is what the function does:The function accepts a variable-length argument list `args`. It returns the result of `func(*args)` if `args` is not already a key in the dictionary `d`. If `args` is already a key in `d`, it returns the value associated with `args` in `d`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. This function does not take any input parameters and its behavior is not described in the provided code snippet.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is the next line read from the standard input, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_2` reads the next line from the standard input, removes any leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_3`. Therefore, no specific precondition can be derived from the function signature alone.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling `func_2()`
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an integer value that is the result of calling `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` string and converting each split substring into an integer.
#Overall this is what the function does:The function accepts a string `delimiter` and returns a list of integers. This list is created by splitting a string (obtained from `func_2()`) using the `delimiter` and converting each resulting substring into an integer.

#State of the program right berfore the function call: No variables are present in the function signature of `func_5`, thus no specific precondition can be derived from the provided function signature alone.
def func_5():
    return func_2()
    #The program returns the result of `func_2()`
#Overall this is what the function does:The function `func_5` accepts no parameters and returns the result of `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers where 2 <= n <= 10^5, 1 <= m <= 2 * 10^5, and 1 <= k <= 2 * 10^5. A is a list of n integers representing the complexities of the prepared problems, sorted in strictly increasing order (1 <= a_i <= 2 * 10^9). D is a list of m integers representing the complexities of the models (1 <= d_i <= 10^9). F is a list of k integers representing the complexities of the functions (1 <= f_i <= 10^9).
def func_6():
    n, m, k = func_4()
    A = func_4()
    D = sorted(set(func_4()))
    F = func_4()
    max_diff, next_max_diff, index = -inf, -inf, None
    for i in range(1, n):
        diff = A[i] - A[i - 1]
        
        if diff > max_diff:
            max_diff = diff
            index = i
        elif diff > next_max_diff:
            next_max_diff = diff
        
    #State: `A` is a list of integers returned by `func_4()`, `n`, `m`, and `k` are the values returned by `func_4()`, `D` is a sorted list of unique integers from `A`, `F` is the list returned by `func_4()`, `max_diff` is the maximum difference between consecutive elements in `A`, `next_max_diff` is the second maximum difference between consecutive elements in `A`, `index` is the index where `max_diff` was found.
    left, right = A[index - 1], A[index]
    ans = max_diff
    for f in F:
        l = bisect_right(D, left - f)
        
        h = bisect_left(D, right - f) - 1
        
        while l < h:
            mid = l + (h - l) // 2
            mid_sum, mid_next_sum = D[mid] + f, D[mid + 1] + f
            if mid_sum - left < right - mid_next_sum:
                l = mid + 1
            else:
                h = mid
        
        if l == h:
            ans = min(ans, max(D[l] + f - left, right - D[l] - f))
        
    #State: ans
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the value of ans and next_max_diff is the value of next_max_diff)
#Overall this is what the function does:The function calculates and prints the maximum difference between consecutive elements in the sorted list `A` of problem complexities, adjusted by the complexities in list `F` of function complexities, and compares it with the second maximum difference between consecutive elements in `A`. The output is the larger of these two values.

#State of the program right berfore the function call: testcases is an integer representing the number of test cases, where 1 <= testcases <= 10^4.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is the value returned by `func_3()` minus `testcases`, where `0 <= testcases - testcases <= 10^4 - testcases`
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves the number of test cases by calling `func_3()`, then iterates through each test case, executing `func_6()` for each one. The function does not return any value explicitly.

