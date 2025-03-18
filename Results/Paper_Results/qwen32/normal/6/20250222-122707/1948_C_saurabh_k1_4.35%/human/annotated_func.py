#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an even integer such that 2 ≤ n ≤ 2 \cdot 10^5, and the sum of n over all test cases does not exceed 2 \cdot 10^5. Each of the two strings representing the rows of the grid consists of exactly n characters, where each character is either '<' or '>'. There are no arrows pointing outside the grid.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: t is 0, and the outputs for each of the t test cases have been printed ("No" or "Yes" based on the condition `b[n - 2] == '<'`).
#Overall this is what the function does:The function processes multiple test cases where each test case consists of two strings of equal even length, containing only '<' and '>'. It checks the second-to-last character of the second string and prints "No" if it is '<', otherwise it prints "Yes".

