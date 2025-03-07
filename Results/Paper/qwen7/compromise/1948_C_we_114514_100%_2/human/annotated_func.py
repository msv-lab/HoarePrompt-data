#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, row1 is a string consisting of exactly n characters '<' and/or '>', and row2 is a string consisting of exactly n characters '<' and/or '>' representing the first and second rows of the grid respectively. Additionally, n is even.
def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: n is unchanged, half_n is n // 2, no value for row1 or row2 provided, no return value from the loop.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: n is unchanged, half_n is n // 2, no value for row1 or row2 provided, and either row1[n - 1] ≠ '<' or row2[n - 2] ≠ '<'
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 2 * 10^5 and n is even), and two strings `row1` and `row2` each consisting of exactly n characters '<' and/or '>'. It checks if it's possible to pair up all characters in `row1` and `row2` such that each '<' in `row1` is paired with a '>' in `row2` and vice versa, forming valid pairs. If such a pairing is possible, the function returns 'Yes'; otherwise, it returns 'No'.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases; n is a positive even integer representing the number of columns in the grid; row1 is a string of length n containing only '<' and '>' characters representing the first row of the grid; row2 is a string of length n containing only '<' and '>' characters representing the second row of the grid.
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
        
    #State: Output State: `results` is a list containing `t` elements, where each element is the result of calling `func_1(n, row1, row2)` with the respective inputs from each iteration of the loop. Each iteration reads an integer `n`, followed by two strings `row1` and `row2`, and appends the result of `func_1(n, row1, row2)` to the `results` list.
    print('\n'.join(results))
    #This is printed: the results of calling func_1(n, row1, row2) for each iteration, each result on a new line
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n`, followed by two strings `row1` and `row2`. It then calls `func_1(n, row1, row2)` to compute a result based on the comparison of `row1` and `row2`. Finally, it collects all these results into a list and prints them, each on a new line.

