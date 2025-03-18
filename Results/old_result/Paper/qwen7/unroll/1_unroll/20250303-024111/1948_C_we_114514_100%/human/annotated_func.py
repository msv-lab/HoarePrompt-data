#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2⋅10^5, row1 is a string of length n consisting of characters '<' and/or '>', and row2 is a string of length n consisting of characters '<' and/or '>' where n is even.
def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: Output State: `half_n` is `n // 2`, `n` is unchanged, `row1` is a string of length `n` consisting of characters '<' and/or '>', and `row2` is a string of length `n` consisting of characters '<' and/or '>', and the loop has executed all its iterations without returning 'No'.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: `half_n` is `n // 2`, `n` is unchanged, `row1` is a string of length `n` consisting of characters '<' and/or '>', and `row2` is a string of length `n` consisting of characters '<' and/or '>', and either the last character of `row1` is not '<' or the second last character of `row2` is not '<'
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function accepts three parameters: an integer `n` (where 2 ≤ n ≤ 2⋅10^5) and two strings `row1` and `row2` (each of length `n` and consisting only of characters '<' and/or '>'). It checks specific conditions related to the characters in these strings and returns 'No' if certain invalid configurations are found, otherwise it returns 'Yes'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even. row1 and row2 are strings of length n consisting of characters '<' and/or '>'.
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
        
    #State: t elements in the results list, each element is the result of calling func_1(n, row1, row2) for each iteration of the loop with the respective n, row1, and row2 inputs.
    print('\n'.join(results))
    #This is printed: a string where each line is the result of func_1(n, row1, row2) for each iteration, separated by newlines
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three inputs: an integer `t` (number of test cases), another integer `n`, and two strings `row1` and `row2` of length `n`. It then calls `func_1(n, row1, row2)` for each test case and stores the result. Finally, it prints the results of all test cases, each on a new line.

