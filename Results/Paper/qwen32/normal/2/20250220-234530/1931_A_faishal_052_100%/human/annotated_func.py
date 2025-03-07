#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, there is an integer n such that 3 <= n <= 78.
def func():
    cases = int(input())
    info = []
    for i in range(cases):
        arr = []
        
        lex = int(input())
        
        for j in range(2):
            if lex < 28:
                arr.append(1)
                lex = lex - 1
            elif lex < 52:
                arr.append(26)
                lex = lex - 26
            elif lex <= 78:
                arr.append(26)
                lex = lex - 26
        
        arr.append(lex)
        
        arr.sort()
        
        info.append(arr)
        
    #State: `cases` is an integer such that 1 <= `cases` <= 100, `info` is a list containing `cases` sublists, where each sublist is a sorted list with up to three elements representing the final values of `arr` after processing each test case, and `lex` is adjusted based on the described rules for each test case.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: `cases` is an integer such that 1 <= `cases` <= 100, `info` is a list containing `cases` sublists, `lex` is adjusted based on the described rules for each test case, `temp` is a string containing the characters `chr(info[cases - 1][0] + 96)`, `chr(info[cases - 1][1] + 96)`, and `chr(info[cases - 1][2] + 96)`, `j` is 2, `i` is `cases`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` (where 3 <= n <= 78) and processes it to produce a string of three characters. The string is derived by converting specific values related to `n` into characters using ASCII values, and the function prints this string for each test case.

