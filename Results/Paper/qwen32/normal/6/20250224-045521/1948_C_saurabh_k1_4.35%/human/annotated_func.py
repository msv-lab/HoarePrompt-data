#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an even integer such that 2 <= n <= 2 * 10^5. The sum of n over all test cases does not exceed 2 * 10^5. Each of the two strings representing the rows of the grid consists of exactly n characters, where each character is either '<' or '>'. There are no arrows pointing outside the grid.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: t is 0, n is the last input integer, a is the list of characters from the last input string for the first row, b is the list of characters from the last input string for the second row. The program has printed 'No' if b[n - 2] was '<' for any of the test cases, otherwise it has printed 'Yes'.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two strings of equal even length `n` made up of '<' and '>' characters. For each test case, it checks if the second-to-last character of the second string is not '<'. If it is not, it prints "Yes", otherwise it prints "No".

