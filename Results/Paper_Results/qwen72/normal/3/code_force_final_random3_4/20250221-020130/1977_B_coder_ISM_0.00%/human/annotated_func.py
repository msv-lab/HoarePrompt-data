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
        
    #State: The variable `x` is a positive integer such that 1 ≤ x < 2^30, and `t` is an input integer. The list `s` contains the binary representation of `x` with possible modifications due to the loop logic, and `length` is the length of the list `s` after all iterations. The modifications to `s` include converting pairs of consecutive '1's to '-1' and '0', and potentially appending an additional '1' to the list if the last bit was modified.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads another integer `x` (where 1 ≤ x < 2^30) and converts it to a binary string representation. It then modifies this binary string by converting pairs of consecutive '1's to '-1' and '0', and potentially appends an additional '1' to the string if the last bit was modified. The function prints the modified binary string, the length of the modified string, and the modified string again for each test case. The final state of the program includes the modified binary string and its length for each test case.

