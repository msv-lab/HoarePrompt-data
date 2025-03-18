#State of the program right berfore the function call: The function `func` does not take any input parameters, but it is expected to read input from stdin where the first line is an integer `t` (1 ≤ t ≤ 32) representing the number of test cases, followed by `t` lines, each containing a string of length 5 consisting of letters 'A' and 'B'. All `t` strings are distinct.
def func():
    t = int(input())
    for q in range(t):
        ac = 0
        
        bc = 0
        
        s = input()
        
        for i in s:
            if i == 'A':
                ac += 1
            else:
                bc += 1
        
        if ac > bc:
            print('A')
        else:
            print('B')
        
    #State: The loop will have printed 'A' or 'B' for each of the `t` test cases, depending on whether the count of 'A' characters in the string is greater than the count of 'B' characters. The variables `ac` and `bc` will be reset to 0 for each test case, and `q` will have iterated from 0 to `t-1`. The value of `t` remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from standard input, representing the number of test cases. It then reads `t` distinct strings of length 5, each consisting of the characters 'A' and 'B'. For each string, the function counts the number of 'A' and 'B' characters. If the count of 'A' characters is greater than the count of 'B' characters, it prints 'A'; otherwise, it prints 'B'. The function does not return any value, but it prints the result for each test case to standard output. After the function concludes, the value of `t` remains unchanged, and the state of the program is as it was before the function call, except for the printed results.

