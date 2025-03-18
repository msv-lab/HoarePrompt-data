#State of the program right berfore the function call: start and end are integers where start <= end, and they represent the range of subfolder names to be considered, which are expected to be numeric.
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
            elif s.count('11') == 1:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: `start` and `end` are integers where `start` <= `end`, `t` is 0, `n` is an input integer, and `s` is a new input string. The loop has completed all iterations, and the variables `start` and `end` remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user, representing the number of test cases. For each test case, it reads an integer `n` and a string `s` from the user. The function then checks if the string `s` meets certain conditions based on the value of `n`. If `n` is 2, it prints 'YES' if `s` is '00', otherwise it prints 'NO'. If `n` is greater than 2, it prints 'NO' if the count of '1' in `s` is odd or if there is exactly one occurrence of '11'. Otherwise, it prints 'YES'. After processing all test cases, the function concludes, and the variables `start` and `end` (if they exist) remain unchanged.

