#State of the program right berfore the function call: func is a callable object representing a function or method.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a wrapper object.
#Overall this is what the function does:The function `func_1` accepts a callable object `func` and returns a wrapper object.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `t` is an integer such that 1 <= t <= 10^4; if `args` are not in `d`, then `d[args]` is assigned the value of `func(*args)`, where `args` are the arguments passed to the function, and the values of `n`, `m`, `k`, `a`, `d`, and `f` remain unchanged.
    return d[args]
    #The program returns the value of `func(*args)` stored in dictionary `d` under key `args`
#Overall this is what the function does:The function uses the arguments passed through `*args` to look up a value in dictionary `d`. If the key `args` exists in `d`, it returns the corresponding value. If the key does not exist, it calls `func(*args)`, stores the result in `d` under the key `args`, and then returns this stored value.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers sorted in ascending order such that 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers such that 1 <= d_i <= 10^9. f is a list of k integers such that 1 <= f_i <= 10^9.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it as a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns it as a string. This operation does not depend on any external parameters and can be performed multiple times independently.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. The list a is a sorted list of n integers such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. The list d is a list of m integers such that 1 ≤ d_i ≤ 10^9. The list f is a list of k integers such that 1 ≤ f_i ≤ 10^9.
def func_3():
    return int(func_2())
    #The program returns an integer value calculated by the function func_2(), which is not defined in the given code snippet. Since the exact implementation of func_2() is not provided, we cannot determine the specific integer value it returns. However, it will be an integer within the range as described by the initial state constraints.
#Overall this is what the function does:The function does not accept any direct parameters. Instead, it relies on predefined variables and lists (t, n, m, k, a, d, f) with specific constraints. After executing, it returns an integer value calculated by calling another function `func_2()`. This returned integer will fall within the range defined by the initial state constraints.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers converted from a string split by a delimiter, where the string is the result of calling `func_2()` and splitting its content.
#Overall this is what the function does:The function accepts a delimiter (a string) and returns a list of integers. It achieves this by first calling another function `func_2()`, then splitting the resulting string using the provided delimiter, and finally converting each split part into an integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2⋅10^5. a is a list of n integers where 1 ≤ a_i ≤ 2⋅10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def func_5():
    return func_2()
    #The program returns the result of calling the function `func_2()` with the current state of variables `t`, `n`, `m`, `k`, `a`, `d`, and `f`.
#Overall this is what the function does:The function calls another function `func_2()` with the current values of the variables `t`, `n`, `m`, `k`, `a`, `d`, and `f`. It then returns the result of this call.

#State of the program right berfore the function call: (n, m, k) are positive integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5; A is a list of n strictly increasing integers where 1 <= A[i] <= 2 * 10^9; D is a list of unique integers obtained by sorting the list of m integers d_i (1 <= d_i <= 10^9); F is a list of k integers representing the complexities of the functions (1 <= f_i <= 10^9).
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
        
    #State: `max_diff` is the maximum difference found across all pairs of adjacent elements in the list `A`, `next_max_diff` is the second maximum difference found (or -inf if no such difference exists), `index` is the index where `max_diff` occurred (or None if not applicable), `i` is `n`, and `diff` is `A[1] - A[0]` if `max_diff` was updated during the last iteration or does not exist otherwise.
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
        
    #State: `ans` holds the smallest value it has been updated to throughout all iterations of the loop, which is determined by the minimum of `max(D[l] + f - left, right - D[l] - f)` for all values of `f` in `F`. The variables `l`, `h`, `mid`, `mid_sum`, `mid_next_sum`, `left`, `right`, `f`, and `D` remain in their final states from the last iteration of the loop.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the smallest value obtained from the expression max(D[l] + f - left, right - D[l] - f) for all f in F, and next_max_diff is the next maximum difference calculated during the loop)
#Overall this is what the function does:The function processes three lists: A (a list of n strictly increasing integers), D (a sorted list of m unique integers), and F (a list of k integers representing complexities). It calculates the maximum difference between adjacent elements in list A and finds the smallest value that can be obtained by adjusting the elements of A using values from list D and complexities from list F. Finally, it prints the maximum of this smallest value and the second largest difference found in list A.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each testcase, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: Output State: `testcases` must be greater than 3.
    #
    #In natural language: The output state after the loop executes all its iterations is that `testcases` must be greater than 3. This is because the loop runs `testcases` times, and we know it has run at least 3 times. Therefore, `testcases` had to be at least 3 initially and must remain greater than 3 after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each involving lists and integers. It initializes the number of test cases and ensures that this number is greater than 3 after processing all test cases. The function does not return any value directly but modifies internal states based on the given inputs.

