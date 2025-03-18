#State of the program right berfore the function call: func is a function that takes some arguments and returns a function named wrapper.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a function named `wrapper` which is returned by the function `func`.
#Overall this is what the function does:The function `func_1` accepts another function `func` as an argument and returns a function named `wrapper`.

#State of the program right berfore the function call: args is a tuple containing any number of arguments that can be passed to the function func.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple containing any number of arguments that can be passed to the function `func`. If `args` was not in the dictionary `d` before the execution, `d` now contains the key `args` with the value `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the value associated with the key `args` in the dictionary `d`. If `args` was not in `d` before the execution, it now contains the key `args` with the value `func(*args)`. Otherwise, it returns the pre-existing value associated with `args`.
#Overall this is what the function does:The function accepts a tuple `args` containing any number of arguments. It returns the value associated with the key `args` in the dictionary `d`. If `args` is not already a key in `d`, it computes the value by calling `func(*args)`, stores this value in `d` with `args` as the key, and then returns this value. Otherwise, it returns the pre-existing value associated with `args`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. Therefore, no precondition can be derived from the function signature alone.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is the next line of input from the standard input, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_2` reads the next line from the standard input, removes any leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: This function does not have any parameters, thus there are no variables or relationships to describe.
def func_3():
    return int(func_2())
    #The program returns the integer value returned by the function `func_2()`
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns the integer value returned by the function `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into components, which are then converted to integers and returned as a list.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers, where each integer is a component of the string returned by `func_2()`, split by the `delimiter` string.
#Overall this is what the function does:The function accepts a `delimiter` string and returns a list of integers. These integers are derived from splitting a string (obtained from `func_2()`) using the `delimiter` and converting each split component to an integer.

#State of the program right berfore the function call: This function does not take any parameters, and thus there are no variables or relationships to describe.
def func_5():
    return func_2()
    #The program returns the result of the function `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of the function `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m <= 2 * 10^5, and 1 <= k <= 2 * 10^5. A is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. D is a list of m integers where 1 <= d_i <= 10^9. F is a list of k integers where 1 <= f_i <= 10^9.
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
        
    #State: `A` is the tuple of values returned by `func_4()`, `n` is the value returned by `func_4()`, `m` is the value returned by `func_4()`, `k` is the value returned by `func_4()`, `D` is a sorted list of unique values from `func_4()`, `F` is the value returned by `func_4()`, `max_diff` is the maximum difference between consecutive elements in `A`, `next_max_diff` is the second maximum difference between consecutive elements in `A`, and `index` is the index where `max_diff` was found.
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
        
    #State: ans is the minimum possible value of the maximum difference between `left - f` and `right - f` for all `f` in `F`.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum possible value of the maximum difference between `left - f` and `right - f` for all `f` in `F`, and next_max_diff is another value in the context of the program)
#Overall this is what the function does:The function calculates and prints the maximum of two values: the second largest difference between consecutive elements in a sorted list `A`, and the minimum possible value of the maximum difference between adjusted elements from `A` and `D` for each value in `F`.

#State of the program right berfore the function call: testcases is an integer representing the number of test cases, and it is guaranteed that 1 <= testcases <= 10^4.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: testcases is 0.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It executes a number of test cases determined by the value returned from `func_3`, and for each test case, it calls `func_6`. The function does not return any value.

