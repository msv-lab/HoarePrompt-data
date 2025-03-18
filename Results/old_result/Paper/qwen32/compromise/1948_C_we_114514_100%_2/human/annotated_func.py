#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 2 * 10^5, row1 and row2 are strings of length n consisting of '<' and/or '>' characters.
def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: The loop has completed all iterations without returning 'No'.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: The loop has completed all iterations without returning 'No'. It is not the case that both `row1[n - 1]` is '<' and `row2[n - 2]` is '<'.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` determines if a robot can move from position (1,1) to (2,n) on a grid based on the directions provided in two strings `row1` and `row2`. It returns 'No' if the robot encounters an obstacle according to specific conditions, otherwise it returns 'Yes'.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, row1 and row2 are strings of length n consisting of the characters '<' and/or '>'.
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
        
    #State: `results` is a list containing the results of `func_1(n, row1, row2)` for each of the `t` iterations.
    print('\n'.join(results))
    #This is printed: Each element of the `results` list on a new line (where `results` contains the results of `func_1(n, row1, row2)` for each of the `t` iterations)
#Overall this is what the function does:The function `func_2` reads multiple test cases from the input, where each test case consists of an integer `n` and two strings `row1` and `row2` of length `n` containing only the characters '<' and '>'. For each test case, it computes a result using the function `func_1` and stores these results. Finally, it prints each result on a new line.

