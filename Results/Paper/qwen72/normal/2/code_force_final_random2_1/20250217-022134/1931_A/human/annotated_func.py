#State of the program right berfore the function call: The function should accept an integer `n` as input, where 3 ≤ n ≤ 78, representing the encoded value of a three-letter word.
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
        
    #State: After all iterations of the loop, `n` is an integer where 3 ≤ n ≤ 78, `cases` is the initial input integer, `info` is a list containing `cases` sublists, each sublist being a sorted list of three integers representing the values of `lex` after processing, and `lex` is the remaining value after the last iteration. The variables `i` and `j` are not relevant outside the loop context.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: `n` is an integer where 3 ≤ n ≤ 78, `cases` is the initial input integer, `info` is a list containing `cases` sublists, each sublist being a sorted list of three integers, `lex` is the remaining value after the last iteration, `i` is `cases - 1`, `temp` is now a string containing the characters corresponding to the ASCII values of `info[cases-1][0] + 96`, `info[cases-1][1] + 96`, and `info[cases-1][2] + 96`, `j` is 2.
#Overall this is what the function does:The function reads an integer `cases` indicating the number of test cases. For each test case, it reads an integer `lex` (3 ≤ lex ≤ 78) representing an encoded value of a three-letter word. It processes `lex` to determine the corresponding three-letter word by breaking it down into three parts, sorting these parts, and converting them to their respective characters. Finally, it prints the three-letter word for each test case. The function does not return any value; it only prints the results.

