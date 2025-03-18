#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end represent valid folder names in the current directory (i.e., they are digits).
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
        
    #State: Output State: After the loop executes all iterations, `t` must be greater than 0, `n` is an integer input for each iteration, and `s` is a string input for each iteration. The variable `cnt1` is the count of '1's in the string `s` for each iteration. The final state of `t`, `n`, and `s` will depend on the inputs provided during each iteration of the loop, but `t` will be decremented by 1 for each iteration until it reaches 0. For each iteration, if `cnt1` is greater than 2 and even, the loop prints 'YES' and does not change `t`, `n`, or `s`. If `cnt1` is not greater than 2 or not even, the loop prints 'NO' and does not change `t`, `n`, or `s`. If '11' is found in `s`, the loop prints 'NO' and does not change `t`, `n`, or `s`. The final value of `t` will be 0, and the values of `n` and `s` will be the last inputs provided during the loop iterations.
#Overall this is what the function does:The function reads multiple inputs from the user, including an integer `t`, followed by `t` pairs of integers `n` and strings `s`. For each pair, it checks if the count of '1's in the string `s` is greater than 2 and even, or if '11' is present in `s`. Based on these conditions, it prints either 'YES' or 'NO'. After processing all inputs, the function returns nothing.

