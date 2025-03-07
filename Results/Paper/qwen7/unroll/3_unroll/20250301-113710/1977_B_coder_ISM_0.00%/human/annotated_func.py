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
        
    #State: The output state will consist of a series of strings representing binary numbers with possible modifications based on specific conditions within the loop. Each string will be of length up to 31 characters ('-1', '0', or '1'), and the length of the string printed at the end of each iteration will indicate the modified length of the binary representation. The exact content of each string will depend on the input provided during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and another positive integer `x`. For each test case, it converts `x` into its 30-bit binary representation, modifies this binary string based on certain conditions, and outputs the modified binary string along with its length. Specifically, it flips certain bits and changes some '1's to '-1's under specific rules. The final output includes the modified binary string and its length for each test case.

