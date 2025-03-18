#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, x is a positive integer such that 1 ≤ x < 2^30.
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
        
    #State: `t` iterations completed, `nalla` equals `t`, `x` is the last input integer, `s` is the final transformed list for the last `x`, and `length` is the final length of `s`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a positive integer `x` and processes it to produce a binary-like string representation of `x` with specific transformations applied. It then prints the length of the transformed string and the transformed string itself. The transformation involves replacing consecutive '1's with a special marker and adjusting the string based on certain rules, potentially increasing its length.

