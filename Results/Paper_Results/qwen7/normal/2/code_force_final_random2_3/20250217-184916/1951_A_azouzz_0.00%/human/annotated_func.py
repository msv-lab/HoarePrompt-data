#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names without leading or trailing spaces.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2 and (cnt1 % 2 == 1 or cnt1 == 1):
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: The final state after the loop executes all its iterations will have the following characteristics:
    #
    #- `start` is an integer, `end` is an integer such that `start` <= `end`.
    #- `t` is the input integer that was initially provided and has been decremented by the number of times the loop ran until it reaches 0.
    #- `n` is the last input integer received during the loop's execution.
    #- `s` is the last input string received during the loop's execution.
    #- `cnt1` is the count of '1' in the last input string `s`.
    #
    #In this final state, the value of `t` will be 0 because the loop runs for `t` times and `t` is decremented by 1 each iteration until it reaches 0. The values of `n` and `s` will be the inputs received during the last iteration of the loop. The variable `cnt1` will hold the count of '1' in the string `s` from the last iteration. The `start` and `end` values will remain as they were initialized since they are not affected by the loop.
#Overall this is what the function does:The function reads multiple test cases where each case consists of an integer `n` followed by a binary string `s`. It checks if the string `s` meets certain conditions: if the count of '1's is greater than 2 and even, it prints 'YES'; if the count of '1's is greater than 2 and odd, or if '11' is a substring of `s`, it prints 'NO'; otherwise, it also prints 'YES'. After processing all test cases, the function outputs the results for each case and returns nothing.

