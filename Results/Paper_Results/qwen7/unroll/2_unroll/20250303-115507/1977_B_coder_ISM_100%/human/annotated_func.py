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
        
    #State: Output State: t lines, each line containing an integer length followed by a sequence of characters either '0', '1', or '-1'. The length represents the modified length of the binary representation after processing, and the sequence shows the modified binary digits with possible '-1' placeholders indicating specific conditions were met during the loop execution.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4) and another positive integer \( x \) (1 ≤ \( x \) < 2^30). For each test case, it converts \( x \) into its 30-bit binary representation, modifies the binary digits according to specific rules, and then prints the modified length of the binary representation along with the modified binary digits. The modified binary digits may include '0', '1', or '-1', where '-1' indicates a specific condition was met during the processing.

