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
        
    #State: Output State: t lines, each line containing an integer (which is the new length of the list `s` after processing) followed by a sequence of characters ('0', '1', or '-1') representing the processed binary representation of the input number. The processing rules transform the binary representation according to specific conditions and update the length of the list accordingly.
#Overall this is what the function does:The function processes a series of test cases, each defined by a positive integer \( t \) (number of test cases) and another positive integer \( x \) (within the range 1 to \( 2^{30} - 1 \)). For each test case, it converts \( x \) into its 30-bit binary representation, applies a series of transformations based on specific conditions, and outputs the new length of the binary representation along with the transformed binary string. The transformations include flipping bits under certain conditions and adjusting the length of the binary string accordingly. After processing all test cases, the function prints the results for each test case, showing the updated length and the modified binary string.

