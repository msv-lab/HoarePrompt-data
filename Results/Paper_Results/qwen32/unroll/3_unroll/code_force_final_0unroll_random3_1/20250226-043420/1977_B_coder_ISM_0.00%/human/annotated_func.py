#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, x is a positive integer such that 1 <= x < 2^30.
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
        
    #State: the final length of the binary representation after processing the last integer `x` and the modified binary representation.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a positive integer `x`, processes its binary representation, and outputs the modified binary representation along with its length. The modification involves replacing consecutive '1's with a '-1' and '1', and adjusting the binary string based on specific rules to ensure no consecutive '1's remain, except for the special case of a trailing '1' after a '-1'.

