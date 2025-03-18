#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an even integer such that 2 ≤ n ≤ 2 \cdot 10^5. The first row and the second row of the grid are strings of length n consisting of '<' and '>' characters. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: After executing the loop, the variable `t` remains unchanged as it represents the number of test cases. For each test case, the program prints either 'Yes' or 'No' based on the condition `if b[n - 2] == '<'`. The output is a series of 'Yes' or 'No' responses, one for each test case, with no changes to the initial state of `t`, `n`, `a`, or `b` outside of the loop iterations.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an even integer `n` and two strings of length `n` composed of '<' and '>' characters. For each test case, it checks the second last character of the second string and prints 'No' if it is '<', otherwise it prints 'Yes'. The function does not modify the input values and outputs a series of 'Yes' or 'No' responses, one for each test case.

