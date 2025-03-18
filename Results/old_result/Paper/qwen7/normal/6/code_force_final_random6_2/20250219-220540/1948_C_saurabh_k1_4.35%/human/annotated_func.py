#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; the first line of each test case contains a string of length n consisting of characters '<' and/or '>'; the second line of each test case contains a string of length n consisting of characters '<' and/or '>'.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: Output State: The value of `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer input such that \(2 \leq n \leq 2 \cdot 10^5\) and `n` is even, `a` is a list of strings where each string is a character from the last input, and `b` is a list of strings where each string is a character from the last input. The string at index `n-2` in `b` is not '<'. The loop has executed for all test cases provided, and for each test case, if the condition `b[n-2] != '<'` was met, it printed 'Yes', otherwise it printed 'No'.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer n (2 ≤ n ≤ 2⋅10^5 and n is even) and two strings of length n consisting of characters '<' and/or '>'. For each test case, it checks if the second last character of the second string is not '<'. If true, it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, the function concludes without returning any value.

