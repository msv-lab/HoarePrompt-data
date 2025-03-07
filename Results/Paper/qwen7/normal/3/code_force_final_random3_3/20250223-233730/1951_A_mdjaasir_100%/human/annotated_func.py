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
        
    #State: Output State: `start` is an integer, `end` is an integer such that `start` <= `end`, `t` is the final input integer provided by the user, `i` is `t`, `n` is the last input integer, `a` is the last input string from the user, `count` is the number of '1's in the string `a`.
    #
    #In this final state, `i` will be equal to `t` because the loop runs `t` times. The values of `n` and `a` will be the inputs provided during the last iteration of the loop. The variable `count` will hold the number of '1's found in the string `a` entered during the last iteration. All other variables and their relationships remain as described in the initial and previous states.
#Overall this is what the function does:The function processes multiple inputs consisting of integers and strings. For each input, it counts the number of '1's in a given string. Based on the count, it prints either 'YES' or 'NO'. After processing all inputs, it outputs the final values of `t`, `i`, `n`, `a`, and `count`. The function does not return any value; it only prints the results.

