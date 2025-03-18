#State of the program right berfore the function call: The function `func` is expected to read input from stdin where the first line is an integer t (1 ≤ t ≤ 100) representing the number of test cases, followed by t lines each containing an integer n (3 ≤ n ≤ 78) representing the encoded word.
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
        
    #State: After all iterations of the loop, `cases` will have its original value (as it is not modified within the loop), `i` will be equal to `cases` (indicating the loop has completed all iterations), `j` will be 2 (the last value it reaches in the inner loop), `lex` will be the last input integer processed (unchanged from its final modification), and `info` will contain a list of lists, each corresponding to one of the `cases` inputs, structured as follows: For each input `lex`, if `lex` is less than 28, the list will be `[1, 1, 1, lex - 3]`; if `lex` is between 28 and 51 (inclusive), the list will be `[1, 1, lex - 27, 26]`; if `lex` is between 52 and 78 (inclusive), the list will be `[26, 26, 26, lex - 78]`. Each list in `info` is sorted in ascending order.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: After all iterations of the loop, `cases` remains unchanged, `i` equals `cases` (indicating the loop has completed all iterations), `j` is 3 (the last value it reaches in the inner loop), `lex` is the last input integer processed, and `info` contains a list of lists, each corresponding to one of the `cases` inputs. The structure of each list in `info` is determined by the value of `lex`: if `lex` is less than 28, the list is `[1, 1, 1, lex - 3]`; if `lex` is between 28 and 51 (inclusive), the list is `[1, 1, lex - 27, 26]`; if `lex` is between 52 and 78 (inclusive), the list is `[26, 26, 26, lex - 78]`. Each list in `info` is sorted in ascending order. The variable `temp` is the string formed by concatenating the characters corresponding to the ASCII values of `info[cases-1][0] + 96`, `info[cases-1][1] + 96`, and `info[cases-1][2] + 96`.
#Overall this is what the function does:The function `func` reads an integer `t` from standard input, representing the number of test cases. For each of the next `t` lines, it reads an integer `n` (where 3 ≤ n ≤ 78) and processes it to generate a list of integers based on specific conditions. It then sorts these lists and constructs a string from the first three elements of each list by converting them to their corresponding lowercase letters (using ASCII values). Finally, it prints these strings to standard output, one per line. The function does not return any value; it only prints the results.

