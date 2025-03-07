#State of the program right berfore the function call: func is a callable object representing a function that will be modified to include additional functionality.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a wrapper function.
#Overall this is what the function does:The function `func_1` accepts a callable object `func` and returns a wrapper function. This wrapper function encapsulates the original function `func`, potentially adding new functionality around it without altering the original function's code.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `t` is an integer such that 1 <= t <= 10^4. If `args` is not found in list `d`, then `d[args]` is assigned the result of `func(*args)`.
    return d[args]
    #The program returns the result of `func(*args)` stored in `d[args]` if `args` is found in dictionary `d`. If `args` is not found in `d`, it returns None.
#Overall this is what the function does:The function `wrapper()` checks if the `args` are present in the dictionary `d`. If `args` are found in `d`, it returns the corresponding value. If `args` are not found, it returns `None`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it as a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns it as a string. This action is performed without requiring any input parameters.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers sorted in ascending order such that 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers such that 1 <= d_i <= 10^9. f is a list of k integers such that 1 <= f_i <= 10^9.
def func_3():
    return int(func_2())
    #The program returns an integer value obtained from the function `func_2()` which is not further specified in the given code snippet.
#Overall this is what the function does:The function calls another function `func_2()` and returns an integer value obtained from its execution. This integer value is derived from processing input data including an integer `t`, and lists `a`, `d`, and `f` with specific constraints.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers converted from a string split by a delimiter, where the string is the result of calling `func_2()` and splitting its output.
#Overall this is what the function does:The function accepts a delimiter parameter and returns a list of integers. This list is obtained by converting a string, which is the result of calling `func_2()` and splitting it using the provided delimiter, into a list of integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2⋅10^5. a is a list of n integers where 1 ≤ a_i ≤ 2⋅10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def func_5():
    return func_2()
    #The program returns the result of calling the function `func_2()` with the current state of variables `t`, `n`, `m`, `k`, `a`, `d`, and `f` as arguments.
#Overall this is what the function does:The function does not accept any direct parameters. Instead, it calls another function `func_2()` using the current values of the variables `t`, `n`, `m`, `k`, `a`, `d`, and `f`. The function returns the result of this call.

#State of the program right berfore the function call: (n, m, k) are positive integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 × 10^5; A is a list of n strictly increasing integers representing the complexities of the prepared problems; D is a sorted list of unique integers representing the complexities of the models; F is a list of k integers representing the complexities of the functions; the values of A, D, and F are within specified ranges as described in the problem statement.
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
        
    #State: Output State: After the loop executes all its iterations, `max_diff` will hold the maximum difference between consecutive elements in the list `A`, `next_max_diff` will hold the second maximum difference between consecutive elements in the list `A` (or remain `-inf` if no such difference exists), `index` will hold the index where `max_diff` was found (or remain `None` if `max_diff` did not change), and `diff`, `i`, `n`, `m`, `k`, `D`, and `F` will retain their values after the last iteration of the loop. The values of `A`, `n`, `m`, `k`, `D`, and `F` will be the same as they were initially, as they are not modified within the loop.
    #
    #In simpler terms, after the loop finishes, `max_diff` will be the largest gap between any two consecutive numbers in the list `A`, `next_max_diff` will be the second largest gap (if there is one), `index` will point to the position in `A` where `max_diff` was found, and the other variables will keep their values from the last iteration of the loop.
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
        
    #State: Output State: After the loop executes all iterations, `l` and `h` will define the boundaries of the search range where the optimal solution is found, `ans` will contain the best result obtained across all iterations, `f` will be the last element in `F` processed by the loop, `mid_sum` and `mid_next_sum` will reflect the sums `D[mid] + f` and `D[mid + 1] + f` for the last valid midpoint `mid`, and `left` and `right` will retain their values from the final iteration. `ans` will be updated to the minimum value between its current value and `max(D[l] + f - left, right - D[l] - f)` after processing the last element in `F`.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff)
#Overall this is what the function does:The function processes three lists \(A\), \(D\), and \(F\) to find the maximum difference between consecutive elements in \(A\) and then determines the best possible value by searching through \(F\) and comparing it with elements in \(D\). Specifically, it calculates the maximum gap between consecutive elements in \(A\), finds the closest pairs in \(D\) that can match the gaps adjusted by elements in \(F\), and outputs the maximum of this calculated gap and the second largest gap in \(A\).

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each testcase, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. The list a is a sorted list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. The list d is a list of m integers where 1 <= d_i <= 10^9. The list f is a list of k integers where 1 <= f_i <= 10^9.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: Output State: `testcases` must be greater than or equal to 3.
    #
    #In natural language: After the loop has executed all its iterations, the value of `testcases` must be at least 3. This is because the loop runs as long as `testcases` is greater than 0, and we know it ran at least 3 times, so `testcases` had to start at a value of 3 or higher.
#Overall this is what the function does:The function processes multiple test cases, each involving three lists: a (a sorted list of integers), d, and f. It ensures that the variable `testcases` is at least 3 after processing all test cases. The function does not return any value directly but modifies the input lists according to unspecified operations within the loop.

