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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of length n consisting of '.', '@', and '*' characters, where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. The variable `ret` is the number of coins collected before encountering two consecutive cells with thorns ('*'). If two consecutive thorns are encountered, the loop breaks and no more coins are counted for that test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a string of length up to 50 containing '.', '@', and '*' characters. It counts the number of '@' (coins) characters in the string until it encounters two consecutive '*' (thorns) characters, at which point it stops counting. The function outputs the count of coins for each test case.

