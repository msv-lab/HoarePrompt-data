#State of the program right berfore the function call: func is a callable object or function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a wrapper function.
#Overall this is what the function does:The function `func_1` accepts a callable object or function as its parameter and returns a wrapper function.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. a is a list of n integers such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. d is a list of m integers such that 1 ≤ d_i ≤ 10^9. f is a list of k integers such that 1 ≤ f_i ≤ 10^9.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n`, `m`, and `k` are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5, `a` is a list of n integers such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}, `d` is a list of m integers such that 1 ≤ d_i ≤ 10^9, `f` is a list of k integers such that 1 ≤ f_i ≤ 10^9, if `args` is not in `d`, then `d[args]` is assigned the value of `func(*args)`.
    return d[args]
    #The program returns the value of `d[args]` which is assigned the value of `func(*args)` if `args` is not in `d`.
#Overall this is what the function does:The function retrieves or computes a value based on the arguments provided through a dictionary `d`. If the arguments `args` are not found in `d`, it calculates the result using `func(*args)` and stores it in `d` before returning it. If the arguments `args` are already present in `d`, it simply returns the stored value.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_3():
    return int(func_2())
    #The program returns an integer value obtained from the function func_2(), which is not defined in the given code snippet. The exact value cannot be determined without knowing the implementation of func_2().
#Overall this is what the function does:The function accepts no parameters and returns an integer value obtained from another undefined function `func_2()`. The final state of the program is that it returns this integer value.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the output of func_2() using the specified delimiter and converting each resulting string to an integer.
#Overall this is what the function does:The function accepts a delimiter parameter and returns a list of integers. It achieves this by first calling another function `func_2()` which presumably returns a string. This string is then split using the provided delimiter, and each resulting substring is converted to an integer. The function does not modify any external variables and solely focuses on processing the output of `func_2()` to produce the final list of integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. The list a is a sorted list of n integers such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. The list d is a list of m integers such that 1 ≤ d_i ≤ 10^9. The list f is a list of k integers such that 1 ≤ f_i ≤ 10^9.
def func_5():
    return func_2()
    #The program returns the result of calling the function `func_2()` with all the given parameters and their respective values as described in the initial state.
#Overall this is what the function does:The function calls another function `func_2()` with predefined parameters `t`, `n`, `m`, `k`, `a`, `d`, and `f` and returns the result of this call.

#State of the program right berfore the function call: (n, m, k) are positive integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5; A is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}; D is a sorted list of unique integers obtained from m integers where 1 <= d_i <= 10^9; F is a list of k integers where 1 <= f_i <= 10^9.
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
        
    #State: Output State: `max_diff` is the maximum difference found across all elements in the array `A`, `next_max_diff` is the second largest difference found or remains unchanged, `index` is the index where `max_diff` occurs or remains `None`, `i` is `n-1`, and `diff` is `A[n-1] - A[n-2]`.
    #
    #In this final output state, `max_diff` will hold the greatest difference between any two consecutive elements in the array `A`, `next_max_diff` will hold the second greatest difference (or remain unchanged if no such difference was found), `index` will hold the index where `max_diff` occurs (or remain `None` if `max_diff` is `-inf`), and `i` will be the last index `n-1` that the loop processed. The variable `diff` will be the difference between the last two elements of the array `A`.
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
        
    #State: `ans` is the minimum value among all updates made during the loop execution, `mid_sum` is `D[l] + f`, `mid_next_sum` is `D[l + 1] + f`, and `l` (which is equal to `h`) is the final index where the optimal solution was determined.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum value among all updates made during the loop execution, and next_max_diff is undefined)
#Overall this is what the function does:The function processes three lists: `A`, `D`, and `F`. It first finds the maximum difference (`max_diff`) and the second maximum difference (`next_max_diff`) between consecutive elements in `A`. Then, it iterates through each element in `F`, using binary search to find pairs of elements in `D` that minimize a certain condition. Finally, it returns the maximum value between `ans` (the minimum value found during the iteration) and `next_max_diff`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. The list a is a sorted list of n integers such that 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. The list d is a list of m integers such that 1 <= d_i <= 10^9. The list f is a list of k integers such that 1 <= f_i <= 10^9.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: Output State: `testcases` must be greater than or equal to 3 and `func_6()` has been called 3 times.
    #
    #This means that after the loop has executed all its iterations, `testcases` should have a value of at least 3 (since it must have been greater than 2 after 3 iterations), and `func_6()` would have been called exactly 3 times as specified in the loop.
#Overall this is what the function does:The function processes multiple test cases, with each test case involving three lists: a (a sorted list of integers), d, and f. It calls `func_6()` exactly three times, regardless of the number of test cases. The function does not return any value but modifies the behavior of `func_6()` by ensuring it is called at least three times across all test cases.

