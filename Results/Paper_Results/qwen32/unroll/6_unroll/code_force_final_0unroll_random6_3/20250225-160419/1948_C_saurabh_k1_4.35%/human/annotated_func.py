#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of an integer n such that 2 <= n <= 2 \cdot 10^5 and n is even, followed by two strings each of length n consisting of characters '<' and/or '>'. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: The output state consists of t lines, each containing either 'Yes' or 'No' based on the condition that if the second last character of the second string (b) is '<', it prints 'No'; otherwise, it prints 'Yes'. The values of t, n, a, and b are not preserved after the loop execution, but t lines of output are produced as per the described logic.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and two strings of length `n` containing only '<' and '>'. For each test case, it checks if the second last character of the second string is '<'. If it is, the function outputs 'No'; otherwise, it outputs 'Yes'.

