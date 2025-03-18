#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: Output State: The output state will consist of three lowercase letters printed for each iteration of the outer loop, based on the value of `lex` after processing. Specifically, the first two characters will always be 'a' and 'z', and the third character will be a letter corresponding to the remaining value of `lex` after it has been reduced by multiples of 26. This process is repeated `cases` times.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it reads an integer `lex` and calculates a sequence of characters. It then prints three characters for each test case: 'a', 'z', and a character corresponding to the remaining value of `lex` after it has been reduced by multiples of 26. This process is repeated for the number of test cases specified by the user.

