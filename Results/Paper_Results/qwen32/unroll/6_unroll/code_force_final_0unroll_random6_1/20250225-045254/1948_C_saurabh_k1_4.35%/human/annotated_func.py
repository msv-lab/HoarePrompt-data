#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4; for each test case, n is an even integer such that 2 <= n <= 2 * 10^5; the first and second lines of each test case are strings of length n consisting of the characters '<' and '>', representing the directions of the arrows in the first and second row of the grid, respectively; the sum of n over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: For each test case, the output will be 'No' if the second last character of the second string (b[n - 2]) is '<'; otherwise, the output will be 'Yes'. The variables t, n, a, and b will reflect the last test case's values after the loop finishes executing.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an even integer `n` and two strings of length `n` made up of '<' and '>' characters. For each test case, it outputs 'No' if the second last character of the second string is '<', otherwise it outputs 'Yes'.

