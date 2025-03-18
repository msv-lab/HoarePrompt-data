#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples where each tuple contains an integer n (1 ≤ n ≤ 50) and a string of n characters ('.', '@', '*') representing the path. The first character of each string is always '.'.
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
        
    #State: After the loop executes all iterations, `s` remains a list of characters from the input string. `ret` is the number of times the character `@` appeared in the string before the second occurrence of `*`. `thorn` is 2 if the second `*` was encountered, otherwise it is 0. `i` is the last character processed in the loop, which could be any character from the string. `_` is incremented by the number of iterations the loop ran, which is equal to the number of characters processed before the loop broke or completed. `len` remains the integer value of the input string.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a string `s` of `n` characters from the input. The function then counts the number of occurrences of the character `@` in the string `s` before the second occurrence of the character `*`. If the second `*` is encountered, the counting stops. The function prints the count for each test case. The function does not return any value. After the function concludes, the input strings are processed, and the counts are printed for each test case. The final state of the program includes the printed counts and the input variables remain as they were read from the input.

