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
        
    #State: `x` is an input integer, `t` is 0, `nalla` is `t-1`, `i` is 30, `length` is 30 or 31 depending on the final value of `flag`, and `s` is a list containing 30 or 31 strings, each representing the result of the bitwise AND operation between the final value of `x` and `2^i` for `i` ranging from 0 to 29 (or 30 if `length` is 31). The list `s` has been processed to replace any occurrence of '1' followed by '1' with '-1' and '0', and any occurrence of '-1' immediately following a '1' with '0' and '-1'. If `flag` was 1 and `s[29]` was '0', then `s[29]` is set to '1'. If `flag` was 1 and `s[29]` was '1', then `s[29]` remains '1', and an additional '1' is appended to `s`, making `length` 31. If `flag` was 0, `s[29]` remains unchanged, and `length` is 30.
#Overall this is what the function does:The function `func` reads a number `t` from the user, indicating how many times the main operation should be performed. For each iteration, it reads a positive integer `x` (1 ≤ x < 2^30) and converts it into a binary string representation of length 30. It then processes this binary string to replace certain patterns: any '1' followed by another '1' is replaced with '-1' and '0', and any '-1' immediately following a '1' is replaced with '0' and '-1'. If a carry (`flag`) is set at the end of the processing and the last bit is '0', it is changed to '1'. If the carry is set and the last bit is '1', an additional '1' is appended to the list, increasing its length to 31. The function prints the initial binary string, the final length, and the processed binary string for each input `x`. The function does not return any value.

