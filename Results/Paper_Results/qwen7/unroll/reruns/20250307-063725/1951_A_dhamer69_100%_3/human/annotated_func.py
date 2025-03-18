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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' printed based on the conditions evaluated within the loop for each iteration where `n` and `s` are provided as inputs. Specifically, if `n` equals 2 and `s` is '00', it prints 'YES'. For other values of `n`, it checks if the count of '1's in `s` is odd or if there is exactly one occurrence of '11' with two '1's in total, printing 'NO' in these cases; otherwise, it prints 'YES'.
    #
    #The exact sequence of 'YES' and 'NO' depends on the inputs provided during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads two integers \( n \) and a string \( s \). If \( n \) is 2 and \( s \) is '00', it prints 'YES'. Otherwise, it checks if the number of '1's in \( s \) is odd or if there is exactly one occurrence of '11' with two '1's in total, in which case it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value but prints the result for each test case.

