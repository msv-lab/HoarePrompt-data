#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, x is a positive integer such that 1 ≤ x < 2^{30}.
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
        
    #State: Output State: The loop will execute exactly `t` times, where `t` is the initial input integer. After all iterations, the variable `i` will be `30 * t - 1`, meaning it will count up to one less than 30 times the number of iterations. The variable `flag` will be either `True` or `False` depending on the final state of the loop. The `length` variable will be `30 + (t - 1)`, as it increments by 1 for every iteration after the first. The list `s` will contain a sequence of '0's, '1's, and '-1's, with the exact pattern depending on the values of `x` for each iteration and the operations performed within the loop. Each element in `s` will be either '0', '1', or '-1', and the list will have a length of `30 + (t - 1)`.
    #
    #In summary, after all iterations, `i` will be `29t`, `flag` will be a boolean value, `length` will be `29 + t`, and `s` will be a list of length `29 + t` containing '0's, '1's, and '-1's, reflecting the transformations applied during each iteration based on the input values of `x`.
#Overall this is what the function does:The function processes `t` test cases, where `t` is a positive integer between 1 and 10^4. For each test case, it takes an integer `x` between 1 and 2^30 - 1. It converts `x` into a binary representation of 30 bits and then modifies this binary representation according to specific rules. The function outputs the length of the modified binary sequence and the sequence itself. The final state of the program includes printing the length and the modified binary sequence for each test case.

