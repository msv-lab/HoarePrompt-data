#State of the program right berfore the function call: func is a function that is expected to be used in the context of the problem, although the provided function signature does not fully describe its parameters or return type.
def func_1(func):
    d = {}
    return wrapper
    #The program returns `wrapper`.
#Overall this is what the function does:The function `func_1` accepts a function `func` as a parameter and returns another function named `wrapper`.

#State of the program right berfore the function call: args is a tuple containing arguments that the function `func` will take, and `d` is a dictionary used to store the results of `func` for given arguments to avoid redundant calculations.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple containing arguments that the function `func` will take, and `d` is a dictionary used to store the results of `func` for given arguments to avoid redundant calculations. If `args` was not originally a key in `d`, it is now a key in the dictionary `d` with its value set to the result of `func(*args)`. If `args` was already a key in `d`, the dictionary `d` remains unchanged.
    return d[args]
    #The program returns the result of `func(*args)` if `args` was not originally a key in `d`. If `args` was already a key in `d`, it returns the previously stored value associated with `args` in `d`.
#Overall this is what the function does:The function accepts a tuple `args` containing arguments and a dictionary `d` to store results. It returns the result of `func(*args)` if `args` is not already a key in `d`. If `args` is already a key in `d`, it returns the previously stored value associated with `args` in `d`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. This function does not take any parameters and returns a string read from standard input, stripped of leading and trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is read from standard input and stripped of any leading and trailing whitespace.
#Overall this is what the function does:The function `func_2` reads a line of text from standard input, removes any leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_3`. Therefore, no precondition can be derived based on the variables in the function signature.
def func_3():
    return int(func_2())
    #The program returns the integer value returned by `func_2()`
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns the integer value returned by `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` string and converting each split part into an integer.
#Overall this is what the function does:The function accepts a `delimiter` string, splits the string returned by `func_2()` using this `delimiter`, and returns a list of integers obtained by converting each part of the split string into an integer.

#State of the program right berfore the function call: No variables are present in the function signature of `func_5()`. Therefore, no precondition can be derived from the variables in the function signature.
def func_5():
    return func_2()
    #The program returns the result of `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers representing the number of prepared problems, the number of models, and the number of functions, respectively, such that 2 <= n <= 10^5, 1 <= m <= 2 * 10^5, and 1 <= k <= 2 * 10^5. A is a list of integers representing the complexities of the prepared problems, sorted in ascending order, with length n and each element satisfying 1 <= a_i <= 2 * 10^9. D is a sorted list of unique integers representing the complexities of the models, with length m and each element satisfying 1 <= d_i <= 10^9. F is a list of integers representing the complexities of the functions, with length k and each element satisfying 1 <= f_i <= 10^9.
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
        
    #State: `n` is the length of list `A`, `m` and `k` remain unchanged, `A` and `D` remain unchanged, `F` remains unchanged, `max_diff` holds the maximum difference between consecutive elements in `A`, `next_max_diff` holds the second largest difference between consecutive elements in `A`, and `index` holds the index of the element in `A` where `max_diff` occurs.
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
        
    #State: `n` is the length of list `A`, `m` and `k` remain unchanged, `A` and `D` remain unchanged, `F` remains unchanged, `max_diff` holds the maximum difference between consecutive elements in `A`, `next_max_diff` holds the second largest difference between consecutive elements in `A`, `index` holds the index of the element in `A` where `max_diff` occurs, `left` is `A[index - 1]`, and `right` is `A[index]`. `ans` is the minimum of its initial value and all values computed as `max(D[l] + f - left, right - D[l] - f)` for each `f` in `F`.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum of its initial value and all values computed as max(D[l] + f - left, right - D[l] - f) for each f in F, and next_max_diff is the second largest difference between consecutive elements in A)
#Overall this is what the function does:The function `func_6` calculates and prints the maximum of two values: the second largest difference between consecutive elements in the sorted list `A` (representing complexities of prepared problems), and a computed value `ans` which is the minimum of the initial maximum difference between consecutive elements in `A` and values derived from the complexities of models in `D` and functions in `F`.

#State of the program right berfore the function call: testcases is a positive integer representing the number of test cases.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is 1 and `func_6()` has been executed 3 times.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It processes a number of test cases, which is determined by the value returned from `func_3()`. For each test case, it executes `func_6()`. The final state of the program after it concludes is that all test cases have been processed by executing `func_6()` the corresponding number of times.

