#State of the program right berfore the function call: The function should take an integer n as input where 3 ≤ n ≤ 78, representing the encoded sum of the positions of three lowercase Latin letters.
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
        
    #State: azzzzz
#Overall this is what the function does:The function reads an integer `cases` from the input, indicating the number of test cases. For each test case, it reads an integer `lex` (3 ≤ lex ≤ 78) from the input, which represents the encoded sum of the positions of three lowercase Latin letters. The function then calculates and prints three lowercase Latin letters whose positions sum up to `lex`. The letters are sorted in ascending order before printing. The function does not return any value.

