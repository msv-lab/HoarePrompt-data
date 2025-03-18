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
        
    #State: The loop processes each input integer `x` for `t` iterations, converting it to a 30-bit binary string `s`. It then modifies `s` based on specific rules, potentially increasing its length by 1 if a carry is generated. After all iterations, the final state of `s` and `length` will depend on the last input `x` and the modifications applied. The variable `x` will be the last input integer, `t` will be 0 (since the loop has completed), `s` will be the modified binary string, and `length` will be the length of the modified `s` (either 30 or 31).
#Overall this is what the function does:The function `func` processes a series of positive integers `x` (where 1 ≤ x < 2^30) provided by the user. For each integer, it converts `x` into a 30-bit binary string `s` and then modifies `s` according to specific rules. These rules involve flipping bits and potentially adding an extra bit if a carry is generated. The function prints the original 30-bit binary string, the modified length of the binary string (which can be 30 or 31), and the final modified binary string. The function does not return any value. After processing all `t` inputs, the final state of the program is that `t` is 0, `x` is the last input integer, `s` is the final modified binary string, and `length` is the length of the modified `s` (either 30 or 31).

