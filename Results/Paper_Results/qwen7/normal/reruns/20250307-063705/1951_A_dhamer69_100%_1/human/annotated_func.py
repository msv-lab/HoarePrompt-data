#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names without leading zeros.
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
        
    #State: Output State: `start` is an integer, `end` is an integer such that `start` <= `end`, `t` is equal to 0, `n` is an input integer from the user, `s` is a string input from the user, and `count_1` is the number of times '1' appears in the string `s`.
    #
    #After all iterations of the loop have finished, the variable `t` will be decremented until it reaches 0. At this point, the loop terminates, and the values of `n` and `s` will remain as they were during the last iteration of the loop. The variable `count_1` will also retain its value from the last iteration, which is the number of '1's in the string `s`. The values of `start` and `end` remain unchanged as they are not affected by the loop.
#Overall this is what the function does:The function processes multiple inputs where each input consists of an integer `n` and a string `s`. For each input, it checks specific conditions related to the string `s` (such as the presence of '1's and consecutive '11'). Based on these conditions, it prints either 'YES' or 'NO'. After processing all inputs, the function outputs nothing but modifies the internal state of variables like `t`, `n`, `s`, and `count_1` according to the loop iterations. The initial values of `start` and `end` remain unchanged throughout the function's execution.

