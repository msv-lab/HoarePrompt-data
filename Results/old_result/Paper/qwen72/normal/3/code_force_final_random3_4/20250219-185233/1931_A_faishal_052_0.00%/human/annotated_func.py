#State of the program right berfore the function call: The function should take an integer t (1 ≤ t ≤ 100) representing the number of test cases, and for each test case, an integer n (3 ≤ n ≤ 78) representing the encoded word.
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
        
    #State: `cases` is 0, `i` is `cases - 1`, `j` is 2, `k` is 3, `range` is 3, `lex` is an input integer, and `arr` is a sorted list with elements appended based on the value of `lex` for each iteration.
#Overall this is what the function does:The function `func` reads an integer `cases` from the input, representing the number of test cases. For each test case, it reads another integer `lex` from the input, processes it to generate a list `arr` with up to 3 elements based on the value of `lex`, sorts `arr`, and then prints the corresponding lowercase letters (based on the ASCII values of the elements in `arr` plus 96) for each of the 3 elements. The function does not return any value; it only prints the decoded words for each test case. After the function concludes, `cases` is 0, and the state of other variables (`i`, `j`, `k`, `lex`, `arr`) is undefined as they are local to the function and reset for each test case.

