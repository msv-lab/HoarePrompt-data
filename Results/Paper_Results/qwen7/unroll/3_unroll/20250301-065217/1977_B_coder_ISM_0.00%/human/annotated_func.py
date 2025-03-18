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
        
    #State: Output State: The output state will vary based on the input integer `t` and the binary representation of each `x`. For each `x`, the program converts it to a 30-bit binary string, processes it according to specific rules, and prints the modified binary string along with its length. The processing rules include flipping certain bits and converting some '1's to '-1's under specific conditions. The final output state consists of `t` lines, each containing a modified 30-bit binary string or a 31-bit binary string if the length was increased, followed by the length of the string.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( t \) (where \( 1 \leq t \leq 10^4 \)) and a positive integer \( x \) (where \( 1 \leq x < 2^{30} \)). For each test case, it converts \( x \) into a 30-bit binary string, modifies this string according to specific rules, and prints the modified binary string along with its length. If the length of the binary string is increased during processing, it also prints the new length. The modifications include flipping certain bits and converting some '1's to '-1's under specific conditions.

