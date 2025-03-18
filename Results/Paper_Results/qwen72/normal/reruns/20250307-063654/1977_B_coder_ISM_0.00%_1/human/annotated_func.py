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
        
        print(*s)
        
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
        
    #State: After the loop executes all iterations, `nalla` is `t-1`, `length` is 30 or 31, and `s` is a list of 30 or 31 strings where the transformation rules have been applied to all elements. The `flag` variable will be either 0 or 1 depending on the final transformation of `s[29]`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads another integer `x` (1 ≤ x < 2^30) and converts it to a binary string of length 30. It then applies a series of transformation rules to the binary string, which may result in the string being extended to a length of 31. The function prints the original binary string, the final length of the transformed string, and the transformed binary string for each test case. After all test cases are processed, the function concludes.

