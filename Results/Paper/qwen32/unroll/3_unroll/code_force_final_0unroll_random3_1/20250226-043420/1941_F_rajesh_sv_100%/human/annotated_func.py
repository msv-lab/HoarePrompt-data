#State of the program right berfore the function call: func is a function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns the variable `wrapper` which is not defined in the given initial state.
#Overall this is what the function does:The function `func_1` accepts a parameter `func`, which is expected to be a function, and returns a variable `wrapper`. However, the variable `wrapper` is not defined within the provided code, leading to a potential error.

#State of the program right berfore the function call: args is a tuple containing any number of arguments of any type.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple containing any number of arguments of any type. If `args` was not already a key in the dictionary `d`, then `d` now contains the key `args` with the value `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the value associated with the key `args` in the dictionary `d`. This value is the result of `func(*args)` if `args` was not already a key in `d`, or it is the previously stored value if `args` was already a key in `d`.
#Overall this is what the function does:The function `wrapper` returns the result of calling `func` with the arguments provided in `args`. If the same arguments have been used before, it returns the cached result from the dictionary `d` instead of recomputing it.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the string read from standard input, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a string read from standard input, with leading and trailing whitespace removed.

#State of the program right berfore the function call: This function does not have any parameters, so there are no variables or relationships to describe.
def func_3():
    return int(func_2())
    #The program returns the integer value returned by the function `func_2()`
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns the integer value returned by the function `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers, where the default value is a space (' ').
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers, where the integers are the result of splitting the string returned by `func_2()` using the `delimiter`.
#Overall this is what the function does:The function accepts a string `delimiter` and returns a list of integers obtained by splitting the string returned by `func_2()` using the specified `delimiter`.

#State of the program right berfore the function call: This function does not take any parameters, so there are no variables to describe in terms of preconditions.
def func_5():
    return func_2()
    #The program returns the result of func_2()
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers where 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. D is a list of m integers where 1 <= d_i <= 10^9. F is a list of k integers where 1 <= f_j <= 10^9.
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
        
    #State: `n`, `m`, `k`, `A`, `D`, `F`, `max_diff` (largest difference), `next_max_diff` (second largest difference), `index` (index of the largest difference).
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
        
    #State: n, m, k, A, D, F, max_diff, next_max_diff, index, left, right, ans is the minimum of the maximum differences found during the loop iterations.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum of the maximum differences found during the loop iterations and next_max_diff is the maximum difference found in the current or most recent iteration)
#Overall this is what the function does:The function calculates and prints the maximum of two values: the second largest difference between consecutive elements in a sorted list `A`, and the minimum of the maximum differences found when adjusting elements in another list `D` by values in a third list `F`.

#State of the program right berfore the function call: testcases is a non-negative integer representing the number of test cases, and func_3() and func_6() are functions that provide the necessary input data and perform the required computations for each test case, respectively.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` remains the same value returned by `func_3()`. No other variables are affected by the loop.
#Overall this is what the function does:The function `func_7` processes a number of test cases specified by a non-negative integer. For each test case, it performs computations using the functions `func_3()` to obtain input data and `func_6()` to carry out the required operations. The function does not return any specific value but completes the computations for each test case.

