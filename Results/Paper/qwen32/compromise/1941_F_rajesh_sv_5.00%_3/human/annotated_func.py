#State of the program right berfore the function call: func is a function, but the relationship and the values it should handle are not specified in the given function signature.
def func_1(func):
    d = {}
    return wrapper
    #The program returns the variable `wrapper`
#Overall this is what the function does:The function `func_1` accepts a parameter `func`, which is expected to be a function, and returns a variable `wrapper`.

#State of the program right berfore the function call: args is a tuple of arguments that the function `func` can accept. The values in `args` are used as keys in the dictionary `d`, and `func` is a function that computes a value based on these arguments.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple of arguments that the function `func` can accept. If `args` was not in the dictionary `d`, `d` now includes a new key-value pair where the key is `args` and the value is `func(*args)`. If `args` was already in `d`, `d` remains unchanged.
    return d[args]
    #The program returns the value associated with the key `args` in the dictionary `d`. If `args` was not in `d` before the function call, it has been added with the value `func(*args)`. If `args` was already in `d`, the existing value is returned.
#Overall this is what the function does:The function `wrapper` takes a tuple of arguments `args` and a function `func`. It checks if `args` is a key in the dictionary `d`. If not, it computes a value using `func(*args)`, stores this value in `d` with `args` as the key, and returns this value. If `args` is already in `d`, it returns the existing value associated with `args`.

#State of the program right berfore the function call: No variables are present in the function signature, thus no specific precondition can be derived from it.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is the next line of input from the standard input (stdin) with any leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_2` reads a line from the standard input, removes any leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature, so there are no preconditions to describe.
def func_3():
    return int(func_2())
    #The program returns the integer value returned by the function `func_2()`
#Overall this is what the function does:The function `func_3` accepts no parameters and returns the integer value returned by the function `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` string and converting each split substring to an integer.
#Overall this is what the function does:The function accepts a `delimiter` string, splits the string returned by `func_2()` using this `delimiter`, converts each split substring to an integer, and returns a list of these integers.

#State of the program right berfore the function call: This function does not have any parameters or variables in its signature, so no precondition can be derived from it.
def func_5():
    return func_2()
    #The program returns the result of the function `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of the function `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m <= 2 * 10^5, and 1 <= k <= 2 * 10^5. A is a list of integers of length n where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. D is a sorted list of unique integers of length m where 1 <= d_i <= 10^9. F is a list of integers of length k where 1 <= f_i <= 10^9.
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
        
    #State: `max_diff` is the largest difference between consecutive elements in `A`, `next_max_diff` is the second largest difference between consecutive elements in `A`, and `index` is the index of the larger element in the pair that gives the largest difference. `n`, `m`, `k`, `A`, `D`, `F` remain unchanged from their initial values.
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
        
    #State: max_diff is 2, next_max_diff is the second largest difference between consecutive elements in A, index is the index of the larger element in the pair that gives the largest difference, A is [1, 3, 5, 7], D is [1, 3, 5, 7], F remains unchanged, left is 1, right is 3, ans is 2.
    print(max(ans, next_max_diff))
    #This is printed: 2
#Overall this is what the function does:The function calculates and prints the maximum of two values: the largest difference between consecutive elements in a sorted list `A`, and a computed value `ans` that is derived from the elements of `A`, `D`, and `F`. The function does not modify the input lists `A`, `D`, or `F`, and it does not return any value; instead, it prints the result.

#State of the program right berfore the function call: testcases is an integer representing the number of test cases, where 1 <= testcases <= 10^4.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is 0 and `func_6()` has been executed `testcases` times.
#Overall this is what the function does:The function `func_7` executes `func_6` a number of times equal to the value returned by `func_3`. The number of executions is between 1 and 10,000, inclusive. The function itself does not accept any parameters and does not return a specific value.

