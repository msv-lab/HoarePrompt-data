#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of length n consisting of '.', '@', and '*' characters, where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. Additionally, the first character of the string is always '.', indicating that the starting cell is empty.
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
                thorn == 0
        
        print(ret)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of length n consisting of '.', '@', and '*' characters, where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. The variable `ret` is the number of coins collected before encountering two consecutive thorns ('*'), and it is printed at the end of each test case. If two thorns are encountered consecutively, no more cells are processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer t and a string of length n containing '.', '@', and '*' characters. For each test case, it counts the number of '@' (coins) encountered before two consecutive '*' (thorns) are found. If two thorns are encountered, the counting stops. The function prints the count of coins for each test case.

