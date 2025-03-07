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
        
    #State: `t` is an integer such that 1 <= `t` <= 10^4, `nalla` is `t` (indicating all test cases have been processed), `x` is the input integer from the last test case, `s` is a list of 30 or 31 strings with no consecutive `'1'` and `'-1'` pairs, `length` is 30 or 31 based on the value of `flag` from the last test case, and `flag` is 0 or 1 based on the last test case's processing.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a positive integer `x`. For each `x`, it generates a binary representation of length 30, modifies it to ensure no consecutive '1's and '-1's, and then outputs the modified length and the modified binary representation.

