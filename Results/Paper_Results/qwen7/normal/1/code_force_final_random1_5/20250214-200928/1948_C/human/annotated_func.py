#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2⋅10^5, row1 is a string consisting of exactly n characters '<' and/or '>', and row2 is a string consisting of exactly n characters '<' and/or '>' where n is even.
def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: Output State: The function returns 'No'.
    #
    #Natural Language Explanation: After all iterations of the loop have executed, the function will have returned 'No' if it did not encounter any instance where `row1[2 * i + 1]` is '<' and either `row2[2 * i]` or `row2[2 * i + 2]` is '<' for any `i` from 0 to `half_n - 2`. Since the loop exits immediately upon finding such a condition, and we've gone through all possible iterations without finding one, the function must return 'No'.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: The function returns 'No', `row1` and `row2` are lists of characters, and for all `i` from 0 to `half_n - 2`, `row1[2 * i + 1]` is not '<' or either `row2[2 * i]` or `row2[2 * i + 2]` is not '<'.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function accepts three parameters: an integer \( n \) (where \( 2 \leq n \leq 2 \cdot 10^5 \)), a string \( row1 \) consisting of exactly \( n \) characters '<' and/or '>', and a string \( row2 \) consisting of exactly \( n \) characters '<' and/or '>'. The function checks specific conditions related to the characters in \( row1 \) and \( row2 \). If any condition is met, the function returns 'No'. Otherwise, it returns 'Yes'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even. row1 and row2 are strings of length n, consisting only of '<' and '>', representing the first and second rows of the grid respectively.
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
        
    #State: Output State: `t` must be greater than 0, `n` is an input integer, `row1` is an input string from the user, `row2` is an input string from the user, `results` is a list containing `t` elements where each element is the return value of `func_1(n, row1, row2)` for each iteration of the loop.
    #
    #This means that after all iterations of the loop have finished, `t` will still be the same as the initial value provided, `n`, `row1`, and `row2` will be the last values input by the user during the final iteration of the loop. The `results` list will contain the return values of `func_1(n, row1, row2)` for each of the `t` iterations, in the order they were computed.
    print('\n'.join(results))
    #This is printed: the return values of func_1(n, row1, row2) for each of the t iterations, each on a new line
#Overall this is what the function does:The function reads multiple test cases from the user input. For each test case, it takes an integer `n`, a string `row1`, and a string `row2`. It then calls another function `func_1` with these inputs and stores the result. After processing all test cases, it prints the results of `func_1` for each test case, each on a new line.

