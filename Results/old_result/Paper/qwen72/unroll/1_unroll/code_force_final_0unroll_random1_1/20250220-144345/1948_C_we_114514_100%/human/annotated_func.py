#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 2 * 10^5, row1 and row2 are strings of length n consisting of characters '<' and '>'.
def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: The loop completes all iterations, and the values of `n`, `row1`, `row2`, and `half_n` remain unchanged. If the loop does not encounter a condition where `row1[2 * i + 1] == '<'` and `(row2[2 * i] == '<' or row2[2 * i + 2] == '<')` for any `i` in the range `0` to `half_n - 2`, the loop will finish without returning 'No'.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: The loop completes all iterations, and the values of `n`, `row1`, `row2`, and `half_n` remain unchanged. The loop does not encounter a condition where `row1[2 * i + 1] == '<'` and `(row2[2 * i] == '<' or row2[2 * i + 2] == '<')` for any `i` in the range `0` to `half_n - 2`, and the loop finishes without returning 'No'. Additionally, `row1[n - 1]` is not equal to '<' or `row2[n - 2]` is not equal to '<'.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` takes an even integer `n` within the range 2 to 2 * 10^5, and two strings `row1` and `row2` of length `n` containing only the characters '<' and '>'. It checks if a robot can move from position (1,1) to position (2,n) based on the given rows. The function returns 'No' if at any point during the check, the robot is blocked from moving to the next position by '<' characters in `row1` and `row2`. Otherwise, it returns 'Yes'. The function does not modify the input parameters `n`, `row1`, or `row2`.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads input values directly, where `t` is an integer representing the number of test cases, and for each test case, `n` is an even integer within the range 2 to 2 * 10^5, and `row1` and `row2` are strings of length `n` containing only the characters '<' and '>'.
def func_2():
    """
    读取输入并处理每个测试用例。
    """
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        
        row1 = input()
        
        row2 = input()
        
        results.append(func_1(n, row1, row2))
        
    #State: Output State: `t` is an input integer representing the number of test cases. `results` is a list containing `t` elements, where each element is the result of calling `func_1` with the corresponding `n`, `row1`, and `row2` from each test case. `n`, `row1`, and `row2` are not defined outside the loop and are reset for each iteration.
    print('\n'.join(results))
    #This is printed: [result of func_1 for test case 1]
    #[result of func_1 for test case 2]
    #...
    #[result of func_1 for test case t]
#Overall this is what the function does:The function `func_2` reads the number of test cases `t` from the input. For each test case, it reads an even integer `n` and two strings `row1` and `row2` of length `n` containing only the characters '<' and '>'. It processes each test case by calling `func_1` with `n`, `row1`, and `row2`, and collects the results in a list. After processing all test cases, it prints the results, one per line. The function does not return any value.

