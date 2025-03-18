#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is a positive integer such that 1 ≤ n ≤ 50, and the second line of input is a string of n characters consisting only of '.', '@', and '*', where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. Additionally, the first cell is guaranteed to be empty ('.') and does not contain thorns.
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
        
    #State: Output State: After the loop executes all its iterations, the variable `ret` will contain the total count of '@' characters encountered in the string `s`. The variable `thorn` will be 0, as the loop breaks when `thorn` reaches 2, resetting it back to 0. The variable `i` will be the last character processed in the string `s`, and `len` will be the length of the final string `s` after any necessary adjustments within the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( n \) and a string of \( n \) characters ('.', '@', '*'). For each test case, it counts the number of '@' characters in the string, breaking the count if two consecutive '*' characters are encountered. The function outputs the count for each test case.

