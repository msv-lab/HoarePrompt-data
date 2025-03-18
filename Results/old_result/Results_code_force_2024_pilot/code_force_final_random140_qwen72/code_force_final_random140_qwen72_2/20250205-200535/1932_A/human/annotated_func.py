#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 50, representing the length of the path. The path is represented by a string of n characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first cell of the path is always empty ('.').
def func():
    for _ in range(int(input())):
        len = int(input())
        
        s = list(input())
        
        ret = 0
        
        thorn = 0
        
        for i in s:
            if i == '@':
                thorn = 0
                ret += 1
            elif i == '*':
                thorn += 1
                if thorn == 2:
                    break
            else:
                thorn = 0
        
        print(ret)
        
    #State: _ is t-1, t is an integer where 1 ≤ t ≤ 1000, len is an input integer, s is a list of characters from the input string, ret is the number of '@' characters encountered before the second consecutive '*' character (or the end of the list), thorn is 0 if the loop did not encounter two consecutive '*' characters, otherwise thorn is 2.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a string of length `n` representing a path. The path consists of characters '.', '@', and '*', denoting empty cells, coins, and thorns, respectively. The function counts the number of coins ('@') encountered in the path until it encounters two consecutive thorns ('*'). If two consecutive thorns are found, the counting stops. The function prints the count of coins for each test case. After processing all test cases, the function completes, and the final state includes the printed results for each test case.

