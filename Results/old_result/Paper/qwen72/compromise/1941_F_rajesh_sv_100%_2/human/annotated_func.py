#State of the program right berfore the function call: func is a callable function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a variable named `wrapper`, but no specific information is provided about what `wrapper` is or what it contains. Since `func` is a callable function and `d` is an empty dictionary, it is likely that `wrapper` is a function or object that wraps around `func` or uses `d` in some way, but without more context, we can only say that `wrapper` is being returned.
#Overall this is what the function does:The function `func_1` accepts a callable function `func` and returns a variable named `wrapper`. The function does not modify any input parameters or perform any actions other than defining an empty dictionary `d` and returning `wrapper`. The exact nature and content of `wrapper` are not specified in the code.

#State of the program right berfore the function call: args is a tuple containing any number of arguments of any type, and d is a dictionary that maps tuples to values.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple containing any number of arguments of any type, and `d` is a dictionary that maps tuples to values. If `args` is not already a key in `d`, `d` is updated to map `args` to the value returned by `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the value associated with the tuple `args` in the dictionary `d`. If `args` was not a key in `d` before, `d` is updated to map `args` to the value returned by `func(*args)`, and this value is returned. If `args` was already a key in `d`, the existing value associated with `args` is returned, and `d` remains unchanged.
#Overall this is what the function does:The function `wrapper` operates on a global or external `args` tuple and a global or external dictionary `d`. It returns the value associated with `args` in `d`. If `args` is not a key in `d`, it updates `d` to map `args` to the value returned by `func(*args)` and returns this value. If `args` is already a key in `d`, it returns the existing value associated with `args` without modifying `d`.

#State of the program right berfore the function call: No input variables are used in the function signature.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is read from the standard input (stdin) and stripped of leading and trailing whitespace.
#Overall this is what the function does:The function reads a line of input from the standard input (stdin), removes any leading and trailing whitespace from it, and returns the resulting string.

#State of the program right berfore the function call: None, as the function `func_3` does not have any parameters.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling `func_2()`.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It returns an integer value that is the result of calling `func_2()`. The final state of the program after the function concludes is that an integer value is returned, which is the output of `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` string and then converting each split part into an integer.
#Overall this is what the function does:The function `func_4` accepts a string `delimiter` and returns a list of integers. This list is obtained by splitting the string returned by `func_2()` using the `delimiter` and converting each resulting substring into an integer.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_5():
    return func_2()
    #The program returns the result of the function `func_2()`.
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of the function `func_2()`. After the function concludes, the program state is such that the result of `func_2()` is available to the caller.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a sorted list of n integers where 1 <= A[i] <= 2 * 10^9 and A[i] < A[i+1]. D is a sorted list of unique integers derived from m integers where 1 <= D[i] <= 10^9. F is a list of k integers where 1 <= F[i] <= 10^9.
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
        
    #State: `A` is a sorted list of `n` integers where 1 <= `A[i]` <= 2 * 10^9 and `A[i] < A[i+1]`, `n` is greater than or equal to the number of iterations, `i` is `n-1`, `m` and `k` are updated to the values returned by `func_4()`, `D` is a sorted list of unique integers derived from the values returned by `func_4()`, where 1 <= `D[i]` <= 10^9, `F` is a list of `k` integers where 1 <= `F[i]` <= 10^9, and `F` is now equal to the list returned by `func_4()`, `max_diff` is the largest difference between consecutive elements in `A`, `next_max_diff` is the second largest difference between consecutive elements in `A`, and `index` is the index of the element in `A` where the largest difference occurs.
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
        
    #State: The loop has finished executing, and `l` is equal to `h` for each iteration. The variable `mid` is the final index where `l` and `h` converge, and `mid_sum` is `D[mid] + f`. For each value `f` in `F`, `ans` is updated to the minimum of its previous value and the maximum of `D[l] + f - left` and `right - D[l] - f`. After all iterations, `ans` will be the minimum value of the maximum differences calculated for each `f` in `F`. The other variables (`A`, `n`, `i`, `m`, `k`, `D`, `F`, `max_diff`, `next_max_diff`, `index`, `left`, `right`) retain their values from the initial state.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum value of the maximum differences calculated for each f in F, and next_max_diff retains its initial value)
#Overall this is what the function does:The function `func_6` processes three lists: `A`, a sorted list of integers; `D`, a sorted list of unique integers; and `F`, a list of integers. It finds the largest and second largest differences between consecutive elements in `A`, and then iterates through each element in `F` to find the minimum possible maximum difference between a modified element from `D` and the elements around the largest difference in `A`. Finally, it prints the maximum of this minimum value and the second largest difference found in `A`. The function does not return any value.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_7` does not take any parameters.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` must be greater than or equal to the number of iterations the loop has executed, `_` is a dummy variable, and the function `func_6()` has been called and returned for each iteration.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves the number of test cases by calling `func_3` and then iterates that many times, calling `func_6` in each iteration. After the function concludes, the variable `testcases` holds the number of iterations that were executed, and `func_6` has been called `testcases` times. The function does not return any value.

