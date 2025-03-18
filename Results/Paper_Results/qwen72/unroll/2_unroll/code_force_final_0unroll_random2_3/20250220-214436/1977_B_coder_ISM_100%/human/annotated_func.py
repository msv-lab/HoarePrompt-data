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
        
    #State: The loop will print the length of the modified binary representation of `x` and the modified binary string for each iteration of `nalla` in the range `t`. The variables `x`, `t`, and the list `s` will be modified within the loop, but the final state of `x` and `t` will be the same as their initial state after the loop completes, and `s` will be the final modified binary string for the last iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `x` from the input, where `1 ≤ x < 2^30`. The function then converts `x` into a binary string of length 30, modifies this binary string according to specific rules, and prints the length of the modified binary string followed by the modified binary string itself. The modifications involve flipping certain bits and potentially extending the length of the binary string. After processing all test cases, the function does not return any value, and the final state of the program is that the input values `x` and `t` are unchanged, but the list `s` contains the final modified binary string for the last test case.

