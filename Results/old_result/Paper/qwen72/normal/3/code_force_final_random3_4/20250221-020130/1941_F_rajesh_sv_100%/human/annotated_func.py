#State of the program right berfore the function call: func is a callable function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns `wrapper`, which is a callable function.
#Overall this is what the function does:The function `func_1` accepts a callable function `func` and returns a new callable function `wrapper`. The function does not modify the input `func` or any external state; it simply creates and returns the `wrapper` function.

#State of the program right berfore the function call: args is a tuple of arguments that can be passed to func, and d is a dictionary that maps tuples of arguments to their computed results by func.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple of arguments that can be passed to `func`, and `d` is a dictionary that maps tuples of arguments to their computed results by `func`. If `args` is not already a key in `d`, the current tuple `args` is added as a key in `d`, and the value associated with `args` in `d` is the result of `func(*args)`. If `args` is already a key in `d`, no changes are made to `d`.
    return d[args]
    #The program returns the value associated with the tuple `args` in the dictionary `d`. If `args` is already a key in `d`, the value is the previously computed result of `func(*args)`. If `args` is not a key in `d`, the value is the result of `func(*args)` and `args` is added as a key in `d` with this result.
#Overall this is what the function does:The function `wrapper` does not accept any parameters. It checks if the tuple `args` is a key in the dictionary `d`. If `args` is not a key in `d`, it computes the result of `func(*args)`, adds `args` as a key in `d` with this result, and returns the result. If `args` is already a key in `d`, it returns the value associated with `args` in `d`, which is the previously computed result of `func(*args)`.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read a line from standard input, typically for input handling in the overall solution.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the next line of input from the standard input, with any trailing whitespace (including the newline character) removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads the next line from standard input and returns the line with any trailing whitespace (including the newline character) removed.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling `func_2()`.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It returns an integer value that is the result of calling the function `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input, and by default it is a single space (' ').
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` (which is a single space by default) and converting each split part into an integer.
#Overall this is what the function does:The function `func_4` accepts an optional parameter `delimiter` (a string, default is a single space ' '). It returns a list of integers obtained by splitting the string returned by `func_2()` using the specified `delimiter` and converting each split part into an integer.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_5():
    return func_2()
    #The program returns the result of the function `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of calling the function `func_2`. After the function concludes, the program state is unchanged except for the return value, which is the result of `func_2`.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a list of n integers in strictly increasing order, where 1 <= A[i] <= 2 * 10^9. D is a sorted list of unique integers representing the complexities of the models, where 1 <= d_i <= 10^9. F is a list of k integers representing the complexities of the functions, where 1 <= f_i <= 10^9.
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
        
    #State: `max_diff` is the largest difference between consecutive elements in the list `A`, `next_max_diff` is the second largest difference between consecutive elements in the list `A`, and `index` is the index of the element in `A` where the largest difference occurs. The values of `n`, `m`, `k`, `D`, and `F` remain unchanged.
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
        
    #State: `ans` is the minimum possible value of the maximum difference between `D[l] + f - left` and `right - D[l] - f` for each `f` in `F`, while `max_diff`, `next_max_diff`, `index`, `left`, `right`, `n`, `m`, `k`, `D`, and `F` remain unchanged.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum possible value of the maximum difference between D[l] + f - left and right - D[l] - f for each f in F, and next_max_diff is a predefined value)
#Overall this is what the function does:The function `func_6` takes no explicit parameters but uses values returned from `func_4` to determine the largest and second largest differences between consecutive elements in a strictly increasing list `A`. It then calculates the minimum possible value of the maximum difference between `D[l] + f - left` and `right - D[l] - f` for each `f` in `F`, where `D` is a sorted list of unique integers, and `left` and `right` are the elements in `A` where the largest difference occurs. Finally, it prints the maximum of this calculated value and the second largest difference found in `A`. The function does not return any value.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_7` does not take any parameters.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` remains unchanged, and the state of any variables modified by `func_6()` within the loop will reflect the final state after all iterations.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves a number of test cases by calling `func_3()` and then iterates this number of times, calling `func_6()` in each iteration. After the function concludes, the variable `testcases` remains unchanged, and any variables modified by `func_6()` will reflect their final state after all iterations. The function does not return any value.

