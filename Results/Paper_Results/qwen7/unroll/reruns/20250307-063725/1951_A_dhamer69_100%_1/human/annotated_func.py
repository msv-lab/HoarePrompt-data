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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' printed for each iteration of the loop based on the conditions provided in the loop body.
    #
    #The loop runs `t` times. For each iteration:
    #- If `n` equals 2, it checks if the string `s` is exactly '00'. If true, it prints 'YES', otherwise 'NO'.
    #- If `n` is not 2, it counts the number of '1's in `s`. If this count is odd, it prints 'NO'. If the count is 2 and there is exactly one occurrence of '11', it also prints 'NO'. Otherwise, it prints 'YES'.
    #
    #The final output state will be a sequence of 'YES' and 'NO' printed during the loop's execution, with each line corresponding to one iteration of the loop.
#Overall this is what the function does:The function processes a series of inputs, each consisting of an integer `t`, followed by `t` pairs of inputs: an integer `n` and a string `s`. Based on the value of `n`, it either checks if `s` is exactly '00' or counts the occurrences of '1' in `s` and checks specific conditions. For each pair, it prints 'YES' or 'NO' accordingly. The function does not return any value but outputs a sequence of 'YES' and 'NO' based on the given conditions.

