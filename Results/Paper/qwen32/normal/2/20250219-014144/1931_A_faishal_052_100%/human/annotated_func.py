#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: `info` contains `cases` number of sorted arrays, each generated based on the corresponding `lex` value; `t` and `n` remain unchanged; `cases` remains unchanged; `i` equals `cases`.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: `info` contains `cases` number of sorted arrays, each generated based on the corresponding `lex` value; `t` and `n` remain unchanged; `cases` remains unchanged; `i` equals `cases`.
#Overall this is what the function does:The function reads an integer `cases` representing the number of test cases. For each test case, it reads an integer `lex` and generates a string of three characters based on the value of `lex`. It then prints these strings. The values of `t` and `n` mentioned in the annotations are not parameters of the function and do not affect its behavior.

