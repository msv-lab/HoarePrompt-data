#State of the program right berfore the function call: func is a callable function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a callable function named `wrapper`.
#Overall this is what the function does:The function `func_1` accepts a callable function `func` and returns a callable function named `wrapper`. The function `func_1` does not modify any input parameters and does not perform any actions other than creating and returning the `wrapper` function.

#State of the program right berfore the function call: args is a tuple of arguments that can be passed to the function `func`.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple of arguments that can be passed to the function `func`. If `args` is not present as a key in the dictionary `d` before the execution of the code, `d` now contains `args` as a key with the value `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the value of `func(*args)` if `args` was not previously a key in the dictionary `d`. If `args` was already a key in `d`, the program returns the value associated with `args` in `d`.
#Overall this is what the function does:The function `wrapper` accepts no parameters and returns the result of `func(*args)` if `args` is not already a key in the dictionary `d`. If `args` is already a key in `d`, it returns the value associated with `args` in `d`. The function ensures that `d` contains the result of `func(*args)` for the given `args` after the function concludes.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads the first line of input from the user via `sys.stdin`, removes any trailing whitespace from this line, and returns the resulting string. The function does not modify any external variables or state.

#State of the program right berfore the function call: This function does not have any input variables.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling `func_2()`.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It returns an integer value that is the result of calling `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` and converting each split part into an integer.
#Overall this is what the function does:The function `func_4` accepts a parameter `delimiter` and returns a list of integers. This list is obtained by splitting the string returned by `func_2()` using the `delimiter` and converting each resulting substring into an integer.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any arguments.
def func_5():
    return func_2()
    #The program returns the result of the function `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of the function `func_2()`. After the function concludes, the program state is unchanged except for the returned value, which is the result of `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m <= 2 * 10^5, and 1 <= k <= 2 * 10^5. A is a sorted list of n integers where 1 <= A[i] <= 2 * 10^9 and A[i] < A[i+1]. D is a sorted list of unique integers derived from m integers where 1 <= D[i] <= 10^9. F is a list of k integers where 1 <= F[i] <= 10^9.
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
        
    #State: `A` remains the list returned by `func_4()`, `n`, `m`, and `k` remain the values returned by `func_4()`, `D` remains a sorted list of unique integers derived from the list returned by `func_4()` where 1 <= D[i] <= 10^9, `F` remains the list of `k` integers where 1 <= F[i] <= 10^9, `max_diff` is the maximum difference between consecutive elements in `A`, `next_max_diff` is the second maximum difference between consecutive elements in `A`, `index` is the index of the element in `A` where the maximum difference occurs.
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
        
    #State: `A` remains the same list of integers, `n`, `m`, and `k` remain the same values, `D` remains the same sorted list of unique integers, `F` remains the same list of `k` integers, `max_diff` remains the maximum difference between consecutive elements in `A`, `next_max_diff` remains the second maximum difference between consecutive elements in `A`, `index` remains the index of the element in `A` where the maximum difference occurs, `left` remains `A[index - 1]`, `right` remains `A[index]`, `ans` is updated to the minimum value of the maximum differences calculated for each `f` in `F`.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum value of the maximum differences calculated for each f in F, and next_max_diff is the second maximum difference between consecutive elements in A)
#Overall this is what the function does:The function `func_6` takes no parameters and returns no value. It operates on three integers `n`, `m`, and `k`, and three lists `A`, `D`, and `F` that are provided by the `func_4` function. The function identifies the maximum and second maximum differences between consecutive elements in the sorted list `A`. It then calculates a new value `ans` by finding the minimum of the maximum differences between the adjusted elements of `D` and the elements `left` and `right` from `A` (where `left` and `right` are the elements around the maximum difference in `A`). Finally, it prints the maximum of `ans` and `next_max_diff`. The state of `A`, `D`, and `F` remains unchanged, and the function does not modify any global variables or have any side effects other than printing the result.

#State of the program right berfore the function call: No variables are passed to the function `func_7`.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` remains the value returned by `func_3()`, and no other variables are affected.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It calls `func_3` to get a number of test cases, and then iterates that many times, calling `func_6` in each iteration. After the function concludes, the variable `testcases` retains the value returned by `func_3`, and no other variables are affected. The function does not return any value.

