#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples where each tuple contains an integer n (1 ≤ n ≤ 50) and a string of n characters ('.', '@', '*') representing the path. The first character of each string is '.', indicating the starting cell is empty.
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
        
    #State: For each test case, the output state is the value of `ret` after the loop has finished executing. The value of `ret` is the number of times the character '@' appears in the string `s` before two consecutive '*' characters are encountered. If two consecutive '*' characters are found, the loop breaks, and the final value of `ret` is printed. The variables `len` and `s` are not affected by the loop and remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case consists of an integer `n` and a string `s` of `n` characters, where the first character is always '.'. The function counts the number of times the character '@' appears in the string `s` before encountering two consecutive '*' characters. If two consecutive '*' characters are found, the counting stops. The function prints the count for each test case. The variables `n` and `s` remain unchanged after processing each test case.

