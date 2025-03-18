#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names without leading zeros.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = input()
        
        count = a.count('1')
        
        if count == 0:
            print('YES')
        elif count > 2 and count % 2 == 0:
            print('YES')
        elif count == 2:
            if a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: Output State: After the loop executes all iterations, the value of `i` will be `t-1`, `t` remains unchanged, `n` is the integer input on the last iteration, `a` is the string input on the last iteration, and `count` is the number of times '1' appears in `a` on the last iteration. The output of the program will depend on the value of `count` as follows:
    #- If `count` is 0, the output will be 'YES'.
    #- If `count` is greater than 2 and even, the output will be 'YES'.
    #- If `count` is exactly 2, the output will be 'YES' if the next character after the first '1' is not '1', otherwise it will be 'NO'.
    #- If none of the above conditions are met, the output will be 'NO'.
    #
    #In summary, the final output state will reflect the result of the last iteration of the loop based on the criteria provided within the loop's body.
#Overall this is what the function does:The function processes multiple inputs consisting of integers and strings. For each input, it counts the number of '1's in the string. Based on this count, it prints either 'YES' or 'NO'. Specifically, if the count is 0, greater than 2 and even, or exactly 2 with the next character not being '1', it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each input.

