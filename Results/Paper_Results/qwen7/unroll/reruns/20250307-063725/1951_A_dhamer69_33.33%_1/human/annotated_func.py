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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' printed based on the conditions checked within the loop for each iteration where `n` and `s` are provided as inputs.
    #
    #For each iteration of the loop, the value of `t` is decremented by 1 until it reaches 0. During each iteration, the program reads an integer `n` and a string `s`. If `n` equals 2, it checks if `s` is '00'. If `s` is '00', it prints 'YES'; otherwise, it prints 'NO'. If `n` is not 2, it counts the number of '1's in `s`. If the count of '1's is odd, it prints 'NO'. If there is exactly one occurrence of '11' in `s`, it also prints 'NO'. Otherwise, it prints 'YES'.
    #
    #The final output state will be a sequence of 'YES' and 'NO' strings corresponding to the results of each loop iteration, with no additional state variables being modified outside the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two inputs: an integer `n` and a string `s`. If `n` is 2, it checks if `s` is '00'. If true, it prints 'YES'; otherwise, it prints 'NO'. If `n` is not 2, it checks if the count of '1's in `s` is odd or if there is exactly one occurrence of '11' in `s`. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, it outputs a sequence of 'YES' and 'NO' strings corresponding to the results of each test case.

