#State of the program right berfore the function call: func is a callable function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a callable function `wrapper` that has been defined or referenced somewhere in the code, and `d` remains an empty dictionary.
#Overall this is what the function does:The function `func_1` accepts a callable function `func` as a parameter and returns a callable function `wrapper`. The dictionary `d` remains empty after the function concludes.

#State of the program right berfore the function call: args is a tuple of arguments that can be passed to the function `func`, and `d` is a dictionary that maps tuples of arguments to their computed results by `func`.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple of arguments that can be passed to the function `func`, and `d` is a dictionary that maps tuples of arguments to their computed results by `func`. If `args` is not in `d`, then `d[args]` is set to the result of `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the computed result of `func(*args)` if `args` is not already in the dictionary `d`. If `args` is in `d`, the program returns the value associated with `args` in `d`.
#Overall this is what the function does:The function `wrapper` does not accept any parameters. It checks if a tuple `args` is present in a dictionary `d`. If `args` is not in `d`, it computes the result of `func(*args)` and stores it in `d` with `args` as the key. The function then returns the value associated with `args` in `d`. If `args` is already in `d`, the function simply returns the value associated with `args` without recomputing it.

#State of the program right berfore the function call: This function does not take any parameters and is designed to read a line from standard input, stripping any trailing whitespace. It is used to read input values but does not directly involve the variables from the problem description.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the input line read from standard input, with any trailing whitespace removed.
#Overall this is what the function does:The function `func_2` reads a line from standard input, removes any trailing whitespace from the line, and returns the processed line. It does not take any parameters and does not modify any external variables. The final state of the program after the function concludes is that a line of input has been read and stripped of trailing whitespace, and this line is returned to the caller.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_3` does not take any parameters.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling the function `func_2()`.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an integer value obtained by calling the function `func_2()`. The state of the program after the function concludes is that an integer value is returned, which is the result of the `func_2()` call.

#State of the program right berfore the function call: delimiter is a string used to split the input, defaulting to a single space (' ').
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` and converting each split part to an integer.
#Overall this is what the function does:The function `func_4` accepts a parameter `delimiter` (a string, defaulting to a single space ' ') and returns a list of integers. These integers are obtained by splitting the string returned by `func_2()` using the specified `delimiter` and converting each resulting substring to an integer. The function does not modify any external state or variables.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_5():
    return func_2()
    #The program returns the value or output of `func_2()`, which is not defined in the initial state.
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of calling `func_2()`. The final state of the program after the function concludes is that it has the return value of `func_2()`, which is not defined in the initial state.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m <= 2 * 10^5, and 1 <= k <= 2 * 10^5. A is a list of n integers where 1 <= A[i] <= 2 * 10^9 and A[i] < A[i+1]. D is a sorted list of unique integers derived from a list of m integers where 1 <= D[i] <= 10^9. F is a list of k integers where 1 <= F[i] <= 10^9.
def func_6():
    n, m, k = func_4()
    A = func_4()
    D = sorted(set(func_4()))
    F = func_4()
    max_diff, next_max_diff, index = -inf, -inf, None
    for i in range(1, n):
        diff = A[i] - A[i - 1]
        
        if diff > max_diff:
            next_max_diff = max_diff
            max_diff = diff
            index = i
        elif diff > next_max_diff:
            next_max_diff = diff
        
    #State: `n`, `m`, and `k` remain unchanged. `A` remains unchanged. `D` remains unchanged. `F` remains unchanged. `max_diff` is the maximum difference between any two consecutive elements in `A`. `next_max_diff` is the second maximum difference between any two consecutive elements in `A`. `index` is the index of the element in `A` where the maximum difference occurs.
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
        
    #State: `n`, `m`, and `k` remain unchanged. `A` remains unchanged. `D` remains unchanged. `F` remains unchanged. `max_diff` remains unchanged. `next_max_diff` remains unchanged. `index` remains unchanged. `left` remains unchanged. `right` remains unchanged. `ans` is the minimum value of `max(D[l] + f - left, right - D[l] - f)` for all `f` in `F` where `l` is the index found by the binary search in the loop.
    print(max(ans, next_max_diff))
    #This is printed: - Since the exact values of `D`, `F`, `left`, `right`, and `next_max_diff` are not provided, we can't compute the exact numerical value of `ans` or `next_max_diff`.
    #   - However, based on the given information, the print statement will output the larger of the two values: `ans` and `next_max_diff`.
    #
    #Output:
#Overall this is what the function does:The function `func_6` accepts no parameters and returns no values. It operates on integers `n`, `m`, and `k`, and lists `A`, `D`, and `F` with specific constraints. The function identifies the maximum and second maximum differences between consecutive elements in the sorted list `A`. It then uses a binary search to find the minimum possible maximum difference between a modified value from `D` and the elements `left` and `right` in `A`, where `left` and `right` are the elements surrounding the maximum difference. Finally, the function prints the larger of the two values: the minimum possible maximum difference found or the second maximum difference. The state of `n`, `m`, `k`, `A`, `D`, and `F` remains unchanged throughout the function's execution.

#State of the program right berfore the function call: No input variables are used in the function signature.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is the return value of `func_3()`.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves a number of test cases by calling `func_3` and then iterates that many times, calling `func_6` in each iteration. The function does not return any value. After the function concludes, the variable `testcases` holds the return value of `func_3`, and `func_6` has been called `testcases` times.

