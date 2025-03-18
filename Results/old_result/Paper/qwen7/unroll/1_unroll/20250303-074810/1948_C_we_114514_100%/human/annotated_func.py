#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, row1 is a string consisting of exactly n characters '<' and/or '>', and row2 is a string consisting of exactly n characters '<' and/or '>'. Additionally, n is even, and there are no arrows pointing outside the grid.
def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: The function returns 'No' if any condition inside the loop is met; otherwise, it does not return anything.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: The function does not return 'No', and either row1[n - 1] is not '<' or row2[n - 2] is not '<'
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `row1`, and `row2`. It checks if it's possible to pair each character in `row1` with a corresponding character in `row2` such that no two paired characters point at each other. If any invalid pairing is found, it returns 'No'; otherwise, it returns 'Yes'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even. row1 and row2 are strings consisting of exactly n characters, where each character is either '<' or '>'.
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
        
    #State: Output State: t is an integer equal to the input integer, n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even, row1 and row2 are strings consisting of exactly n characters, where each character is either '<' or '>', results is a list containing t elements, each element being the result of calling func_1(n, row1, row2) for each iteration of the loop.
    print('\n'.join(results))
    #This is printed: a series of lines, each line representing the return value of `func_1(n, row1, row2)`
#Overall this is what the function does:The function reads multiple test cases from standard input. For each test case, it takes an integer \( t \) (number of cases), an even integer \( n \) (length of two input strings), and two strings \( row1 \) and \( row2 \) of length \( n \) consisting of '<' and '>' characters. It then calls another function `func_1` for each test case, passing \( n \), \( row1 \), and \( row2 \) as arguments. After processing all test cases, it prints the results of these calls, one per line, to standard output.

