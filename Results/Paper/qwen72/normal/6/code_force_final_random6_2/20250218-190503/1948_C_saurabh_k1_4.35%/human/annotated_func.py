#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an even integer such that 2 ≤ n ≤ 2·10^5, and the sum of n over all test cases does not exceed 2·10^5. The function receives a list of test cases, where each test case is a tuple containing an integer n and two strings of length n, each consisting of characters '<' and '>', representing the arrows in the first and second rows of the grid, respectively.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer greater than 0, the sum of `n` over all test cases does not exceed 2·10^5, the function receives a list of test cases, where each test case is a tuple containing an integer `n` and two strings of length `n`, each consisting of characters '<' and '>', `_` is incremented by 1 for each test case where the second-to-last character of `b` is not '<', otherwise `_` remains unchanged for that test case.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of an even integer `n` and two strings of length `n` containing characters '<' and '>'. For each test case, the function checks if the second-to-last character of the second string `b` is '<'. If it is, the function prints 'No'; otherwise, it prints 'Yes'. The function does not return any value. After all test cases are processed, the state of the program remains as it was before the function call, except that the output has been printed to the standard output for each test case.

