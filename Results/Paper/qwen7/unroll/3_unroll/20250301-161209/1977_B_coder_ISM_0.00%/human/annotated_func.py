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
        
    #State: After all iterations, the variable `t` will remain unchanged, and for each input integer `x`, the final state of `s` will be a list of 30 elements where each element is either '1', '0', or '-1'. The length of `s` will also be printed after processing each input, and it can vary from 30 to 31 based on the conditions inside the loop.
#Overall this is what the function does:The function processes a series of test cases, each containing a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4) and another positive integer \( x \) (1 ≤ \( x \) < 2^30). For each test case, it converts \( x \) into a binary representation of 30 bits and modifies this representation according to specific rules. It then prints the modified binary representation along with its length, which can be either 30 or 31. The function does not return any value but prints the results for each test case.

