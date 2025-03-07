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
        
    #State: After the loop executes all iterations, `x` will be the last input integer provided, `t` will remain the same as the initial input integer, and `s` will be a list of characters representing the modified binary form of `x` with a length that may be 30 or 31 depending on the final value of `x` and the operations performed. The list `s` will contain '0', '1', and possibly '-1' characters, and the variable `length` will be the length of the list `s`.
#Overall this is what the function does:The function reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads another integer `x` (1 ≤ x < 2^30) and converts it into a binary string of length 30. It then modifies this binary string according to specific rules: if two consecutive '1's are found, the first '1' is replaced with '-1', and a flag is set. If the flag is set and a '0' is found, the '0' is replaced with '1', and the flag is reset. If the flag is still set after the loop, the last character of the list is modified, and an additional '1' may be appended, increasing the length to 31. The function prints the modified binary string, the length of the modified string, and the final modified string for each test case. The function does not return any value.

