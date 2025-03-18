#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end.
def func():
    t = int(input())
    while t > 0:
        n = int(input())
        
        s = input()
        
        if n == 2:
            if s == '00':
                print('YES')
            else:
                print('NO')
        else:
            count_1 = s.count('1')
            if count_1 % 2 != 0:
                print('NO')
            elif s.count('11') == 1 and count_1 == 2:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: `start` and `end` are integers such that 0 <= `start` <= `end`, `t` is 0, and the loop has executed `t` times. For each execution, `n` was an input integer, and `s` was an input string. If `n` was 2, the program checked if `s` was '00' and printed 'YES' if true, otherwise 'NO'. If `n` was not 2, the program counted the number of '1's in `s` (`count_1`). If `count_1` was odd, it printed 'NO'. If `count_1` was even and `s` contained exactly one '11' and exactly two '1's, it printed 'NO'. Otherwise, it printed 'YES'.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a string `s` from the input. The function checks if the string `s` meets certain conditions based on the value of `n` and prints 'YES' or 'NO' accordingly. Specifically, if `n` is 2, it prints 'YES' if `s` is '00', otherwise 'NO'. If `n` is not 2, it prints 'NO' if the number of '1's in `s` is odd, or if there is exactly one occurrence of '11' and exactly two '1's in `s`. Otherwise, it prints 'YES'. After processing all test cases, the function terminates with `t` being 0.

