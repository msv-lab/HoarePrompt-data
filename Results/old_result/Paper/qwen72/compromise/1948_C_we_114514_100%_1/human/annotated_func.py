#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 2 * 10^5, row1 and row2 are strings of length n consisting only of the characters '<' and '>'.
def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: The loop completes all iterations, and the variables `n`, `row1`, `row2`, and `half_n` remain unchanged. If the loop does not encounter a condition where `row1[2 * i + 1] == '<'` and `(row2[2 * i] == '<' or row2[2 * i + 2] == '<')` for any `i` in the range `0` to `half_n - 2`, the loop will finish without returning 'No'.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: The loop completes all iterations, and the variables `n`, `row1`, `row2`, and `half_n` remain unchanged. The loop does not encounter a condition where `row1[2 * i + 1] == '<'` and `(row2[2 * i] == '<' or row2[2 * i + 2] == '<')` for any `i` in the range `0` to `half_n - 2`. Additionally, `row1[n - 1]` is not equal to '<' or `row2[n - 2]` is not equal to '<'.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts an even integer `n` within the range 2 to 200,000, and two strings `row1` and `row2` of length `n` containing only '<' and '>'. It checks if it is possible for a robot to move from position (1,1) to position (2,n) based on the conditions in `row1` and `row2`. If at any point during the check, the robot is blocked by '<' characters in a specific pattern, the function returns 'No'. Otherwise, it returns 'Yes'. The function does not modify the input variables `n`, `row1`, or `row2`.

#State of the program right berfore the function call: No variables are passed to the function func_2, but it interacts with the input to obtain t, n, row1, and row2. t is an integer such that 1 <= t <= 10^4, n is an even integer such that 2 <= n <= 2 \cdot 10^5, row1 and row2 are strings of length n consisting of characters '<' and/or '>', and the sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: `t` is an input integer, `n`, `row1`, and `row2` remain unchanged, `results` is a list containing the results of `func_1(n, row1, row2)` for each iteration of the loop, where `n`, `row1`, and `row2` are the inputs provided during each iteration.
    print('\n'.join(results))
    #This is printed: Each result of `func_1(n, row1, row2)` for each iteration of the loop, printed on a new line.
#Overall this is what the function does:The function `func_2` processes `t` test cases, where each test case includes an even integer `n` and two strings `row1` and `row2` of length `n` consisting of characters '<' and/or '>'. It reads these inputs from the standard input, calls `func_1` with `n`, `row1`, and `row2` for each test case, and collects the results in a list. After processing all test cases, it prints each result on a new line. The function does not return any value.

