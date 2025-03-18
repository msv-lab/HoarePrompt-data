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
        
    #State: Output State: `i` is 30, `length` is 31, `flag` is 1, `s[0]` is '-1', `s[1]` is '0', `s[2]` is '0', for all `i` from 3 to 28, `s[i]` is '0', `s[29]` is '1', `s[30]` is '1', and `s[31]` is '0'.
    #
    #Explanation: After all iterations of the loop have completed, the value of `i` will be 30 because the loop increments `i` starting from 1 and continues until it can no longer find a pair where `s[i]` is '-1' and `s[i - 1]` is '1'. The final modification to the list `s` occurs when `flag` is 1 and `s[29]` is '0', changing `s[29]` to '1' and appending '1' to the list, increasing `length` to 31. The rest of the elements in `s` remain unchanged based on the provided rules.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4) and another positive integer \( x \) (1 ≤ \( x \) < 2^30). For each test case, it converts \( x \) into its binary representation, modifies the binary string according to specific rules, and prints the modified binary string along with its length. The final state of the program includes printing the modified binary string and its length for each test case.

