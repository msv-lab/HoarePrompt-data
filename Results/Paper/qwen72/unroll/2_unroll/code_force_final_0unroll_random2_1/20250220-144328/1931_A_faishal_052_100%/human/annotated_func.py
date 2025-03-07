#State of the program right berfore the function call: The function `func` is expected to take an integer `n` as input, where 3 ≤ n ≤ 78, representing the encoded sum of the positions of three lowercase Latin letters.
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
        
    #State: The `info` list contains `cases` sublists, each with three integers representing the positions of the letters after decoding. Each sublist is sorted in ascending order. The function `func` and the variable `cases` remain unchanged.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: The `info` list remains the same, containing `cases` sublists, each with three integers representing the positions of the letters after decoding. Each sublist is sorted in ascending order. The `cases` variable also remains unchanged. The loop prints the decoded strings for each sublist.
#Overall this is what the function does:The function `func` reads an integer `cases` from the input, representing the number of test cases. For each test case, it reads another integer `lex` (where 3 ≤ lex ≤ 78) and decodes it into three lowercase Latin letters whose positions sum up to `lex`. The decoded letters are printed in ascending order of their positions. The function does not return any value; it only prints the decoded strings for each test case. After the function concludes, the `info` list contains `cases` sublists, each with three integers representing the positions of the decoded letters, and each sublist is sorted in ascending order. The `cases` variable remains unchanged.

