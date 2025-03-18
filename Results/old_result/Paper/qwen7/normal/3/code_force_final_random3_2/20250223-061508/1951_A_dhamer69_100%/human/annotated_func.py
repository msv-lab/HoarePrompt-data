#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end are valid indices for directory names in the current working directory.
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
        
    #State: Output State: `start` is an integer, `end` is an integer, `t` is 0, `n` is an input integer, `s` is the input string from the user after the last iteration of the loop.
    #
    #Explanation: After the loop has executed all its iterations, the variable `t` starts at `start` and decreases by 1 each time through the loop. Since the loop continues as long as `t > 0`, once `t` reaches 0, the loop terminates. Therefore, after all iterations, `t` will be 0. The values of `start`, `end`, `n`, and `s` will retain their final values from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple inputs consisting of integers and strings. It iterates `t` times, where `t` is initially set to an integer value read from input. During each iteration, it reads two integers `n` and a string `s`. If `n` equals 2, it checks if `s` is '00'. If so, it prints 'YES', otherwise 'NO'. For other values of `n`, it counts the number of '1's in `s` and checks specific conditions related to the count and consecutive '1's. Based on these conditions, it prints either 'YES' or 'NO'. After processing all `t` inputs, the function outputs the final values of `t`, `n`, and `s` from the last iteration, while `t` is guaranteed to be 0.

