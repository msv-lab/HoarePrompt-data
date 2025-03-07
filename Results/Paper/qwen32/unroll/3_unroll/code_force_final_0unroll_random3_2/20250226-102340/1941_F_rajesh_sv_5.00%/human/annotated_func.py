#State of the program right berfore the function call: func is a function that takes no arguments and returns a wrapper function.
def func_1(func):
    d = {}
    return wrapper
    #The program returns a wrapper function.
#Overall this is what the function does:The function `func_1` accepts a function `func` as a parameter and returns a wrapper function.

#State of the program right berfore the function call: args is a tuple containing arguments that can be of any type and value, and d is a dictionary that maps these tuples to their corresponding results.
def wrapper():
    if (args not in d) :
        d[args] = func(*args)
    #State: `args` is a tuple containing arguments that can be of any type and value, and `d` is a dictionary that maps these tuples to their corresponding results. If `args` was not originally in `d`, then `d` now includes the entry `args: func(*args)`. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the result corresponding to the tuple 'args' in the dictionary 'd'. If 'args' was not originally in 'd', then 'd' now includes the entry 'args: func(*args)' and the result is the output of 'func(*args)'. Otherwise, the result is the value already mapped to 'args' in 'd'.
#Overall this is what the function does:The function accepts a tuple `args` and a dictionary `d`. It returns the result corresponding to `args` in `d`. If `args` is not in `d`, it computes the result by calling `func(*args)`, adds the entry `args: func(*args)` to `d`, and returns the computed result. Otherwise, it returns the value already mapped to `args` in `d`.

#State of the program right berfore the function call: The function `func_2` does not have any input parameters. It reads a line from the standard input, strips any leading or trailing whitespace, and returns the resulting string.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is read from the standard input, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_2` reads a line from the standard input, removes any leading or trailing whitespace from the line, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_3`. Therefore, no precondition can be derived from the function signature alone.
def func_3():
    return int(func_2())
    #The program returns the integer value returned by `func_2()`
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an integer value, which is the result of the function `func_2()`.

#State of the program right berfore the function call: delimiter is a string used to split the input string into a list of integers.
def func_4(delimiter):
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers, where the integers are obtained by splitting the string returned by `func_2()` using the `delimiter` string and converting each resulting substring to an integer.
#Overall this is what the function does:The function takes a string `delimiter` as input, splits the string returned by `func_2()` using this `delimiter`, converts each resulting substring to an integer, and returns a list of these integers.

#State of the program right berfore the function call: This function does not have any parameters, so there are no variables or relationships to describe.
def func_5():
    return func_2()
    #The program returns the result of the function `func_2()`
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the result of the function `func_2()`.

#State of the program right berfore the function call: n, m, and k are positive integers representing the number of prepared problems, the number of models, and the number of functions, respectively. A is a sorted list of n integers representing the complexities of the prepared problems. D is a sorted list of unique integers representing the complexities of the models. F is a list of k integers representing the complexities of the functions.
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
        
    #State: `A` is the list returned by `func_4()`, `n` is the length of the list returned by `func_4()`, `m` and `k` are the values returned by `func_4()`, `D` is a sorted list of unique integers returned by `func_4()`, `F` is the list returned by `func_4()`, `max_diff` is the largest difference between consecutive elements in `A`, `next_max_diff` is the second largest difference between consecutive elements in `A`, `index` is the index of the element in `A` that is part of the pair with the largest difference.
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
        
    #State: A is the list returned by `func_4()`, n is the length of the list returned by `func_4()`, m and k are the values returned by `func_4()`, D is a sorted list of unique integers returned by `func_4()`, F is the list returned by `func_4()`, max_diff is the largest difference between consecutive elements in A, next_max_diff is the second largest difference between consecutive elements in A, index is the index of the element in A that is part of the pair with the largest difference, left is A[index - 1], right is A[index], ans is the smallest possible maximum difference found during the loop's execution.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the smallest possible maximum difference found during the loop's execution and next_max_diff is the second largest difference between consecutive elements in A)
#Overall this is what the function does:The function calculates and prints the maximum of the second largest difference between consecutive elements in a sorted list of problem complexities and the smallest possible maximum difference that can be achieved by adjusting the complexities of the problems using the complexities of the functions and models.

#State of the program right berfore the function call: testcases is a positive integer representing the number of test cases.
def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is the value returned by `func_3()`.
#Overall this is what the function does:The function `func_7` executes a number of test cases determined by the value returned from `func_3()`. For each test case, it calls `func_6()`. The function itself does not accept any parameters and does not return a value.

