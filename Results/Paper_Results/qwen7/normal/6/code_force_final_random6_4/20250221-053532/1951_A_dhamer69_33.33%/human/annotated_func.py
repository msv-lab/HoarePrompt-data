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
        
    #State: Output State: `start` is an integer, `end` is an integer such that `start` <= `end`, `t` is equal to `0`, `n` is an input integer, `s` is an input string, and `count_1` is the number of '1's in the final input string `s`.
    #
    #Explanation: After all iterations of the loop have finished, the variable `t` will be decremented until it reaches `0`. At this point, the loop terminates. The values of `n` and `s` will reflect the last inputs provided during the loop's execution, and `count_1` will be the count of '1's in the final input string `s`. All other variables from the initial state remain unchanged.
#Overall this is what the function does:The function processes multiple inputs consisting of an integer `t`, followed by pairs of integers `n` and strings `s`. For each pair, it checks specific conditions related to the string `s` and prints either 'YES' or 'NO'. After processing all inputs, the function outputs the final state where `t` is 0, and the variables `n` and `s` reflect the last inputs provided. The function does not return any value but prints the results directly.

