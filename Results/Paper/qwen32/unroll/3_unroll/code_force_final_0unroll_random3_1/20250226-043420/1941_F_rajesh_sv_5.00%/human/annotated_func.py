#State of the program right berfore the function call: func is a function, but the variables d and wrapper are not defined or used in the provided snippet, so no specific relationship or precondition can be inferred from the given function signature alone.
def func_1(func):
    d = {}
    return wrapper
    #The program returns `wrapper`, which is a function.
#Overall this is what the function does:The function `func_1` accepts a function `func` as a parameter and returns another function `wrapper`.

#State of the program right berfore the function call: args is a tuple containing any type and number of values.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple containing any type and number of values. If `args` was not already in the dictionary `d`, then `d` now contains the entry `args: func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the value of `d[args]`. This value is the result of `func(*args)` if `args` was not already in the dictionary `d` when the code was executed. If `args` was already in the dictionary `d`, it returns the previously stored value associated with `args`.
#Overall this is what the function does:The function `wrapper` accepts a tuple `args` containing any type and number of values. It returns the result of `func(*args)`, caching the result in a dictionary `d` to avoid redundant computations. If `args` is already in `d`, it returns the cached result.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the input string provided by the user, stripped of any leading or trailing whitespace.
#Overall this is what the function does:The function `func_2` reads a line of input from the user, removes any leading or trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: This function does not take any parameters, so there are no variables or relationships to describe.
def func_3():
    return int(func_2())
    #The program returns the integer value returned by `func_2()`
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns the integer value returned by `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers, where the input string is expected to contain integers separated by the delimiter.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` string and converting each split substring into an integer.
#Overall this is what the function does:The function accepts a `delimiter` string, splits a string obtained from `func_2()` using this delimiter, converts each split substring into an integer, and returns a list of these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_5`, so there are no preconditions to describe.
def func_5():
    return func_2()
    #The program returns the result of `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a list of n integers representing the complexities of the prepared problems, sorted in ascending order with 1 <= a_i <= 2 * 10^9. D is a sorted list of unique integers representing the complexities of the models with 1 <= d_i <= 10^9. F is a list of k integers representing the complexities of the functions with 1 <= f_i <= 10^9.
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
        
    #State: A is the value returned by `func_4()`, n, m, and k are updated to the values returned by `func_4()`, D is a sorted list of unique integers returned by `func_4()`, F is the list returned by `func_4()`, max_diff is the largest difference between consecutive elements in A, next_max_diff is the second-largest difference between consecutive elements in A, index is the index of the larger element in the pair with the largest difference.
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
        
    #State: `A` is the value returned by `func_4()`, `n`, `m`, and `k` are updated to the values returned by `func_4()`, `D` is a sorted list of unique integers returned by `func_4()`, `F` is the list returned by `func_4()`, `max_diff` is the largest difference between consecutive elements in `A`, `next_max_diff` is the second-largest difference between consecutive elements in `A`, `index` is the index of the larger element in the pair with the largest difference, `left` is `A[index - 1]`, `right` is `A[index]`, `ans` is the minimum possible value of the maximum difference between `left` and `right` after adjusting by any `f` in `F`.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum possible value of the maximum difference between left and right after adjusting by any f in F, and next_max_diff is the second-largest difference between consecutive elements in A)
#Overall this is what the function does:The function calculates and prints the maximum of two values: the second-largest difference between consecutive elements in the sorted list `A`, and the minimum possible value of the maximum difference between a pair of consecutive elements in `A` after adjusting by any element in `F`.

#State of the program right berfore the function call: testcases is a positive integer representing the number of test cases.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `func_6()` has been called `testcases` times.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It executes `func_6` a number of times equal to the positive integer value returned by `func_3`.

