#State of the program right berfore the function call: func is a function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a variable named `wrapper` which is not defined in the provided initial state.
#Overall this is what the function does:The function `func_1` accepts a function `func` as a parameter and returns a variable named `wrapper`, which is not defined within the provided code.

#State of the program right berfore the function call: args is a tuple containing any type and value of arguments that the function `func` can accept.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple containing any type and value of arguments that the function `func` can accept. If `args` was not originally in the dictionary `d`, then `d` now includes the key `args` with the value `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the value of `d[args]`. If `args` was not originally in the dictionary `d`, then `d` now includes the key `args` with the value `func(*args)`. Otherwise, `d` remains unchanged and the program returns the pre-existing value associated with `args` in `d`.
#Overall this is what the function does:The function accepts a tuple `args` containing any type and value of arguments. It returns the value associated with `args` in the dictionary `d` if `args` is already a key in `d`. If `args` is not in `d`, it computes `func(*args)`, stores the result in `d` with `args` as the key, and then returns the computed value.

#State of the program right berfore the function call: The function `func_2` does not take any parameters. It reads a line from standard input and returns it as a string after stripping any leading or trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is read from standard input, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function reads a line from standard input, removes any leading or trailing whitespace from the line, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_3`. Therefore, no specific precondition can be derived from the variables in the function signature.
def func_3():
    return int(func_2())
    #The program returns the integer value returned by `func_2()`
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns the integer value returned by `func_2()`.

#State of the program right berfore the function call: delimiter is a string, which by default is a space (' '), and the function returns a list of integers obtained by splitting the input string from func_2() by the delimiter.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the input string from `func_2()` by the delimiter, which is a space (' ') by default.
#Overall this is what the function does:The function accepts a delimiter string (defaulting to a space) and returns a list of integers by splitting an input string from `func_2()` using the specified delimiter.

#State of the program right berfore the function call: This function does not have any parameters, so there are no variables to describe in terms of preconditions.
def func_5():
    return func_2()
    #The program returns the result of func_2()
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a list of n integers such that 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. D is a sorted list of unique integers derived from a list of m integers such that 1 <= d_i <= 10^9. F is a list of k integers such that 1 <= f_i <= 10^9.
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
        
    #State: `n`, `m`, `k` are assigned the values returned by `func_4()`. `A` is assigned the value returned by `func_4()`. `D` is a sorted list of unique values returned by `func_4()`. `F` is assigned the value returned by `func_4()`. `max_diff` is the largest difference between consecutive elements in `A`. `next_max_diff` is the second largest difference between consecutive elements in `A`. `index` is the index where `max_diff` was found.
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
        
    #State: - After all iterations of the loop, `ans` will hold the minimum value of the maximum of the two differences calculated for each `f` in `F`.
    #
    #Given the loop and the initial state, the only variables that change are `l`, `h`, `mid`, `mid_sum`, `mid_next_sum`, and `ans`. The values of `n`, `m`, `k`, `A`, `D`, `F`, `max_diff`, `next_max_diff`, `index`, `left`, and `right` remain unchanged.
    #
    #Output State:
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum value of the maximum of the two differences calculated for each f in F, and next_max_diff is another maximum difference value)
#Overall this is what the function does:The function calculates and prints the maximum of two values: the second largest difference between consecutive elements in a sorted list `A`, and the minimum value of the maximum of two specific differences calculated for each element in list `F` using elements from a sorted list `D`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_7`.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` holds the return value of `func_3()`
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves a number of test cases from `func_3()` and then calls `func_6()` for each of those test cases.

