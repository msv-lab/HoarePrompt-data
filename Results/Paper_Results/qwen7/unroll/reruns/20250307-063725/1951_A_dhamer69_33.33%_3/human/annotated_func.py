#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names in the current working directory.
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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' printed based on the conditions checked within the loop for each iteration.
    #
    #Explanation: For each iteration of the loop, the value of `t` is decremented by 1 until it reaches 0. During each iteration, the program reads two inputs: an integer `n` and a string `s`. Based on these inputs, it prints either 'YES' or 'NO'. If `n` is 2 and `s` is '00', it prints 'YES'. Otherwise, it checks if the number of '1's in `s` is odd or if there is exactly one occurrence of '11'. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The output state will be a sequence of 'YES' and 'NO' printed during the loop's execution.
#Overall this is what the function does:The function processes multiple inputs consisting of an integer `n` and a string `s` for `t` iterations. It prints 'YES' or 'NO' based on specific conditions related to the values of `n` and the content of `s`. If `n` is 2 and `s` is '00', it prints 'YES'. Otherwise, it checks if the number of '1's in `s` is odd or if there is exactly one occurrence of '11'. If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value but outputs a series of 'YES' and 'NO' based on the given conditions.

