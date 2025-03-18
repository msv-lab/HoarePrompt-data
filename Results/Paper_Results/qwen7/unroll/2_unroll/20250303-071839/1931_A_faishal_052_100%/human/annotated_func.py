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
        
    #State: Output State: `info` is a list containing up to 100 lists. Each inner list contains four elements: two integers between 1 and 26 inclusive, followed by either 1 or 26, and finally an integer between 0 and 78 inclusive. The last element in each inner list is sorted.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: For each list in `info`, the program prints a string formed by converting the first three integers (between 1 and 26) to their corresponding lowercase letters (using `chr(info[i][j] + 96)`), concatenating them together, and then printing the resulting string.
#Overall this is what the function does:The function reads multiple test cases, where each case involves an integer `lex`. It processes `lex` based on its value, sorts a list containing processed values, and converts the first three elements of each processed list into corresponding lowercase letters. Finally, it prints these letter strings for each test case.

