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
        
    #State: After the loop has executed all iterations, `nalla` will be `t - 1`, `t` will remain the same as the input integer, `i` will be 29, `length` will be either 30 or 31, and `s` will be a list of 30 or 31 elements, each either '1', '0', or '-1'. If `flag` is 1 and `s[29]` is '0', then `length` will be 31, `s[30]` will be '1', and `s[29]` will be '0'. If `flag` is 0, then `length` will remain 30, `s` will remain a list of 30 elements, and `s[29]` will not be '0'. Additionally, any occurrences of the pattern '1' followed by '-1' in the list `s` will be replaced by '-1' followed by '0', starting from the beginning of the list and moving towards the end.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `x` (where 1 ≤ x < 2^30) and converts it into a binary string representation of length 30, stored in a list `s`. It then modifies the list `s` according to specific rules: if two consecutive '1's are found, the first '1' is replaced with '-1', and a flag is set. If the flag is set and the last element of `s` is '0', it is changed to '1'. If the flag is set and the last element is not '0', the last element is changed to '0', and an additional '1' is appended to `s`, increasing its length to 31. Finally, it prints the modified list `s`, the length of `s`, and the list `s` again. The function does not return any value.

