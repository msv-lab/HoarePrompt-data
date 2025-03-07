#State of the program right berfore the function call: The function should accept an integer n as input, where 3 ≤ n ≤ 78, representing the encoded value of a three-letter word.
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
        
    #State: For each test case, the loop prints a three-character string where each character is determined by the sorted values in `arr` plus 96.
#Overall this is what the function does:The function reads an integer `cases` from the input, indicating the number of test cases. For each test case, it reads another integer `lex` (3 ≤ lex ≤ 78) representing the encoded value of a three-letter word. It then decodes this value into a three-character string, where each character is determined by the sorted values in an array `arr` plus 96. The function prints the decoded three-character string for each test case. The function does not return any value.

