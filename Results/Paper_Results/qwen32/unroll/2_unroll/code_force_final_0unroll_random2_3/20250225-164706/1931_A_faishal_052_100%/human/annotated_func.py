#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` is an integer such that 3 <= n <= 78, `cases` is an input integer, `info` is a list of `cases` number of sorted lists, each containing 3 integers derived from the values of `lex` as described.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: The output state is the same as the initial state for `t`, `n`, `cases`, and `info`. Additionally, the loop will print `cases` number of strings, each consisting of 3 characters derived from the integers in the corresponding list in `info`.
#Overall this is what the function does:The function reads an integer `cases` representing the number of test cases. For each test case, it reads an integer `lex` and processes it to derive three integers. These integers are then converted to characters (assuming a 1-based index for letters 'a' to 'z') and printed as a string of three characters.

