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
        
    #State: The variable `x` is a positive integer such that 1 ≤ x < 2^30, `t` is an input integer. The loop has executed `t` times, and for each iteration, the binary representation of `x` has been modified according to the rules specified in the loop. The length of the modified binary representation is printed, followed by the modified binary digits. The final state of `x` is not preserved, and the list `s` contains the modified binary representation of the last input `x`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads another integer `x` (1 ≤ x < 2^30) and converts it to a binary string representation. It then modifies this binary string according to specific rules: it changes certain '1's to '-1's and '0's to '1's, and potentially extends the length of the binary string by one. After processing, it prints the length of the modified binary string and the modified binary digits. The function does not return any value, and the final state of `x` is not preserved. The list `s` contains the modified binary representation of the last input `x` after the function concludes.

