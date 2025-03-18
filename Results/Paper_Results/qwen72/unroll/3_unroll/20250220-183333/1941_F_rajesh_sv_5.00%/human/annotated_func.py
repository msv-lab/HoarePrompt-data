#State of the program right berfore the function call: func is a callable function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a callable function named 'wrapper'.
#Overall this is what the function does:The function `func_1` accepts a callable function `func` and returns a new callable function named `wrapper`. The function does not modify the input `func` or any external state; it simply creates and returns the `wrapper` function.

#State of the program right berfore the function call: args is a tuple of arguments that can be passed to the function `func`, and `d` is a dictionary that maps tuples of arguments to their computed results by `func`.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple of arguments that can be passed to the function `func`, and `d` is a dictionary that maps tuples of arguments to their computed results by `func`. If `args` is not already a key in `d`, then `args` is added as a key, and `d[args]` is set to the result of `func(*args)`. If `args` is already a key in `d`, the state of `d` remains unchanged.
    return d[args]
    #The program returns the value associated with the key `args` in the dictionary `d`. If `args` was not already a key in `d`, it is added with its value set to the result of `func(*args)`. If `args` was already a key in `d`, the value associated with `args` is returned without changing the state of `d`.
#Overall this is what the function does:The function `wrapper` does not accept any parameters. It checks if the tuple `args` is a key in the dictionary `d`. If `args` is not a key in `d`, it adds `args` as a key and sets its value to the result of `func(*args)`. If `args` is already a key in `d`, the state of `d` remains unchanged. The function returns the value associated with the key `args` in the dictionary `d`.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the first line of input from the user, with any leading or trailing whitespace removed.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling the function `func_2()`.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an integer value that is the result of calling the function `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input, defaulting to a single space ' '
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` (a single space ' ') and converting each split part into an integer.
#Overall this is what the function does:The function `func_4` accepts a parameter `delimiter` (a string, defaulting to a single space ' '). It returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` and converting each split part into an integer. The function does not modify any external state or variables.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any arguments.
def func_5():
    return func_2()
    #The program returns the value or result of `func_2()`, which is not defined in the initial state.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It returns the result of calling `func_2()`. The final state of the program after the function concludes is that the value or result of `func_2()` is returned.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 1 <= m <= 2 * 10^5, and 1 <= k <= 2 * 10^5. A is a list of n integers where 1 <= A[i] <= 2 * 10^9 and A[i] < A[i+1]. D is a sorted list of unique integers derived from a list of m integers where 1 <= D[i] <= 10^9. F is a list of k integers where 1 <= F[i] <= 10^9.
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
        
    #State: `max_diff` is the maximum difference between consecutive elements in the list `A`, `next_max_diff` is the second largest difference between consecutive elements in the list `A`, and `index` is the index of the element in `A` where the maximum difference occurs. The values of `n`, `m`, `k`, `A`, `D`, and `F` remain unchanged.
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
        
    #State: `ans` is the minimum possible value of the maximum difference between `left` and `D[l] + f`, and `right` and `D[l] + f` for all `f` in `F`. The values of `n`, `m`, `k`, `A`, `D`, and `F` remain unchanged.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where `ans` is the minimum possible value of the maximum difference between `left` and `D[l] + f`, and `right` and `D[l] + f` for all `f` in `F`, and `next_max_diff` is another maximum difference value)
#Overall this is what the function does:The function `func_6` takes no explicit parameters but implicitly uses `n`, `m`, `k`, `A`, `D`, and `F`, where `n`, `m`, and `k` are integers within specified ranges, `A` is a sorted list of `n` integers, `D` is a sorted list of unique integers derived from `m` integers, and `F` is a list of `k` integers. The function calculates the maximum difference (`max_diff`) and the second largest difference (`next_max_diff`) between consecutive elements in `A`. It then finds the minimum possible value of the maximum difference between a specific range in `A` and elements in `D` adjusted by elements in `F`. Finally, it prints the maximum of this minimum value and `next_max_diff`. The values of `n`, `m`, `k`, `A`, `D`, and `F` remain unchanged.

#State of the program right berfore the function call: No variables are passed to the function `func_7`.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is the result of `func_3()` execution, and no other variables are affected.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It calls `func_3` to determine the number of test cases, and then for each test case, it calls `func_6`. The function does not return any value. After the function concludes, `testcases` holds the result of `func_3` execution, and no other variables are affected.

