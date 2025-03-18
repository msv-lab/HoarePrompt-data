#State of the program right berfore the function call: func is a callable object or function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a wrapper function
#Overall this is what the function does:The function `func_1` accepts a callable object or function as its parameter and returns a wrapper function.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `t` is an integer such that 1 <= t <= 10^4, `n`, `m`, and `k` are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5, `a` is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}, `d` is a list of m integers where 1 <= d_i <= 10^9, `f` is a list of k integers where 1 <= f_i <= 10^9. If `args` is not in `d`, then `d[args]` is assigned the result of `func(*args)`.
    return d[args]
    #The program returns the value of `d[args]`, which is the result of `func(*args)` if `args` is not found in list `d`.
#Overall this is what the function does:The function retrieves a value from the dictionary `d` using `args` as the key. If `args` is not found in `d`, it computes the result of calling `func(*args)` and stores it in `d` before returning it. If `args` is already present in `d`, it simply returns the stored value.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. a is a list of n integers where 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def func_3():
    return int(func_2())
    #The program returns an integer value obtained from the function `func_2()` for each test case.
#Overall this is what the function does:The function processes multiple lists and integers (t, n, m, k, a, d, f) and returns an integer value obtained from calling another function `func_2()`. This integer value is returned for each test case defined by the input parameters.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers converted from a string split by a delimiter, where the string is the result of calling `func_2()` and then splitting the result.
#Overall this is what the function does:The function accepts a delimiter (string) and returns a list of integers. It achieves this by first calling another function `func_2()`, obtaining its output as a string, splitting this string using the provided delimiter, and then converting the resulting substrings into integers.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. The list a is a sorted list of n integers such that 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. The list d is a list of m integers such that 1 <= d_i <= 10^9. The list f is a list of k integers such that 1 <= f_i <= 10^9.
def func_5():
    return func_2()
    #The program returns the result of calling the function `func_2()` with the given parameters.
#Overall this is what the function does:The function calls another function `func_2()` with specified parameters including an integer `t`, an integer `n`, an integer `m`, an integer `k`, a sorted list `a` of integers, and two other lists `d` and `f`. It then returns the result of this call. The parameters `t`, `n`, `m`, and `k` are bounded within certain ranges, and the lists `a`, `d`, and `f` have specific constraints on their contents and lengths.

#State of the program right berfore the function call: (n, m, k) are positive integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 * 10^5. A is a list of n integers representing the complexities of the prepared problems, where 1 ≤ a_i ≤ 2 * 10^9 and a_i < a_{i+1}. D is a list of unique integers representing the complexities of the models, sorted in ascending order, where 1 ≤ d_i ≤ 10^9. F is a list of k integers representing the complexities of the functions, where 1 ≤ f_i ≤ 10^9.
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
        
    #State: max_diff is the maximum difference found in the entire array A, next_max_diff is the second largest difference or -inf if no such difference exists, index is the index where max_diff occurred or None if no valid index was found, i is n, and diff is A[n-2] - A[n-3].
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
        
    #State: After the loop executes all iterations, `ans` will hold the minimum value between its current value and the maximum of `D[l] + f - left` and `right - D[l] - f`. The variable `l` will be equal to `h`, which represents the index in list `D` where the condition `D[l] + f < left` holds true and `D[h] + f >= right` starts to hold true. Variables `mid`, `mid_sum`, and `mid_next_sum` will retain their values from the last iteration of the loop, as they are only used within the while loop and are not reassigned outside of it. The other variables (`f`, `D`, `left`, `right`, `i`, `diff`, `index`, `max_diff`, `next_max_diff`) will remain unchanged from their final values after the first three iterations.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff)
#Overall this is what the function does:The function processes three positive integers \( n \), \( m \), and \( k \), along with two lists \( A \) and \( F \). It calculates the maximum difference (\( \text{max\_diff} \)) between consecutive elements in \( A \) and finds the index where this maximum difference occurs. It then searches through the list \( D \) using binary search to find the optimal value of \( f \) from \( F \) that minimizes the maximum absolute difference between elements in \( A \) and elements in \( D \) adjusted by \( f \). Finally, it prints the maximum of \( \text{max\_diff} \) and the second largest difference (\( \text{next\_max\_diff} \)).

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each testcase, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: Output State: `func_6()` has been called 10^4 times.
    #
    #Explanation: The loop runs `testcases` times, which is the result of `func_3()`. Since the output state after 3 iterations already indicates that `func_6()` has been called, we can infer that `func_6()` will be called once per iteration of the loop. Therefore, after all iterations (which is `10^4` times), `func_6()` will have been called `10^4` times.
#Overall this is what the function does:The function processes a series of test cases, each involving lists of integers. It calls `func_6()` exactly 10,000 times, regardless of the input values. The function does not return any value directly but modifies internal states through the calls to `func_6()`.

