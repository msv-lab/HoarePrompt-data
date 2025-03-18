#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, n is an integer such that 3 <= n <= 78.
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
        
    #State: `info` is a list containing `cases` number of lists, each of which has three sorted elements representing the processed values of `lex` for each test case.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: the printed strings for each test case, which are the concatenated characters derived from the elements of each list in `info`.
#Overall this is what the function does:The function processes a number of test cases, each with an integer input `lex` between 3 and 78. For each test case, it calculates a list of three values based on the value of `lex`, sorts this list, and then converts these values into characters by mapping them to the ASCII range of lowercase letters ('a' to 'z'). The function prints a string of these three characters for each test case.

