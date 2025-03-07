#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 3 <= n <= 78.
def func():
    cases = int(input())
    for i in range(cases):
        arr = []
        
        lex = int(input())
        
        for j in range(2):
            if lex <= 26:
                arr.append(1)
                lex = lex - 1
            elif lex < 52:
                arr.append(26)
                lex = lex - 26
            else:
                arr.append(26)
                lex = lex - 26
        
        arr.append(lex)
        
        arr.sort()
        
        for k in range(3):
            print(chr(arr[k] + 96), end='')
        
    #State: The output state consists of three characters for each of the `cases` iterations, derived from the sorted values in `arr` after processing each `lex` input. The values of `t` and `n` remain unchanged.
#Overall this is what the function does:The function reads an integer `cases` representing the number of test cases. For each test case, it reads another integer `lex` and processes it to produce three characters as output. The output for each test case consists of three characters derived from the values in a sorted array `arr` after processing `lex`. The values of `cases` and `lex` remain unchanged after the function execution.

