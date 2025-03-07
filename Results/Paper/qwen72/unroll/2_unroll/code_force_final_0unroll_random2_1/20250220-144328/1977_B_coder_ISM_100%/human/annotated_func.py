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
        
    #State: The loop modifies the binary representation of `x` by flipping certain bits based on specific conditions. After all iterations, `x` is no longer directly accessible, but its modified binary representation is stored in the list `s`. The length of `s` is printed, which is either 30 or 31 depending on whether an extra bit was appended. The list `s` contains the modified binary representation of `x`, with some bits potentially set to '1', '0', or '-1'. The variable `t` is decremented by the number of iterations performed. The variable `nalla` is not used in the loop and remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads another integer `x` (1 ≤ x < 2^30) and modifies its binary representation according to specific rules. The modified binary representation is stored in the list `s`, which may contain '1', '0', or '-1'. The function then prints the length of the modified list `s` (which can be 30 or 31) and the elements of `s`. The function does not return any value. After the function concludes, the original value of `x` is no longer directly accessible, but its modified binary representation is printed. The variable `t` is decremented by the number of test cases processed.

