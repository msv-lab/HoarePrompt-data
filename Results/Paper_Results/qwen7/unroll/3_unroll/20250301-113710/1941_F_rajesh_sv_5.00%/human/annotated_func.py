#State of the program right berfore the function call: func is a callable object representing the complexity of a function, where 1 ≤ func ≤ 10^9.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a wrapper function, which is not defined in the given code snippet but is implied to be a callable object. The value of `func` remains unchanged as it is not modified in the code.
#Overall this is what the function does:The function `func_1` accepts a callable object `func` representing the complexity of another function and returns a wrapper function without altering the value of `func`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `t` is an integer such that 1 <= t <= 10^4, `n`, `m`, and `k` are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5, `a` is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}, `d` is a list of m integers where 1 <= d_i <= 10^9, `f` is a list of k integers where 1 <= f_i <= 10^9, and if `args` is not in `d`, the value of `d[args]` is set to the result of calling function `func` with arguments from the `args` tuple.
    return d[args]
    #The program returns the value of `d[args]`, which is the result of calling function `func` with arguments from the `args` tuple if `args` is not already present in `d`.
#Overall this is what the function does:The function retrieves or computes a value based on the input arguments. If the input arguments (`args`) are not already stored in the dictionary `d`, it calls another function `func` with these arguments and stores the result in `d`. The function then returns the value from `d` corresponding to the input arguments.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. a is a list of n integers where 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it as a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns it as a string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. a is a list of n integers sorted in ascending order such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. d is a list of m integers such that 1 ≤ d_i ≤ 10^9. f is a list of k integers such that 1 ≤ f_i ≤ 10^9.
def func_3():
    return int(func_2())
    #The program returns an integer value obtained from the function func_2(), which is not specified in the given code snippet. The value returned by func_2() could be any integer based on its implementation.
#Overall this is what the function does:The function does not accept any parameters and returns an integer value obtained from another unspecified function `func_2()`. The integer returned can be any value depending on the implementation of `func_2()`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by converting each element in the list returned by `func_2().split(delimiter)` into an integer.
#Overall this is what the function does:The function accepts a delimiter parameter and returns a list of integers. It achieves this by splitting a string obtained from `func_2()` using the provided delimiter, then converting each resulting substring into an integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. The list a is a sorted list of n integers such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. The list d is a list of m integers such that 1 ≤ d_i ≤ 10^9. The list f is a list of k integers such that 1 ≤ f_i ≤ 10^9.
def func_5():
    return func_2()
    #The program returns the result of calling the function `func_2()` with all the given parameters and lists intact.
#Overall this is what the function does:The function calls another function `func_2()` with the parameters `t`, `n`, `m`, `k`, and the lists `a`, `d`, and `f` intact and returns the result of this call.

#State of the program right berfore the function call: n, m, and k are positive integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 * 10^5; A is a list of n strictly increasing integers representing the complexities of the prepared problems; D is a sorted list of unique integers representing the complexities of the models; F is a list of k positive integers representing the complexities of the functions; the values of n, m, and k, as well as the lists A, D, and F, are provided within the constraints specified in the problem description.
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
        
    #State: Output State: `max_diff` is the largest difference between consecutive elements in the list `A` starting from index 1 to `n-1`, `next_max_diff` is the second largest difference between consecutive elements under the same condition, `index` is the index of the element where `max_diff` occurs, and the states of `D`, `n`, `m`, `k`, and `F` remain unchanged.
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
        
    #State: Output State: `max_diff` is the largest difference between consecutive elements in the list `A` starting from index 1 to `n-1`, `next_max_diff` is the second largest difference between consecutive elements under the same condition, `index` remains the index of the element where `max_diff` occurs, `left` is `A[index - 1]`, `right` is `A[index]`, `ans` is updated to the minimum value of `max(D[l] + f - left, right - D[l] - f)` for each `f` in `F` where `l` is found using binary search, and the states of `D`, `n`, `m`, `k`, and `F` remain unchanged.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff)
#Overall this is what the function does:The function calculates and prints the maximum value among the largest difference (`max_diff`) between consecutive elements in the list `A` and the minimum value of `max(D[l] + f - left, right - D[l] - f)` for each `f` in `F` where `l` is determined using binary search. The function does not return any value but prints the result.

#State of the program right berfore the function call: testcases is an integer such that 1 <= testcases <= 10^4. For each testcase, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: The return value of func_3() repeated func_6() for each iteration specified by the return value of func_3().
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes four integers (n, m, k), a list of n integers (a), a list of m integers (d), and a list of k integers (f). It then calls `func_6()` for each test case, passing the relevant parameters. After processing all test cases, it does not return any value.

