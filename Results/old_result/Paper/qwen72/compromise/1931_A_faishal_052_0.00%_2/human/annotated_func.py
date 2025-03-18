#State of the program right berfore the function call: The function should accept an integer t (1 ≤ t ≤ 100) representing the number of test cases, and for each test case, an integer n (3 ≤ n ≤ 78) representing the encoded word.
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
        
    #State: `cases` is an integer between 1 and 100, `i` is `cases - 1`, `arr` is a sorted list with the first two elements being either 1 or 26, and the third element being the remaining value of `lex` after the loop's operations, `j` is 2, `k` is 3.
#Overall this is what the function does:The function `func` accepts an integer `t` (1 ≤ t ≤ 100) representing the number of test cases. For each test case, it reads an integer `n` (3 ≤ n ≤ 78) representing an encoded word. The function then decodes the word into a 3-character string, where the first two characters are either 'a' or 'z' and the third character is determined by the remaining value of `n` after the decoding process. The function prints the decoded string for each test case and does not return any value. After the function concludes, `cases` is an integer between 1 and 100, `i` is `cases - 1`, and the final state of the program includes the sorted list `arr` with the first two elements being either 1 or 26, and the third element being the remaining value of `n` after the loop's operations.

