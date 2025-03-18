#State of the program right berfore the function call: func is a callable function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a function named `wrapper`, which is a callable function.
#Overall this is what the function does:The function `func_1` accepts a callable function `func` and returns a new callable function named `wrapper`. The function `func_1` does not modify the input `func` or any other external state; it simply creates and returns the `wrapper` function.

#State of the program right berfore the function call: args is a tuple of arguments that can be passed to the function `func`, and `d` is a dictionary used for memoization.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple of arguments that can be passed to the function `func`, and `d` is a dictionary used for memoization. If `args` is not in `d`, `d[args]` is set to the result of `func(*args)`, and `args` is now a key in `d`. If `args` is already in `d`, the state of `d` remains unchanged.
    return d[args]
    #The program returns the value associated with the key `args` in the dictionary `d`. If `args` was not initially in `d`, the value returned is the result of `func(*args)`, and `args` is now a key in `d`. If `args` was already in `d`, the value returned is the previously stored result of `func(*args)`.
#Overall this is what the function does:The `wrapper` function does not explicitly accept parameters but uses a tuple `args` and a dictionary `d` that are assumed to be defined in the outer scope. It checks if `args` is a key in the dictionary `d`. If `args` is not in `d`, it computes the result of `func(*args)`, stores this result in `d` with `args` as the key, and returns the result. If `args` is already in `d`, it simply returns the value associated with `args` in `d`. In both cases, the function ensures that `d` contains the result of `func(*args)` for the given `args`.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the first line of input from the user, with any leading or trailing whitespace removed.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_3` does not take any parameters.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling `func_2()`.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an integer value that is the result of calling `func_2()`. After the function concludes, the program has an integer value that represents the output of `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input, and it defaults to a single space (' ').
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` (which defaults to a single space ' ') and then converting each split part to an integer.
#Overall this is what the function does:The function `func_4` accepts a parameter `delimiter` (a string, defaulting to a single space ' '). It returns a list of integers by splitting the string returned from `func_2()` using the specified `delimiter` and converting each part to an integer.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_5` does not take any parameters.
def func_5():
    return func_2()
    #The program returns the result of `func_2()`, which is a value or variable produced by the execution of `func_2()`.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It returns the result of `func_2()`, which is the value or variable produced by the execution of `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a list of n integers in strictly increasing order (1 <= a_i <= 2 * 10^9, a_i < a_{i+1}). D is a sorted list of unique integers representing the complexities of the models (1 <= d_i <= 10^9). F is a list of k integers representing the complexities of the functions (1 <= f_i <= 10^9).
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
        
    #State: `n` is greater than 1, `i` is `n-1`, `m` and `k` are assigned the values returned by `func_4()`, `A` is a list of `n` integers in strictly increasing order (1 <= a_i <= 2 * 10^9, a_i < a_{i+1}), `D` is a sorted list of unique integers representing the complexities of the models (1 <= d_i <= 10^9), `F` is a list of integers returned by `func_4()` representing the complexities of the functions (1 <= f_i <= 10^9), `max_diff` is the largest difference between consecutive elements in `A`, `next_max_diff` is the second largest difference between consecutive elements in `A` (if it exists), `index` is the index of the element in `A` where the largest difference occurs.
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
        
    #State: The loop has finished executing, and the variables `l` and `h` have converged to the same index in `D` for each element `f` in `F`. The other variables (`n`, `i`, `m`, `k`, `A`, `D`, `F`, `max_diff`, `next_max_diff`, `index`, `left`, `right`) remain unchanged. The variable `ans` is updated to the minimum value of the maximum differences calculated for each `f` in `F` between `left` and `right` using the closest element in `D` to the midpoint between `left - f` and `right - f`.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum value of the maximum differences calculated for each f in F, and next_max_diff is an unchanged value)
#Overall this is what the function does:The function `func_6` processes a set of input variables `n`, `m`, `k`, `A`, `D`, and `F`. It identifies the largest and second largest differences between consecutive elements in the list `A`. It then calculates the minimum possible maximum difference between two elements in `A` by adjusting them using the elements in `F` and the closest elements in `D`. Finally, it prints the maximum of this minimum value and the second largest difference found in `A`. The function does not return any value.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_7` does not take any parameters.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` must be greater than or equal to the number of iterations, `func_6()` has been called `testcases` times.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves a number of test cases by calling `func_3()`, and then calls `func_6()` that many times. After the function concludes, `testcases` is a non-negative integer, and `func_6()` has been called `testcases` times. The function does not return any value.

