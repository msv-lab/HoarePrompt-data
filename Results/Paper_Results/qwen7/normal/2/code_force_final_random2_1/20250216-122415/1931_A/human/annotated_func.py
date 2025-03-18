#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: Output State: `arr` is a sorted list of integers where the last element is `lex` and the rest of the elements are either 0 or 1, with the total count of 1s being equal to the number of cases. `j` is 1 for all sublists in `arr`. `info` is a list containing the results of all iterations, with each sublist sorted and having the same structure as described above. The length of `info` is equal to the value of `cases`.
    #
    #This means that after all iterations of the loop, `arr` will contain a series of lists, each sorted, with the last element being the final value of `lex` for that iteration, and the preceding elements being either 0s or 1s based on the logic inside the loop. The `info` list will hold all these results, maintaining the order of the iterations.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: `i` is 9, `cases` must be greater than 0, `temp` is a string consisting of the characters corresponding to the ASCII values of `info[8][4] + 96`, `j` is 5.
#Overall this is what the function does:The function reads a series of test cases, where each case involves an integer `lex` within a specific range. For each case, it processes `lex` according to certain conditions, sorts the resulting list, and appends it to a list of results. Finally, it prints a string derived from the first three elements of each processed list.

