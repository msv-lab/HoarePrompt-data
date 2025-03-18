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
        
    #State: `info` is a list of lists, where each inner list contains three integers sorted in ascending order, representing the processed values for each test case.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: info is a list of lists, where each inner list contains three integers sorted in ascending order, representing the processed values for each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each of the `t` test cases, it reads an integer `n` (3 <= n <= 78). It then computes a string of three characters corresponding to the values derived from `n` and prints this string for each test case.

