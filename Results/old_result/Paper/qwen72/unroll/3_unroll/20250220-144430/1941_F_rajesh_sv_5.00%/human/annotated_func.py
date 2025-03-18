#State of the program right berfore the function call: func is a callable function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a function named `wrapper`.
#Overall this is what the function does:The function `func_1` accepts a callable function `func` and returns a function named `wrapper`. The function `func_1` does not modify or use the provided `func` in any way within its body. After the function concludes, the returned `wrapper` function can be used independently, but it does not have any specific behavior or functionality defined within `func_1`.

#State of the program right berfore the function call: args is a tuple of arguments that can be passed to func, and d is a dictionary that maps tuples of arguments to their computed results by func.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple of arguments that can be passed to `func`, and `d` is a dictionary that maps tuples of arguments to their computed results by `func`. If `args` is not already a key in `d`, then `args` is added as a key and `d[args]` is set to the result of `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the computed result of `func(*args)` if `args` was not already a key in the dictionary `d`. If `args` was already a key in `d`, the program returns the value associated with `args` in `d`.
#Overall this is what the function does:The function `wrapper` accepts no parameters and returns the result of `func(*args)` if `args` is not already a key in the dictionary `d`. If `args` is already a key in `d`, it returns the value associated with `args` in `d`. The dictionary `d` is updated to include the result of `func(*args)` if `args` is not already a key.

#State of the program right berfore the function call: No variables are used in the function signature.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any trailing whitespace removed.
#Overall this is what the function does:The function `func_2` accepts no parameters and returns the first line of input from the user, with any trailing whitespace removed.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling the function `func_2()`.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an integer value that is the result of calling the function `func_2()`. After the function concludes, the program state includes a returned integer value.

#State of the program right berfore the function call: delimiter is a string used to split the input, defaulting to a single space ' '
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` (which defaults to a single space ' ') and then converting each resulting substring into an integer.
#Overall this is what the function does:The function `func_4` accepts a parameter `delimiter` (defaulting to a single space ' ') and returns a list of integers. This list is obtained by splitting the string returned by `func_2()` using the specified `delimiter` and converting each resulting substring into an integer. The state of the program after the function concludes includes the returned list of integers, and the `delimiter` parameter remains unchanged.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_5` does not take any parameters.
def func_5():
    return func_2()
    #The program returns the value or output produced by the function `func_2()`.
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the value or output produced by the function `func_2()`. After the function concludes, the program state is unchanged except for the return value, which is the result of `func_2()`.

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
            max_diff = diff
            index = i
        elif diff > next_max_diff:
            next_max_diff = diff
        
    #State: `max_diff` is the largest difference between consecutive elements in the list `A`, `next_max_diff` is the second largest difference between consecutive elements in the list `A`, and `index` is the index of the element in `A` that follows the largest difference. The values of `n`, `m`, `k`, `D`, and `F` remain unchanged.
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
        
    #State: `ans` is the minimum value of the maximum differences between `D[l] + f - left` and `right - D[l] - f` for all `f` in `F`, while `max_diff`, `next_max_diff`, `index`, `left`, `right`, `n`, `m`, `k`, `D`, and `F` remain unchanged.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum value of the maximum differences between D[l] + f - left and right - D[l] - f for all f in F, and next_max_diff is the value of next_max_diff)
#Overall this is what the function does:The function `func_6` processes three integers `n`, `m`, and `k`, and three lists `A`, `D`, and `F`. It finds the largest and second largest differences between consecutive elements in the sorted list `A`. Then, it calculates the minimum value of the maximum differences between `D[l] + f - left` and `right - D[l] - f` for all `f` in `F`, where `left` and `right` are the elements in `A` that define the largest difference. Finally, the function prints the maximum of this minimum value and the second largest difference found in `A`. The function does not return any value, but it prints the result. The original values of `n`, `m`, `k`, `D`, and `F` remain unchanged.

#State of the program right berfore the function call: No variables are passed to the function `func_7`.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is the result of `func_3()`, and no other variables are affected.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It calls `func_3` to determine the number of test cases, and then iterates that many times, calling `func_6` in each iteration. After the function concludes, the only variable affected is `testcases`, which holds the result of `func_3()`. No return value is specified.

