#State of the program right berfore the function call: func is a function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns `wrapper`
#Overall this is what the function does:The function `func_1` accepts a parameter `func`, which is a function, and returns `wrapper`.

#State of the program right berfore the function call: args is a tuple containing any values that the function `func` can accept as arguments.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple containing any values that the function `func` can accept as arguments. If `args` was not in the dictionary `d`, a new key-value pair is added to `d` where the key is `args` and the value is `func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the value associated with the key `args` in the dictionary `d`. If `args` was not in `d` before the function was called, it has now been added with the value `func(*args)`.
#Overall this is what the function does:The function accepts a tuple `args` containing any values. It returns the value associated with the key `args` in the dictionary `d`. If `args` was not in `d` before the function was called, it computes `func(*args)`, adds `args` to `d` with this value, and then returns this value.

#State of the program right berfore the function call: This function does not have any parameters and does not contribute directly to solving the problem based on the provided code snippet. It appears to be a utility function intended to read a line from standard input and strip any leading or trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is a line read from standard input, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_2` reads a line from standard input and returns it as a string with any leading or trailing whitespace removed.

#State of the program right berfore the function call: No variables are present in the function signature of `func_3`. Therefore, the precondition is that there are no specific variable constraints or relationships to describe.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of `func_2()`
#Overall this is what the function does:The function `func_3` accepts no parameters and returns an integer value that is the result of `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers derived from splitting the string returned by `func_2()` using the `delimiter`.
#Overall this is what the function does:The function takes a string `delimiter` as input and returns a list of integers. This list is obtained by splitting the string returned by `func_2()` using the specified `delimiter` and converting each split segment into an integer.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_5():
    return func_2()
    #The program returns the value returned by the function `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the value returned by the function `func_2()`.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. D is a list of m integers where 1 <= d_i <= 10^9. F is a list of k integers where 1 <= f_i <= 10^9.
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
        
    #State: - After the loop, `max_diff` will hold the largest difference between consecutive elements in `A`.
    #   - `next_max_diff` will hold the second largest difference between consecutive elements in `A`.
    #   - `index` will hold the index `i` where the largest difference `max_diff` occurs.
    #   - `A`, `D`, and `F` remain unchanged as they are not modified within the loop.
    #
    #Thus, the output state can be described as:
    #
    #Output State:
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
        
    #State: ans is the minimum of its initial value and the calculated differences for each f in F.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum of its initial value and the calculated differences for each f in F, and next_max_diff is another value being compared)
#Overall this is what the function does:The function calculates and prints the maximum of two values: the largest difference between consecutive elements in a sorted list `A`, and a computed minimum difference based on elements from lists `D` and `F`. The computed minimum difference is determined by finding the optimal element in `D` for each element in `F` to minimize the maximum of two specific differences.

#State of the program right berfore the function call: testcases is an integer representing the number of test cases, and it satisfies 1 <= testcases <= 10^4.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` remains the integer value returned by `func_3()`, and it satisfies 1 <= `testcases` <= 10^4.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It performs a series of operations based on the number of test cases, which is determined by the value returned from `func_3()`. The function iterates through each test case by calling `func_6()` for each one. After completing the iterations, the function does not return any specific value or modify the input parameters.

