#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of n characters consisting only of '.', '@', and '*', where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. Additionally, the first cell is guaranteed to be empty ('.') and does not contain thorns.
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
        
    #State: All characters in the list `s` have been processed, `thorn` is either 0 or 2 depending on whether any '*' characters were encountered, `ret` is the total count of '@' characters found in the list `s`, and `i` does not exist since the loop has completed all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string of characters representing a row in a grid. For each test case, it counts the number of cells containing a coin ('@'), stopping the count if two consecutive thorn ('*') cells are encountered. It prints the count of coins for each test case and returns nothing.

