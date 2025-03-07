#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end are used to filter folder names which should be digits within the specified range.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2:
            print('NO')
        elif cnt1 == 1:
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: After all iterations of the loop have finished, `t` will be equal to the number of times the loop was executed, which is the initial value of `t`. For each iteration, `n` will be an input integer, and `s` will be a new input string for each iteration. The variable `cnt1` will be the count of '1's in the string `s` for that particular iteration. If the count of '1's in `s` is greater than 2 and even, `cnt1` will remain unchanged from its previous value (if any) or will be set to the current count. Otherwise, `cnt1` will be set to the count of '1's in `s` for that iteration.
    #
    #In summary, after all iterations, `t` will be the total number of iterations, `n` and `s` will be the latest inputs for the last iteration, and `cnt1` will be the count of '1's in the string `s` for the last iteration, unless the conditions specified in the loop body change it.
#Overall this is what the function does:The function processes multiple input strings, each followed by an integer and a string. For each string, it counts the occurrences of the digit '1'. Based on this count and certain conditions, it prints either 'YES' or 'NO'. After processing all inputs, the function outputs the final state of the loop variables, where `t` is the total number of iterations, `n` is the last input integer, `s` is the last input string, and `cnt1` is the count of '1's in the last input string.

