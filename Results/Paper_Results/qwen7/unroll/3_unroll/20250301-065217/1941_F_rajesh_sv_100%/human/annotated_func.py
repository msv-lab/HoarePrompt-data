#State of the program right berfore the function call: func is a function object.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a function object named wrapper.
#Overall this is what the function does:The function `func_1` accepts another function object as a parameter and returns a new function object named `wrapper`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. a is a list of n integers where 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n`, `m`, and `k` are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5, `a` is a list of n integers where 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}, `d` is a list of m integers where 1 ≤ d_i ≤ 10^9, `f` is a list of k integers where 1 ≤ f_i ≤ 10^9. If `args` is not in `d`, then `d[args]` is set to the result of `func(*args)` where `args` is a tuple of arguments passed to the function `func`.
    return d[args]
    #The program returns the value of `d[args]` where `args` is a tuple of arguments that was not previously in list `d`. The value of `d[args]` is the result of calling the function `func` with `args` as its arguments.
#Overall this is what the function does:The function acts as a wrapper to handle multiple test cases. For each test case, it checks if the arguments are already in the dictionary `d`. If not, it calls the function `func` with those arguments and stores the result in `d`. Finally, it returns the stored result for the given arguments.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. a is a list of n integers sorted in ascending order such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. d is a list of m integers such that 1 ≤ d_i ≤ 10^9. f is a list of k integers such that 1 ≤ f_i ≤ 10^9.
def func_3():
    return int(func_2())
    #The program returns an integer value obtained from the function func_2(), which is not specified in the given code snippet. The exact value depends on the implementation of func_2().
#Overall this is what the function does:The function accepts no parameters and returns an integer value obtained from another unspecified function `func_2()`. The exact integer value returned depends on the implementation of `func_2()`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. a is a list of n integers where 1 <= a_i <= 2 * 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 <= d_i <= 10^9. f is a list of k integers where 1 <= f_i <= 10^9.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers converted from a string split by a delimiter, where the string is the result of calling `func_2()` and splitting its output.
#Overall this is what the function does:The function accepts a delimiter parameter and returns a list of integers. This list is obtained by converting a string, which is the result of calling `func_2()` and splitting it using the provided delimiter, into a list of integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2⋅10^5. The list a is a sorted list of n integers such that 1 ≤ a_i ≤ 2⋅10^9 and a_i < a_{i+1}. The list d is a list of m integers such that 1 ≤ d_i ≤ 10^9. The list f is a list of k integers such that 1 ≤ f_i ≤ 10^9.
def func_5():
    return func_2()
    #The program returns the result of the function `func_2()` which is not defined in the given code snippet.
#Overall this is what the function does:The function does not accept any parameters and returns the result of another undefined function `func_2()`. The final state of the program is that it has returned this result.

#State of the program right berfore the function call: (n, m, k) are positive integers such that 2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5. A is a list of n strictly increasing integers representing the complexities of the prepared problems, D is a list of unique integers representing the complexities of the models after sorting, F is a list of k positive integers representing the complexities of the functions.
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
        
    #State: Output State: `max_diff` is the largest difference found between consecutive elements in the array `A`, `next_max_diff` is the second largest difference found between consecutive elements in the array `A`, and `index` is the index of the element where `max_diff` was found.
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
        
    #State: max_diff is the largest difference found between consecutive elements in the array A, next_max_diff is the second largest difference found between consecutive elements in the array A, index is the index of the element where max_diff was found, left is A[index - 1], right is A[index], ans is the minimum value among all calculated differences during the loop iterations.
    print(max(ans, next_max_diff))
    #This is printed: next_max_diff
#Overall this is what the function does:The function accepts three parameters: n, m, and k, where n is a positive integer between 2 and 10^5, m and k are positive integers between 1 and 2 * 10^5. Additionally, A is a list of n strictly increasing integers, D is a list of unique integers, and F is a list of k positive integers. The function calculates the maximum difference between consecutive elements in the list A and finds the minimum value among all possible differences between elements in D and adjusted values from F. Finally, it prints the larger of the maximum difference or the second-largest difference.

#State of the program right berfore the function call: testcases is a positive integer indicating the number of test cases. For each test case, n, m, and k are positive integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 ⋅ 10^5. a is a sorted list of n integers where 1 ≤ a_i ≤ 2 ⋅ 10^9 and a_i < a_{i+1}. d is a list of m integers where 1 ≤ d_i ≤ 10^9. f is a list of k integers where 1 ≤ f_i ≤ 10^9.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: Output State: `func_6()` has been called `testcases` times.
#Overall this is what the function does:The function processes a series of test cases, each involving a sorted list of integers (a), and two other lists of integers (d and f). For each test case, it calls `func_6()`, which performs unspecified operations on the inputs. After processing all test cases, it does not return any value but ensures that `func_6()` has been called the specified number of times (`testcases`).

