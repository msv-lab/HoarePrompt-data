#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 2 * 10^5, row1 and row2 are strings of length n consisting of '<' and '>' characters.
def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: n is an even integer such that 2 <= n <= 2 * 10^5, row1 and row2 are strings of length n consisting of '<' and '>' characters, half_n is n // 2.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: `n` is an even integer such that 2 <= n <= 2 * 10^5, `row1` and `row2` are strings of length `n` consisting of '<' and '>' characters, `half_n` is `n // 2`. It is not the case that `row1[n - 1]` is '<' and `row2[n - 2]` is '<'
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` determines if a robot can move from position (1,1) to (2,n) on a grid based on the given rules defined by the strings `row1` and `row2`. It returns 'No' if the robot cannot make the move due to specific configurations of '<' and '>' in `row1` and `row2`, otherwise it returns 'Yes'.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, row1 and row2 are strings of length n consisting of '<' and/or '>'.
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
        
    #State: `n` is the integer value from the last iteration, `row1` is the string from the last iteration, `row2` is the string from the last iteration, `t` remains unchanged, `results` is a list of `t` elements, each being the result of `func_1(n, row1, row2)` from each iteration.
    print('\n'.join(results))
    #This is printed: Each element of the `results` list printed on a new line (where `results` is a list of `t` elements, each being the result of `func_1(n, row1, row2)` from each iteration)
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and two strings `row1` and `row2` of length `n` containing '<' and/or '>'. For each test case, it computes a result using the `func_1` function and stores these results. Finally, it prints each result on a new line.

