#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, n is an integer such that 3 <= n <= 78.
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
        
    #State: Concatenation of three characters for each test case, where each character is determined by the adjusted `lex` value after processing each test case.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer `lex` (3 <= lex <= 78). For each test case, it determines three characters based on the value of `lex` and prints these characters concatenated together. The characters are derived from the English alphabet, with the value of `lex` being adjusted to map to specific letters.

