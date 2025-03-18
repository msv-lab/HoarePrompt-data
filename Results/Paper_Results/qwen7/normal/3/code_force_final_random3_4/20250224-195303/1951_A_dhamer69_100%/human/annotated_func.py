#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end represent valid directory names without leading zeros.
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
        
    #State: Output State: `t` is equal to `t - 3`, `n` is an input integer, `s` is an input string, and `count_1` is the number of times '1' appears in `s`.
    #
    #After all iterations of the loop have finished, the variable `t` will be reduced by 3 (since the loop runs 3 times), and the values of `n` and `s` will be determined by the last iteration of the loop. The variable `count_1` will be the number of '1's in the string `s` provided in the last iteration. The conditions inside the loop will be evaluated based on these final values of `n` and `s`.
#Overall this is what the function does:The function processes multiple inputs where each input consists of an integer `n` and a string `s`. It checks specific conditions based on the value of `n` and the content of `s`. If `n` is 2 and `s` is '00', it prints 'YES'. For other values of `n`, it counts the number of '1's in `s`. If the count of '1's is odd or if there is exactly one occurrence of '11' and the count of '1's is 2, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value but prints 'YES' or 'NO' based on the conditions checked.

