#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, x is a positive integer such that 1 <= x < 2^30.
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
        
    #State: The loop will execute `t` times, and for each execution, it will process an input integer `x` to create a binary string `s` of length 30 or 31. The string `s` will be transformed such that no two '1's are consecutive, and all `'-1'`s will be replaced by '0's. The final `s` for each `x` will be printed, followed by the length of `s` and then the transformed `s`. The variable `t` remains unchanged after all iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a positive integer `x` and processes it to create a binary representation of length 30 or 31. It then transforms this binary representation to ensure no two '1's are consecutive, replacing any `'-1'`s with '0's. The function prints the length of the transformed binary string and the transformed string itself for each test case.

