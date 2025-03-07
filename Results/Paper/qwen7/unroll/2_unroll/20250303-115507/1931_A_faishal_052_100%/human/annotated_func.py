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
        
    #State: Output State: `info` is a list containing 100 lists. Each inner list contains 3 elements: two numbers between 1 and 26 (inclusive) and one number between 0 and 78 (inclusive). The last element of each inner list is derived from the initial value of `lex` after applying the specified operations, and the first two elements are the result of the operations on `lex`. All values are sorted within each inner list.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: For each inner list in `info`, the output will be a string created by converting the first three integers to their corresponding lowercase letters (using `chr(info[i][j] + 96)`), concatenated together, and then printed. The fourth integer remains unchanged and is not part of the printed output.
#Overall this is what the function does:The function processes a series of test cases, where each case involves an integer \( n \) such that \( 3 \leq n \leq 78 \). For each case, it performs a series of operations on \( n \) and stores the results in a list. Specifically, it calculates two numbers based on \( n \) and appends them along with the modified \( n \) to a list. After processing all cases, it converts the first two numbers in each list to their corresponding lowercase letters and prints these letters as a string, while the third number is not printed. The function ultimately outputs a series of strings, each representing the processed values of \( n \) in a specific format.

