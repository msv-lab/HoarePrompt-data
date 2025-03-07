#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: Output State: The output state will consist of a series of characters printed for each iteration of the outer loop. For each iteration, three characters will be printed based on the value of `lex` after processing through the inner loops. If `lex` is less than or equal to 26, it will be replaced by 1, otherwise, it will be replaced by 26, and then sorted before converting to characters using `chr(arr[k] + 96)`. The exact characters depend on the initial value of `lex` for each case.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it reads an integer `lex` and transforms it based on certain conditions. Specifically, if `lex` is less than or equal to 26, it replaces `lex` with 1; otherwise, it replaces `lex` with 26. After processing, it sorts the transformed values and prints the first three characters corresponding to these values, converted to lowercase letters. The function does not return any value but outputs the processed characters for each test case.

