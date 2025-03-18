#State of the program right berfore the function call: func is a callable function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a callable function named 'wrapper'.
#Overall this is what the function does:The function `func_1` accepts a callable function `func` and returns a new callable function named `wrapper`. The function does not modify any input variables and does not perform any actions other than creating and returning the `wrapper` function.

#State of the program right berfore the function call: args is a tuple of arguments that are passed to the function `func`. The tuple `args` can contain any number of elements, and the elements can be of any type. `d` is a dictionary that maps tuples of arguments to the results of `func` when called with those arguments.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple of arguments that can contain any number of elements of any type. `d` is a dictionary that maps tuples of arguments to the results of `func` when called with those arguments. If `args` is not a key in `d`, then `args` is now a key in `d`, and the value associated with `args` in `d` is the result of `func` when called with the arguments in `args`.
    return d[args]
    #The program returns the value associated with `args` in the dictionary `d`. If `args` was not a key in `d` before, it is now added as a key, and the value associated with `args` is the result of calling `func` with the arguments in `args`.
#Overall this is what the function does:The function `wrapper` takes no explicit parameters but uses the global variables `args` and `d`. It returns the value associated with `args` in the dictionary `d`. If `args` is not already a key in `d`, the function calls `func` with the arguments in `args`, stores the result in `d` with `args` as the key, and then returns this result. The dictionary `d` is updated to include the result of `func` for the given `args` if it was not previously present.

#State of the program right berfore the function call: No variables are used in the function signature.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the first line of input from the user, with any leading or trailing whitespace removed.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return int(func_2())
    #The program returns an integer value that is the result of calling the function `func_2()`. Since `func_2()` is not defined in the initial state, the exact value cannot be determined, but it will be an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an integer value that is the result of calling another function `func_2()`. The exact integer value returned depends on the implementation of `func_2()`, which is not provided.

#State of the program right berfore the function call: delimiter is a string used to split the input, typically a space (' ') or another character.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers obtained by splitting the string returned by `func_2()` using the `delimiter` and converting each resulting substring into an integer.
#Overall this is what the function does:The function `func_4` accepts a parameter `delimiter` and returns a list of integers. This list is obtained by splitting the string returned by `func_2()` using the provided `delimiter` and converting each resulting substring into an integer. The function does not modify any external state or variables.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_5():
    return func_2()
    #The program returns the value returned by the function `func_2()`.
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of calling `func_2()`. After the function concludes, the program state is such that the value returned by `func_2()` is the final output of `func_5`.

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
        
    #State: `A` is a list of `n` integers where 1 <= `A[i]` <= 2 * 10^9 and `A[i]` < `A[i+1]`, `n` is the length of `A`, `i` is `n - 1`, `m` and `k` are assigned the values returned by `func_4()`, `D` is a sorted list of unique integers derived from the list returned by `func_4()`, `F` is a list of `k` integers where 1 <= `F[i]` <= 10^9, `max_diff` is the largest difference between consecutive elements in `A`, `next_max_diff` is the second largest difference between consecutive elements in `A`, and `index` is the index of the element in `A` that follows the element which, together with the previous element, forms the largest difference.
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
        
    #State: The loop has finished executing, and `l` and `h` are equal for each iteration. The variables `A`, `n`, `i`, `m`, `k`, `D`, `F`, `max_diff`, `next_max_diff`, `index`, `left`, and `right` remain unchanged. `ans` is now the minimum value of its initial value and the maximum of `D[l] + f - left` and `right - D[l] - f` for each `f` in `F` where `l` and `h` are equal.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum value of its initial value and the maximum of D[l] + f - left and right - D[l] - f for each f in F where l and h are equal, and next_max_diff is a fixed value)
#Overall this is what the function does:The function `func_6` processes three lists of integers, `A`, `D`, and `F`. It finds the largest and second largest differences between consecutive elements in the sorted list `A`. It then calculates the minimum possible maximum difference between the elements `left` and `right` (which are the elements in `A` forming the largest difference) and any element in `D` adjusted by each element in `F`. Finally, it prints the maximum of this calculated value and the second largest difference found in `A`. The function does not return any value; it only prints the result.

#State of the program right berfore the function call: No variables are passed to the function `func_7`.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` must be greater than or equal to the number of iterations executed, `_` is a placeholder and does not need to be adjusted, `func_6()` has been called the number of times equal to the value of `testcases`, and `func_6()` has returned after each call.
#Overall this is what the function does:The function `func_7` does not accept any parameters and does not return any value. It calls `func_3` to get the number of test cases, and then it calls `func_6` that many times. After the function concludes, `func_6` has been called the number of times equal to the value returned by `func_3`.

