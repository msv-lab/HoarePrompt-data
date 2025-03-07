#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: Output State: The loop has executed all its iterations, printing 'a', 'b', and 'c' in sequence.
    #
    #Explanation: Given the loop runs three times as specified by `range(3)`, and each iteration processes the value of `lex` to form an array `arr` which is then sorted and printed. Regardless of the initial value of `lex` (as long as it's within the given constraints), the final sorted array `arr` will always be `[1, 26, lex]` after the operations inside the loop. When sorted, this array becomes `[1, 26, lex]` (assuming `lex` is less than or equal to 26). Converting these values to characters using `chr(arr[k] + 96)` results in 'a', 'b', and 'c'. Therefore, after all iterations, the loop prints 'a', 'b', and 'c' in sequence.
#Overall this is what the function does:The function processes a series of test cases, each involving an integer `lex`. For each test case, it calculates a sequence of values based on `lex` and prints the first three characters of the resulting sequence. Specifically, it converts the calculated values into characters 'a', 'b', and 'c' and outputs them in that order. The function accepts no parameters and does not return any value; instead, it directly prints the output.

