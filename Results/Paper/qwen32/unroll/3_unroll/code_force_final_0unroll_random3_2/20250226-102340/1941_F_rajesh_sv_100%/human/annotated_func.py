#State of the program right berfore the function call: func is a function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a function named `wrapper`
#Overall this is what the function does:The function `func_1` accepts a function `func` as a parameter and returns a new function named `wrapper`.

#State of the program right berfore the function call: args is a tuple containing arguments that can be of any type and value.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple containing arguments that can be of any type and value. If `args` was not in `d`, `d` now contains a new key-value pair where the key is `args` and the value is `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the value associated with the key `args` in the dictionary `d`. If `args` was not originally in `d`, it now contains a new key-value pair where the key is `args` and the value is `func(*args)`, and the program returns `func(*args)`. If `args` was already in `d`, the program returns the previously stored value associated with `args`.
#Overall this is what the function does:The function returns the value associated with the key `args` in the dictionary `d`. If `args` was not originally in `d`, it adds a new key-value pair to `d` where the key is `args` and the value is the result of `func(*args)`, and then returns this result. If `args` was already in `d`, it returns the previously stored value associated with `args`.

#State of the program right berfore the function call: This function does not have any parameters, and it returns a string which is a line read from standard input, stripped of leading and trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string which is a line read from standard input, stripped of leading and trailing whitespace.
#Overall this is what the function does:The function reads a line from standard input and returns it as a string with leading and trailing whitespace removed.

#State of the program right berfore the function call: No variables in the function signature. This function does not take any parameters and does not provide information about the variables used in the problem description.
def func_3():
    return int(func_2())
    #The program returns the integer value returned by the function `func_2()`
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns the integer value returned by the function `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers, where the input string is expected to contain integers separated by the delimiter.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers, each integer obtained by splitting the input string returned by `func_2()` using the `delimiter` string.
#Overall this is what the function does:The function accepts a `delimiter` string and returns a list of integers by splitting an input string (obtained from `func_2()`) using the `delimiter`.

#State of the program right berfore the function call: This function does not have any parameters, so there are no variables or relationships to describe.
def func_5():
    return func_2()
    #The program returns the result of the function `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of the function `func_2()`.

#State of the program right berfore the function call: n, m, and k are positive integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a list of n integers representing the complexities of the prepared problems, sorted in strictly ascending order. D is a sorted list of unique integers representing the complexities of the models. F is a list of k integers representing the complexities of the functions.
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
        
    #State: `max_diff` is the largest difference between consecutive elements in list `A`, `next_max_diff` is the second largest difference between consecutive elements in list `A`, `index` is the index of the element that is part of the pair with the largest difference, `n`, `m`, `k`, `A`, `D`, `F` remain unchanged.
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
        
    #State: `max_diff` is the largest difference between consecutive elements in list `A`, `next_max_diff` is the second largest difference between consecutive elements in list `A`, `index` is the index of the element that is part of the pair with the largest difference, `left` is `A[index - 1]`, `right` is `A[index]`, `n`, `m`, `k`, `A`, `D`, `F` remain unchanged, `ans` is the smallest possible maximum difference found during the binary searches for each `f` in `F`.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the smallest possible maximum difference found during the binary searches for each f in F, and next_max_diff is the second largest difference between consecutive elements in list A)
#Overall this is what the function does:The function calculates and prints the maximum of two values: the second largest difference between consecutive elements in a sorted list `A` of problem complexities, and the smallest possible maximum difference found during a series of binary searches involving the complexities of models `D` and functions `F`.

#State of the program right berfore the function call: No variables are specified in the function signature of `func_7`, so no precondition can be derived from it.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` holds the value returned by `func_3()`.
#Overall this is what the function does:The function `func_7` executes a series of operations based on the number of test cases returned by `func_3()`. It calls `func_6()` for each test case, but it does not return any specific value or modify any external variables.

