#State of the program right berfore the function call: The function `func` is expected to take an integer `n` as input, where 3 ≤ n ≤ 78, representing the encoded sum of the positions of three lowercase Latin letters.
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
        
    #State: `cases` is 0, `i` is `cases` - 1, `j` is 2, `k` is 3, `lex` is an input integer, and `arr` is [1, 1, `lex`] if `lex` is less than or equal to 26, [1, 26, `lex` - 26] if `lex` is between 27 and 51 (inclusive), or [26, 26, `lex` - 51] if `lex` is greater than or equal to 52.
#Overall this is what the function does:The function `func` reads an integer `cases` from the input, representing the number of test cases. For each test case, it reads another integer `lex` (3 ≤ lex ≤ 78) from the input, which is the encoded sum of the positions of three lowercase Latin letters. The function then calculates and prints a string of three lowercase Latin letters whose positions sum up to `lex`. The letters are sorted in non-decreasing order of their positions. After processing all test cases, the function terminates, and the variables `cases`, `i`, `j`, `k`, and `lex` are in their final states as described in the annotations.

