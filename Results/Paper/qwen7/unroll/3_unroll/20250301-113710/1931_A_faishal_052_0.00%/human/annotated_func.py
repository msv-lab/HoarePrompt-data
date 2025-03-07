#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: Output State: The output state will consist of three lowercase letters printed for each iteration of the outer loop, based on the value of `lex` after processing. Specifically, the first two characters will always be 'a' (1 in the array) and 'z' (26 in the array), and the third character will be the result of `lex % 26` converted to a lowercase letter, plus 'a'. This process is repeated for each case provided by the user.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it reads two values: `cases` (the number of test cases) and `lex` (an integer). For each test case, it calculates and prints three lowercase letters. The first two letters are always 'a' and 'z', and the third letter is determined by the value of `lex % 26`, converted to a corresponding lowercase letter. The function does not return any value but outputs the calculated letters for each test case.

