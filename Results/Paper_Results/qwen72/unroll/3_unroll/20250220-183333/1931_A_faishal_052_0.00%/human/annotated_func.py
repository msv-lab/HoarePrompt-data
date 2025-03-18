#State of the program right berfore the function call: The function should accept an integer n such that 3 ≤ n ≤ 78, representing the encoded sum of the positions of three lowercase Latin letters.
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
        
    #State: For each of the `cases` iterations, the output will be a string of three lowercase Latin letters, where the letters are determined by the sorted values in `arr` after processing `lex`.
#Overall this is what the function does:The function reads an integer `cases` from the input, representing the number of test cases. For each test case, it reads another integer `lex` (3 ≤ lex ≤ 78) from the input, processes it to generate a list `arr` of three integers, sorts this list, and then prints a string of three lowercase Latin letters corresponding to the sorted values in `arr`. The letters are determined by the positions in the alphabet (1 for 'a', 2 for 'b', etc.). The function does not return any value; it only prints the results.

