#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: Output State: After the loop executes all its iterations, `arr` will contain the elements `[1, 26, 26, lex - 2]` or `[1, 26, 26, lex - 27]`, depending on the value of `lex` after the last iteration, and `arr` will be sorted in ascending order. `info` will be a list containing the final state of `arr` after sorting for each iteration.
    #
    #This means that for each case (`i` in `range(cases)`), the loop constructs an array `arr` based on the value of `lex`, appends `lex` to `arr`, sorts `arr`, and then adds it to the `info` list. After all cases have been processed, `info` will contain a list of lists, where each inner list represents the final state of `arr` for each respective case, sorted in ascending order.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: `i` is 2, `j` is 3, `cases` must be a positive integer, `temp` is a string containing the character corresponding to `chr(info[2][3] + 96)` repeated three times, and `info` contains a list of lists where each inner list represents the final state of `arr` after sorting for each respective case.
#Overall this is what the function does:The function reads multiple test cases, where each case involves an integer `lex`. For each `lex`, it constructs an array `arr` based on certain conditions, appends `lex` to `arr`, sorts `arr`, and stores the result in a list `info`. Finally, it prints a string composed of characters corresponding to the first three elements of the sorted array for each case.

