#State of the program right berfore the function call: func is a function that takes some arguments and returns a wrapper function, but the specific arguments and the purpose of the wrapper function are not specified in the given code snippet.
def func_1(func):
    d = {}
    return wrapper
    #The program returns the wrapper function.
#Overall this is what the function does:The function `func_1` accepts a function `func` as a parameter and returns a wrapper function.

#State of the program right berfore the function call: args is a tuple containing the arguments passed to the function func.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple containing the arguments passed to the function `func`. If `args` was not originally a key in `d`, `d` now contains the key `args` with the value `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the value associated with the key `args` in the dictionary `d`. If `args` was not originally a key in `d`, it now contains the key `args` with the value `func(*args)`. Otherwise, it returns the pre-existing value associated with `args`.
#Overall this is what the function does:The function accepts a tuple `args` containing the arguments passed to the function `func`. It returns the value associated with the key `args` in the dictionary `d`. If `args` is not already a key in `d`, it computes `func(*args)`, stores the result in `d` with `args` as the key, and then returns this newly computed value. If `args` is already a key in `d`, it simply returns the pre-existing value associated with `args`.

#State of the program right berfore the function call: No specific variables are present in the function signature of `func_2()`. This function is assumed to read a line from standard input and strip any leading/trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that represents the line read from standard input with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_2` reads a line from standard input, removes any leading or trailing whitespace from the line, and returns the resulting string.

#State of the program right berfore the function call: This function does not have any parameters, so there are no variables or relationships to describe.
def func_3():
    return int(func_2())
    #The program returns the integer value returned by `func_2()`
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns the integer value returned by `func_2()`.

#State of the program right berfore the function call: delimiter is a string that specifies the delimiter used to split the input string into parts, which are then converted to integers and returned as a list.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers derived from the string returned by `func_2()`, split by the `delimiter`.
#Overall this is what the function does:The function accepts a string `delimiter` and returns a list of integers. This list is derived by splitting the string returned by `func_2()` using the `delimiter` and converting each split part into an integer.

#State of the program right berfore the function call: This function does not have any parameters, and thus there are no variables or relationships to describe in the precondition.
def func_5():
    return func_2()
    #The program returns the result of `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of `func_2()`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, m and k are integers such that 1 <= m, k <= 2 * 10^5, A is a list of n integers where 1 <= A[i] <= 2 * 10^9 and A is sorted in strictly ascending order, D is a sorted list of unique integers where 1 <= D[i] <= 10^9, and F is a list of k integers where 1 <= F[i] <= 10^9.
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
        
    #State: `max_diff` is the maximum difference between consecutive elements in `A`; `next_max_diff` is the second maximum difference between consecutive elements in `A`; `index` is the index where `max_diff` occurs; `n`, `m`, `k`, `A`, `D`, and `F` remain unchanged.
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
        
    #State: `max_diff` is the maximum difference between consecutive elements in `A`; `next_max_diff` is the second maximum difference between consecutive elements in `A`; `index` is the index where `max_diff` occurs; `n`, `m`, `k`, `A`, `D`, and `F` remain unchanged; `left` is `A[index - 1]`; `right` is `A[index]`; `ans` is the minimum value of `max(D[l] + f - left, right - D[l] - f)` for all `f` in `F`.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum value of max(D[l] + f - left, right - D[l] - f) for all f in F, and next_max_diff is the second maximum difference between consecutive elements in A)
#Overall this is what the function does:The function takes integers `n`, `m`, `k`, a strictly ascending sorted list `A` of `n` integers, a sorted list `D` of `m` unique integers, and a list `F` of `k` integers. It calculates the maximum difference between consecutive elements in `A` and the second maximum difference. For each value in `F`, it finds the optimal position in `D` to minimize a specific expression involving the elements of `A` and `D`, adjusted by the value from `F`. Finally, it prints the maximum value between the second maximum difference and the minimum value of the calculated expression for all values in `F`.

#State of the program right berfore the function call: No variables are provided in the function signature of `func_7`, thus no specific precondition can be derived from the given signature alone.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: testcases is 0.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It calls `func_3` to determine the number of test cases and then iterates that many times, calling `func_6` in each iteration. The function does not return any value explicitly, and after execution, the state of `testcases` is 0.

