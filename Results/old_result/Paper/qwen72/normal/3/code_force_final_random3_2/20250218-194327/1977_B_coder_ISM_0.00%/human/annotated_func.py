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
        
    #State: After the loop executes all `t` iterations, the final state of `s` will be a list of 30 or 31 strings, depending on whether the `flag` was set during the last iteration. Each iteration processes the binary representation of `x` (input in that iteration) and applies the specified transformations. Specifically, the transformations replace '11' with '-10', and if the `flag` is set and the last element is '0', it changes to '1'. If the `flag` is set and the last element is not '0', a '0' is appended to the list, and a '1' is added at the end, increasing the length of `s` to 31. The `flag` is reset to 0 or 1 based on the transformations in each iteration. The variables `nalla` and `x` are updated with each iteration, but `t` remains unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads another integer `x` (where 1 ≤ x < 2^30) and processes the binary representation of `x` to create a list `s` of strings representing the binary digits. It then applies a series of transformations to `s` to replace '11' with '-10' and adjusts the last element based on a flag. The function prints the initial binary representation of `x`, the length of the transformed list `s`, and the final transformed list `s`. After processing all `t` test cases, the function concludes, and the final state of `s` will be a list of 30 or 31 strings, depending on the transformations applied in the last iteration. The variables `t`, `nalla`, and `x` are updated during the execution, but `t` remains unchanged after the initial input.

