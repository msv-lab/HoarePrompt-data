#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 2 * 10^5, row1 and row2 are strings of length n consisting of characters '<' and/or '>'.
def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: the loop completes without returning 'No'.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: the loop completes without returning 'No', and either `row1[n - 1]` is not equal to '<' or `row2[n - 2]` is not equal to '<'
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` determines if a robot can move from position (1,1) to (2,n) on a grid based on the given rules defined by the strings `row1` and `row2`. It returns 'No' if the robot encounters an obstacle according to the specified conditions, otherwise it returns 'Yes'.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, row1 and row2 are strings of length n consisting of '<' and/or '>' characters.
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
        
    #State: `n` is the integer and `row1` and `row2` are the strings from the last iteration, and `results` is a list of `t` elements, each being the output of `func_1` for each iteration.
    print('\n'.join(results))
    #This is printed: result1\nresult2\n...\nresultt (where result1, result2, ..., resultt are the outputs of `func_1` for each iteration)
#Overall this is what the function does:The function `func_2` reads multiple test cases from the input. For each test case, it processes two strings `row1` and `row2` of length `n` consisting of '<' and/or '>' characters. It determines if there is at least one position in both strings where the characters are the same ('<' or '>'). If such a position exists, it returns "Yes"; otherwise, it returns "No". The results for all test cases are printed, each on a new line.

