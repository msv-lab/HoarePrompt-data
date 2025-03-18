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
        
    #State: `x` remains an input integer, `t` is equal to the initial value of `t`, `nalla` is `t-1`, `length` is 30 or 31, `i` is 29, and `s` is a list containing 30 or 31 elements where each element is either '1', '0', or '-1'. The list `s` will have been processed such that any occurrence of `-1` followed by `1` will result in the `-1` moving one position to the left and the `1` becoming `0`. This process will continue through the entire list up to the 29th index. If `flag` is 1 and `s[29]` is '0', the 29th element of `s` (`s[29]`) is now '1'. If `flag` is 1 and `s[29]` is not '0', `length` is 31, and `s` is a list containing 31 elements where the last element is '0'. If `flag` is 0, `length` remains 30 and the last element of `s` is not '0'.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads another integer `x` (where 1 ≤ x < 2^30), converts `x` into a binary string representation, processes this binary string according to specific rules, and prints the length of the resulting string and the string itself. The processing involves converting certain sequences of '1's and '0's into special characters ('-1'), and then resolving these characters to ensure the final string meets the specified conditions. After processing all test cases, the function does not return any value, but it prints the results for each test case.

