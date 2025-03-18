#State of the program right berfore the function call: func is a callable function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns the `wrapper` function, which is a callable function.
#Overall this is what the function does:The function `func_1` accepts a parameter `func`, which is a callable function, and returns a `wrapper` function, which is also a callable function. The `wrapper` function is returned without any modifications or additional behavior being attached to it.

#State of the program right berfore the function call: args is a tuple of arguments that can be passed to the function `func`, and `d` is a dictionary that maps tuples of arguments to their computed results by `func`.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple of arguments that can be passed to the function `func`, and `d` is a dictionary that maps tuples of arguments to their computed results by `func`. If `args` is not a key in `d`, then `args` is added as a key in `d` with its value set to the result of `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the computed result of `func(*args)` if `args` is a key in the dictionary `d`. If `args` is not a key in `d`, it is added as a key with its value set to the result of `func(*args)`, and then the program returns this result.
#Overall this is what the function does:The function `wrapper` checks if the tuple `args` is a key in the dictionary `d`. If `args` is not a key, it adds `args` to `d` with the value being the result of `func(*args)`. The function then returns the value associated with `args` in `d`.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the first line of input from the user, with any trailing whitespace removed.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling `func_2()`.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an integer value that is the result of calling `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input, defaulting to a single space (' ').
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` string, which defaults to a single space (' '), and then converting each split part to an integer.
#Overall this is what the function does:The function `func_4` accepts a parameter `delimiter` (a string, defaulting to a single space ' ') and returns a list of integers. This list is obtained by splitting the string returned by `func_2()` using the specified `delimiter` and then converting each split part to an integer. The function does not modify any external state or variables.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_5` does not take any parameters.
def func_5():
    return func_2()
    #The program returns the value or result produced by the function `func_2()`.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It returns the value or result produced by the function `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m <= 2 * 10^5, and 1 <= k <= 2 * 10^5. A is a list of n integers in strictly increasing order, where 1 <= A[i] <= 2 * 10^9. D is a sorted list of unique integers derived from a list of m integers, where 1 <= D[i] <= 10^9. F is a list of k integers, where 1 <= F[i] <= 10^9.
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
        
    #State: `A` is a list of `n` integers in strictly increasing order, where 1 <= A[i] <= 2 * 10^9. `n` is the length of `A` and must be greater than or equal to 2. `m` and `k` are assigned the values returned by `func_4()`. `D` is a sorted list of unique integers derived from the list returned by `func_4()`, where 1 <= D[i] <= 10^9. `F` is a list of `k` integers, where 1 <= F[i] <= 10^9, and `F` is the list returned by `func_4()`. `max_diff` is the largest difference between any two consecutive elements in `A`. `next_max_diff` is the second largest difference between any two consecutive elements in `A`. `index` is the index of the element in `A` that follows the largest difference. `i` is `n - 1`, and `diff` is the difference between the last two elements in `A` (i.e., `A[n-1] - A[n-2]`).
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
        
    #State: `A` remains a list of `n` integers in strictly increasing order, `n` is the length of `A` and must be greater than or equal to 2, `m` and `k` are assigned the values returned by `func_4()`, `D` remains a sorted list of unique integers derived from the list returned by `func_4()`, `F` remains a list of `k` integers returned by `func_4()`, `max_diff` remains the largest difference between any two consecutive elements in `A`, `next_max_diff` remains the second largest difference between any two consecutive elements in `A`, `index` remains the index of the element in `A` that follows the largest difference, `i` remains `n - 1`, `diff` remains the difference between the last two elements in `A`, `left` remains `A[index - 1]`, `right` remains `A[index]`, `ans` is the minimum of the initial `ans` and the maximum of `D[l] + F[j] - left` and `right - D[l] - F[j]` for all `j` in `0` to `k-1` where `l` is the index found by the binary search for each `f` in `F`, `l` is the final index found by the binary search for the last `f` in `F`, `h` is the final index found by the binary search for the last `f` in `F`, `mid` is the final value of `l` (or `h`) for the last `f` in `F`, `mid_sum` is `D[mid] + F[k-1]`, and `mid_next_sum` is `D[mid + 1] + F[k-1]` if `mid + 1` is within the bounds of `D`, otherwise `mid_next_sum` is undefined.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum of the initial ans and the maximum of D[l] + F[j] - left and right - D[l] - F[j] for all j in 0 to k-1, and next_max_diff is the second largest difference between any two consecutive elements in A)
#Overall this is what the function does:The function `func_6` processes three lists `A`, `D`, and `F` with specific constraints. It identifies the largest and second largest differences between consecutive elements in `A`. It then uses a binary search on `D` to find the minimum possible maximum difference that can be achieved by adding elements from `F` to elements in `D` and adjusting the gap between the identified largest difference in `A`. Finally, it prints the maximum of this adjusted minimum difference and the second largest difference in `A`. The function does not return any value, and the lists `A`, `D`, and `F` remain unchanged after the function concludes.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_7` does not take any parameters.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` must be greater than 0, `func_6()` has been called `testcases` times.
#Overall this is what the function does:The function `func_7` does not accept any parameters and does not return any value. It calls `func_3` to get a number of test cases, and then calls `func_6` that many times. After the function concludes, `testcases` is greater than 0, and `func_6` has been executed `testcases` times.

