#State of the program right berfore the function call: func is a function object representing one of the functions with complexity f_j.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a wrapper function.
#Overall this is what the function does:The function `func_1` accepts a function object as its parameter and returns a wrapper function.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `t` is an integer such that 1 <= t <= 10^4. For each test case, `n`, `m`, and `k` are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. `a` is a list of `n` integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. `d` is a list of `m` integers where 1 <= d_i <= 10^9. `f` is a list of `k` integers where 1 <= f_i <= 10^9. If `args` are not in `d`, then `d[args]` is set to the result of `func(*args)`, where `args` are the elements passed to the function call. The values of `n`, `m`, `k`, `a`, `d`, and `f` remain unchanged.
    return d[args]
    #The program returns the value of `d[args]` where `args` are the elements passed to the function call, and if `args` are not already present in `d`, then `d[args]` is set to the result of `func(*args)`
#Overall this is what the function does:The function retrieves the value of `d[args]` where `args` are the elements passed to the function call. If `args` are not already present in `d`, it calculates `func(*args)` and stores the result in `d[args]` before returning it.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers sorted in ascending order such that 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers such that 1 <= d_i <= 10^9. f is a list of k integers such that 1 <= f_i <= 10^9.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it as a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns it as a string. This operation does not depend on any external parameters and can be performed multiple times independently.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. The list a is a sorted list of n integers such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. The list d is a list of m integers such that 1 ≤ d_i ≤ 10^9. The list f is a list of k integers such that 1 ≤ f_i ≤ 10^9.
def func_3():
    return int(func_2())
    #The program returns an integer value calculated by the function func_2(), which is not defined in the given code snippet.
#Overall this is what the function does:The function accepts no parameters and returns an integer value calculated by the function `func_2()`. This integer value is derived from processing inputs such as a sorted list of integers `a`, another list of integers `d`, and a third list of integers `f`, along with additional integers `n`, `m`, and `k` that define the sizes and ranges of these lists.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers sorted in ascending order such that 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers such that 1 <= d_i <= 10^9. f is a list of k integers such that 1 <= f_i <= 10^9.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` and converting each element to an integer.
#Overall this is what the function does:The function accepts a delimiter parameter and returns a list of integers. It achieves this by first calling another function `func_2()` to get a string, then splitting this string using the provided delimiter, and finally converting each element of the resulting list to an integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2⋅10^5. a is a list of n integers where 1 ≤ a_i ≤ 2⋅10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def func_5():
    return func_2()
    #The program returns the result of calling the function `func_2()` with the given parameters.
#Overall this is what the function does:The function indirectly calls `func_2()` with parameters including an integer `t` (1 ≤ t ≤ 10^4), a list `a` of sorted integers (1 ≤ a_i ≤ 2⋅10^9), and two other lists `d` and `f` (both 1 ≤ d_i, f_i ≤ 10^9). It returns whatever `func_2()` returns.

#State of the program right berfore the function call: (n, m, k) are positive integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 × 10^5. A is a list of n strictly increasing integers representing the complexities of the prepared problems, D is a list of unique integers representing the complexities of the models after sorting, and F is a list of k integers representing the complexities of the functions.
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
        
    #State: Output State: `max_diff` is the maximum difference found between consecutive elements in the array `A` from index 1 to `n-1`, `next_max_diff` is the second maximum difference found under the same conditions, `index` is the index where `max_diff` was found, and `i` is `n`. `diff` is the last calculated difference which is `A[n-1] - A[n-2]`.
    #
    #In simpler terms, after the loop has executed all its iterations, `max_diff` will hold the largest difference between any two consecutive elements in the array `A` starting from the second element, `next_max_diff` will hold the second largest such difference, `index` will point to the index where `max_diff` was found (if there were any differences), and `i` will be equal to `n` (the total number of elements in the array). The variable `diff` will contain the difference between the last two elements of the array `A`.
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
        
    #State: `ans` holds the minimum value among all the updates made during the loop execution, `mid` is the final midpoint where the loop exits, `l` and `h` are equal to each other (representing the final boundaries of the search range), `mid_sum` is `D[mid] + f`, `mid_next_sum` is `D[mid + 1] + f`, and `f` is the last value from the sequence `F` used in the comparisons.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff)
#Overall this is what the function does:The function processes three lists: A, D, and F. It first finds the maximum difference (`max_diff`) and the second maximum difference (`next_max_diff`) between consecutive elements in list A. Then, for each element in list F, it uses binary search to find pairs of elements in list D that, when adjusted by the current element from F, form a valid pair within certain constraints. Finally, it prints the maximum value among `max_diff`, `next_max_diff`, and the minimum adjustments found during the search process.

#State of the program right berfore the function call: testcases is an integer such that 1 <= testcases <= 10^4. For each testcase, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: Output State: `testcases` must be greater than 2.
    #
    #In natural language: After the loop has executed all its iterations, `testcases` must be greater than 2. This is because the loop continues to execute as long as `testcases` is greater than 0, and it specifically mentions that after 3 iterations, `testcases` must be greater than 1. Therefore, for the loop to complete all its iterations, `testcases` must initially be greater than 2.
#Overall this is what the function does:The function processes multiple test cases, each involving four lists (a, d, f) and three integers (n, m, k). It ensures that the variable `testcases` is greater than 2 after completing all iterations of the loop. The function does not return any value but modifies the state of predefined lists and integers based on the specified conditions.

