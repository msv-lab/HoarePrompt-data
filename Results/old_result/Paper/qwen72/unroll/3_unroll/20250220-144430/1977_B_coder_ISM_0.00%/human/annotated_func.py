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
        
    #State: The value of `x` is not preserved and changes with each iteration based on user input. The list `s` will contain a sequence of characters representing the modified binary form of `x` after the transformations. The variable `length` will be the length of the modified list `s`, which could be 30 or 31 depending on the transformations applied. The variable `flag` will be 0 or 1 based on the final state of the transformations.
#Overall this is what the function does:The function `func` reads a positive integer `t` indicating the number of test cases. For each test case, it reads a positive integer `x` (1 ≤ x < 2^30) and converts it to a binary string of length 30. It then applies a series of transformations to this binary string, which may result in the string being modified and potentially extended to a length of 31. The function prints the original binary string, the length of the modified string, and the modified binary string for each test case. The value of `x` is not preserved across iterations, and the final state includes the modified binary string and its length.

