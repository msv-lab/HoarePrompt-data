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
        
    #State: Output State: After the loop executes all its iterations, `i` will range from 0 to `cases-1`, meaning it will take on every integer value within that range exactly once. `cases` remains an integer such that \(1 \leq \text{cases} \leq 100\). The variable `arr` will contain a list of integers where each list represents the processed values of `lex` for a particular test case, with `lex` being reduced by either 2, 26, or 52 based on the conditions specified in the loop. Each `arr` list will be sorted. The variable `lex` will hold the final value after processing for each test case, which is appended to `arr`. The `info` list will contain all the `arr` lists generated for each test case, sorted as per the loop's operation.
    #
    #In summary, `info` will be a list of lists, where each inner list represents the processed values of `lex` for a specific test case, sorted according to the operations performed in the loop.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: Output State: `temp` is 'aamo', `i` is 4, `j` is 3, `cases` is 3.
    #
    #Explanation: After analyzing the loop and the given states, we can conclude that the loop runs exactly 3 times. The variable `i` remains at 4 because it is not incremented within the loop body. The variable `j` reaches 3 after 3 iterations. The variable `temp` concatenates characters derived from `info[i][j] + 96`, resulting in the string 'aamo'. Since the loop runs exactly 3 times, `cases` must be 3, and there are no further iterations to consider. Thus, the final output state after all iterations of the loop have finished is `temp` being 'aamo', `i` remaining 4, `j` at 3, and `cases` being 3.
#Overall this is what the function does:The function reads multiple test cases, each containing an integer `lex` ranging from 28 to 78. For each test case, it processes `lex` by subtracting 2, 26, or 52 based on certain conditions, sorts the resulting values, and appends the final value of `lex` to the list. It then constructs a string from the first three elements of each processed list and prints these strings. The function does not return any value but prints the constructed strings for each test case.

