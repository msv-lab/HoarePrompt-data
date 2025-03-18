#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end are used to filter folder names which should be digits within the specified range.
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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' printed for each iteration of the loop based on the conditions specified in the loop body.
    #
    #For each iteration:
    #- If `n` is 2, the program checks if `s` is '00'. If it is, it prints 'YES', otherwise it prints 'NO'.
    #- If `n` is not 2, the program counts the number of '1's in `s`. If this count is odd, it prints 'NO'. If the count is 2 and there is exactly one occurrence of '11', it also prints 'NO'. Otherwise, it prints 'YES'.
    #
    #The final output state will be a sequence of 'YES' and 'NO' outputs corresponding to each input pair `(n, s)` provided during the loop iterations.
#Overall this is what the function does:The function processes a series of input pairs consisting of an integer `n` and a string `s`. For each pair, if `n` is 2, it checks if `s` equals '00'; otherwise, it counts the number of '1's in `s`. If the count is odd or if the count is 2 with exactly one occurrence of '11', it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value but prints a sequence of 'YES' and 'NO' outputs based on the given conditions.

