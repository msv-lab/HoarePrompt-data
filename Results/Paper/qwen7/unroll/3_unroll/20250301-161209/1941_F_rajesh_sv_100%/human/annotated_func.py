#State of the program right berfore the function call: func is a function object.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a function object named wrapper.
#Overall this is what the function does:The function `func_1` accepts another function object as a parameter and returns a new function object named `wrapper`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `d[args]` is set to the result of `func(*args)`, `t` is an integer such that 1 <= t <= 10^4, `n`, `m`, and `k` are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5, `a` is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}, `d` is a list of m integers where 1 <= d_i <= 10^9, `f` is a list of k integers where 1 <= f_i <= 10^9, and the arguments passed to the function are not in the list `d`.
    return d[args]
    #The program returns the result of the function call `func(*args)` which is stored in `d[args]`
#Overall this is what the function does:The function accepts a tuple of arguments `args` containing `t`, `n`, `m`, `k`, `a`, `d`, and `f`. If the arguments are not already in the dictionary `d`, it calls the function `func` with these arguments and stores the result in `d[args]`. If the arguments are already in `d`, it simply returns the stored result. The function returns the result of `func(*args)` which is either newly computed or retrieved from `d`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_3():
    return int(func_2())
    #The program returns an integer value obtained from the function func_2() for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by specific constraints involving integers n, m, k, lists a, d, and f. For each test case, it calls another function `func_2()` to compute an integer value, which it then returns.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers converted from a string split by a delimiter, where the string is obtained from the result of func_2()
#Overall this is what the function does:The function accepts a delimiter parameter and returns a list of integers. This list is obtained by splitting a string, which is the result of calling another function `func_2()`, using the provided delimiter.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. The list a is a sorted list of n integers such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. The list d is a list of m integers such that 1 ≤ d_i ≤ 10^9. The list f is a list of k integers such that 1 ≤ f_i ≤ 10^9.
def func_5():
    return func_2()
    #The program returns the result of calling the function `func_2()` with the given parameters.
#Overall this is what the function does:The function calls another function `func_2()` with specific parameters including an integer `t`, an integer `n`, an integer `m`, an integer `k`, a sorted list `a` of integers, and two other lists `d` and `f`. It then returns the result of this call.

#State of the program right berfore the function call: (n, m, k) are positive integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 × 10^5; A is a list of n strictly increasing integers representing the complexities of the prepared problems; D is a list of unique integers representing the complexities of the models after sorting; F is a list of k positive integers representing the complexities of the functions.
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
        
    #State: Output State: `max_diff` is the largest difference found between consecutive elements in the array `A`, `next_max_diff` is the second largest difference found, and `index` is the index of the element where `max_diff` was found.
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
        
    #State: `max_diff` is the largest difference found between consecutive elements in the array `A`, `next_max_diff` is the second largest difference found, `index` is the index of the element where `max_diff` was found, `left` is `A[index - 1]`, `right` is `A[index]`, `ans` is the minimum value among all `max(D[l] + f - left, right - D[l] - f)` for each `f` in `F`.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff)
#Overall this is what the function does:The function accepts three lists: A (problem complexities), D (sorted model complexities), and F (function complexities). It finds the largest difference (`max_diff`) and the second largest difference (`next_max_diff`) between consecutive elements in A. Then, for each complexity in F, it uses binary search to find the closest model complexity in D that can balance the differences. Finally, it prints the maximum value between `max_diff` and `next_max_diff`, or the minimum imbalance found during the search process.

#State of the program right berfore the function call: testcases is an integer such that 1 <= testcases <= 10^4. For each testcase, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: The return value of func_3() repeated func_6() for each iteration in the range specified by the return value of func_3().
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( n \), \( m \), and \( k \), along with lists \( a \), \( d \), and \( f \). For each test case, it calls another function `func_6()` which performs some unspecified operations. The function does not return any value but processes the input data as described.

