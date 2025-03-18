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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each value of t, the variable `x` is an integer read from input, and `s` is a list of strings representing the binary representation of `x` with some modifications based on specific rules. After processing, `length` is updated to reflect the new length of the list `s`. The final output consists of the new length and the modified list `s` printed line by line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4) and another positive integer \( x \) (1 ≤ \( x \) < 2^30). For each test case, it reads \( x \), converts it to its binary representation, and applies a series of transformations based on specific rules. The final output for each test case includes the new length of the binary representation and the modified binary string.

