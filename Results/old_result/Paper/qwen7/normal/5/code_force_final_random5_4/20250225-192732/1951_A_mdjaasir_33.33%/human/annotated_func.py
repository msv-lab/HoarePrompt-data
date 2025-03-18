#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end are used to filter folder names which should be digits within the specified range.
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
            if a.index('1') and a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: Output State: `count` is the total number of '1's in the input string `a` after processing all `t` inputs. `i` will be set to `t-1` after all iterations of the loop have completed, since `i` is incremented at the end of each iteration. `t` remains unchanged, `n` is an input integer for each iteration, and `start` and `end` are integers such that `start` <= `end` and are not affected by the loop. The value of `a` will be the last input string provided during the loop iterations.
    #
    #In natural language, after all iterations of the loop have finished, `count` will hold the cumulative number of '1's from all the input strings `a` provided during the loop. The variable `i` will be `t-1`, indicating the last iteration of the loop. The variable `t` will retain its initial value, `n` will be the last input integer received, and `start` and `end` will remain unchanged from their initial state.
#Overall this is what the function does:The function processes multiple input strings `a` over a series of iterations defined by `t`. For each input string, it counts the number of '1's. If the count of '1's is 0, 2, or even and greater than 2, it prints 'YES'. Otherwise, it prints 'NO'. After processing all inputs, the function outputs the cumulative count of '1's from all input strings and sets the loop index `i` to `t-1`. The variables `t`, `n`, and the initial values of `start` and `end` remain unchanged.

