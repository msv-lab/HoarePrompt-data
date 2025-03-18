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
        
    #State: i is 31, length is greater than 31, and s is a list of 32 elements where each element from index 1 to 30 follows the rule that if s[i-1] is '-1' and s[i] is '0', then s[i] is changed to '0'. The last two elements, s[31] and s[30], are '-1' and '0' respectively.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves reading a positive integer `t` (1 ≤ t ≤ 10^4) and another positive integer `x` (1 ≤ x < 2^30). For each test case, it converts `x` into its binary representation, manipulates this binary string according to specific rules, and prints the modified binary string along with its length. The function ensures that the final binary string adheres to certain conditions and outputs the length and the modified string for each test case.

