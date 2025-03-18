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
            elif s.count('11') == 1:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: Output State: `n` is an input integer, `s` is a string input by the user, `count_1` is the number of times '1' appears in `s`; `t` is `0`.
    #
    #This means after the loop has executed all its iterations, the variable `t` will be `0` since it is decremented by `1` in each iteration until it reaches `0`. The values of `n` and `s` will be the last inputs provided by the user during the loop's final iteration, and `count_1` will be the count of '1's in the string `s` from that last iteration.
#Overall this is what the function does:The function processes multiple inputs where each input consists of an integer `n` and a string `s`. It checks specific conditions on `s` based on the value of `n`. If `n` is 2, it checks if `s` is exactly "00". For other values of `n`, it counts the number of '1's in `s` and checks if the count is odd or if there is only one occurrence of "11". Based on these conditions, it prints either "YES" or "NO". After processing all inputs, the function ensures that the counter `t` is set to 0.

