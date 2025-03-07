#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: The output state is a sequence of characters derived from the values in `arr` after sorting and converting to letters for each iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `lex` and performs calculations to derive three characters. These characters are then printed in sorted order. The characters are determined based on the value of `lex`, with values up to 26 corresponding to letters 'a' to 'z', and values above 26 being adjusted accordingly.

