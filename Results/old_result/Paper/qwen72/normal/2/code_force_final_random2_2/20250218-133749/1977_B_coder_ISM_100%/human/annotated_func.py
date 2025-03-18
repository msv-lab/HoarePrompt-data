#State of the program right berfore the function call: x is a positive integer such that 1 ≤ x < 2^30.
def func():
    t = int(input())
    for nalla in range(t):
        x = int(input())
        
        s = []
        
        length = 30
        
        for i in range(30):
            if x & pow(2, i):
                s.append('1')
            else:
                s.append('0')
        
        flag = 0
        
        for i in range(0, 29):
            if flag and s[i] == '0':
                s[i] = '1'
                flag = 0
            if flag == 0 and s[i] == s[i + 1] and s[i] == '1':
                s[i] = '-1'
                flag = 1
            elif flag == 1:
                s[i] = '0'
            else:
                pass
        
        if flag and s[29] == '0':
            s[29] = '1'
        elif flag:
            s[29] = '0'
            s.append('1')
            length += 1
        
        for i in range(1, length):
            if (s[i] == '-1') & (s[i - 1] == '1'):
                s[i] = '0'
                s[i - 1] = '-1'
        
        print(length)
        
        print(*s)
        
    #State: After the loop executes all the iterations, `nalla` is `t - 1`, `x` is the last input integer provided, `s` is a list of 30 or 31 elements (depending on whether `flag` was set in the last iteration), and `length` is 30 or 31 accordingly. The list `s` contains strings of '1', '0', or '-1', reflecting the transformations applied during the loop. Specifically, any consecutive '1's in the list `s` have been replaced with '-1' followed by '0', and any '-1' and '1' pairs have been transformed such that the '-1' moves one position to the left and becomes '0'. The final state of `s` will reflect these transformations, with the last element (`s[29]`) potentially being modified based on the conditions described in the loop.
#Overall this is what the function does:The function reads a series of positive integers `x` (where 1 ≤ x < 2^30) from user input, processes each integer to transform its binary representation according to specific rules, and prints the transformed binary string along with its length. The transformation involves replacing consecutive '1's with '-1' followed by '0', and handling carry-over operations when necessary. After processing all inputs, the function does not return any value but outputs the transformed binary strings and their lengths.

