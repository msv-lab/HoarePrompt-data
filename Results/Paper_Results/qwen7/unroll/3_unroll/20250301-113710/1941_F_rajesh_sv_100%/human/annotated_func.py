#State of the program right berfore the function call: func is a function object.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a function object named wrapper
#Overall this is what the function does:The function `func_1` accepts another function object as a parameter and returns a new function object named `wrapper`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2⋅10^5. a is a list of n integers where 1 ≤ a_i ≤ 2⋅10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `d[args]` is assigned the result of `func(*args)`, `n`, `m`, and `k` are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2⋅10^5, `a` is a list of n integers where 1 ≤ a_i ≤ 2⋅10^9 and a_i < a_{i+1}, `d` is a list of m integers where 1 ≤ d_i ≤ 10^9, `f` is a list of k integers where 1 ≤ f_i ≤ 10^9. If the arguments passed to `func` are not present in the list `d`, `d[args]` is updated with the result of `func(*args)`. If the arguments are already present in `d`, no change is made to `d`.
    return d[args]
    #The program returns the result of `func(*args)` which is stored in `d[args]`, given that `args` are not already present in `d` as a key. If `args` are already a key in `d`, the value remains unchanged.
#Overall this is what the function does:The function accepts a dictionary `d` and variable arguments `*args`. It checks whether `args` are already a key in `d`. If `args` are not in `d`, it calls a function `func` with `*args` and stores the result in `d[args]`. If `args` are already a key in `d`, it returns the existing value associated with `args` without making any changes to the dictionary.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. a is a list of n integers where 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def func_3():
    return int(func_2())
    #The program returns an integer value obtained from the function func_2(), which is not further defined in the given code snippet.
#Overall this is what the function does:The function accepts no parameters and returns an integer value obtained from the function `func_2()`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the specified `delimiter` and converting each resulting substring into an integer.
#Overall this is what the function does:The function accepts a delimiter (a string) as input and returns a list of integers. It achieves this by first calling another function `func_2()` to get a string, then splits this string using the provided delimiter, and finally converts each resulting substring into an integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2⋅10^5. a is a list of n integers where 1 ≤ a_i ≤ 2⋅10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def func_5():
    return func_2()
    #The program returns the result of calling the function `func_2()` with the current values of the variables `t`, `n`, `m`, `k`, `a`, `d`, and `f` as arguments.
#Overall this is what the function does:The function indirectly calls `func_2(t, n, m, k, a, d, f)` and returns its result. Here, `t` is an integer between 1 and 10^4, `n` is an integer between 2 and 10^5, `m` and `k` are integers between 1 and 2⋅10^5, `a` is a list of `n` integers sorted in ascending order with each integer between 1 and 2⋅10^9, `d` is a list of `m` integers each between 1 and 10^9, and `f` is a list of `k` integers each between 1 and 10^9. The function does not modify any of these inputs; instead, it passes them to `func_2()` and returns whatever `func_2()` returns.

#State of the program right berfore the function call: (n, m, k) are positive integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. D is a sorted list of unique integers obtained by sorting the list generated by m integers d_1, d_2, ..., d_m where 1 <= d_i <= 10^9. F is a list of k integers where 1 <= f_i <= 10^9.
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
        
    #State: Output State: `A` is the return value of `func_4()`, `D` is a sorted list of unique elements returned by `func_4()`, `F` is the return value of `func_4()`, `max_diff` is the maximum difference found between consecutive elements in `A`, `next_max_diff` is the second maximum difference found between consecutive elements in `A`, `index` is the index of the first element involved in the maximum difference.
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
        
    #State: Output State: `A` is the return value of `func_4()`, `D` is a sorted list of unique elements returned by `func_4()`, `F` is the return value of `func_4()`, `max_diff` is the maximum difference found between consecutive elements in `A`, `next_max_diff` is the second maximum difference found between consecutive elements in `A`, `index` is the index of the first element involved in the maximum difference, `left` is `A[index - 1]`, `right` is `A[index]`, `ans` is the minimum value obtained by evaluating `min(max(D[l] + f - left, right - D[l] - f))` for each `f` in `F` and updating it during the loop iterations.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff)
#Overall this is what the function does:The function processes three lists: `A`, `D`, and `F`. It calculates the maximum difference (`max_diff`) and the second maximum difference (`next_max_diff`) between consecutive elements in `A`. Then, it iterates through each element in `F` and finds the minimum value by evaluating a specific condition involving elements from `D`. Finally, it prints the maximum value between `ans` and `next_max_diff`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each testcase, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: Output State: `testcases` is the result of `func_3()` call, `t` is an integer such that 1 <= t <= 10^4, `n`, `m`, and `k` are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5, `a` is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}, `d` is a list of m integers where 1 <= d_i <= 10^9, `f` is a list of k integers where 1 <= f_i <= 10^9, `func_6` has been called `testcases` times.
    #
    #In this output state, the variable `testcases` remains unchanged, and `func_6` has been executed `testcases` times. The other variables (`t`, `n`, `m`, `k`, `a`, `d`, `f`) remain in their initial states as they are not affected by the loop.
#Overall this is what the function does:The function processes multiple test cases, each involving four lists (a, d, f) and three integers (t, n, m, k). It calls another function `func_6` for each test case, but does not modify the input lists or integers. The function returns the result of `func_6` after processing all test cases.

