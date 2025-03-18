#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of n characters where each character is either '.', '@', or '*', representing an empty cell, a cell with a coin, and a cell with thorns, respectively, and the first character is always '.', indicating that the starting cell is empty.
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
        
    #State: `thorn` is either 0, 1, or 2, `ret` is the total number of '@' encountered across all iterations, and `i` is the last character processed in the last list `s`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string of `n` characters ('.', '@', '*'). It counts the number of '@' characters (cells with coins) in each string, breaking early if two consecutive '*' characters (cells with thorns) are found. For each test case, it prints the count of '@' characters. The final state of the program includes the printed counts for all test cases.

