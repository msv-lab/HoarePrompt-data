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
        
    #State: `info` is a list containing `cases` number of sorted arrays `arr`, where each `arr` is constructed based on the input `lex` values read during each iteration of the loop.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: `info` is a list containing `cases` number of sorted arrays `arr`; `temp` is a string containing the characters `chr(info[cases-1][0] + 96)`, `chr(info[cases-1][1] + 96)`, and `chr(info[cases-1][2] + 96)`; `j` is 2; `i` is `cases - 1`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `lex` (where 3 ≤ lex ≤ 78), and outputs a string of three characters derived from the processed value of `lex`. For each test case, the function calculates a sequence of numbers based on the value of `lex`, sorts them, and then converts the first three numbers of the sorted sequence into lowercase alphabetic characters by adding 96 to each number and converting to ASCII. The resulting strings are printed one per line.

