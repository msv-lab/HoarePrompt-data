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
        
    #State: Output State: `start` is an integer, `end` is an integer such that `start` <= `end`, `t` is 0, `n` is the integer input by the user during the last iteration, `s` is the string input by the user during the last iteration, and the values of these variables remain unchanged unless `n` equals 2. If `n` does not equal 2, `count_1` is the number of times '1' appears in the string `s`. If `count_1` is odd, or if `count_1` is even and the string `s` contains exactly one instance of '11', the postcondition remains the same as the precondition. Otherwise, the postcondition remains the same as the precondition.
    #
    #In simpler terms, after all iterations of the loop have finished, `t` will be 0 because it is decremented by 1 in each iteration until it reaches 0. The values of `n` and `s` will be those provided during the last iteration of the loop. The output of the last iteration (whether 'YES' or 'NO') will depend on the conditions specified in the loop body, based on the value of `n` and the content of `s`.
#Overall this is what the function does:The function processes multiple inputs in a loop. For each input, it reads two integers \( t \) and \( n \), followed by a string \( s \). If \( n \) is 2, it checks if \( s \) is '00'. If so, it prints 'YES'; otherwise, it prints 'NO'. If \( n \) is not 2, it counts the number of '1's in \( s \). If the count of '1's is odd or if there is exactly one instance of '11' in \( s \), it prints 'NO'. Otherwise, it prints 'YES'. After processing all inputs, the function prints 'NO' for any remaining iterations where \( n \neq 2 \) and the count of '1's is even, or if \( s \) contains exactly one instance of '11'.

