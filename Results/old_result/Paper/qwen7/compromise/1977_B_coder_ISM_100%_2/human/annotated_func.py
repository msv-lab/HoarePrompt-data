#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, x is a positive integer such that 1 ≤ x < 2^{30}.
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
        
    #State: Output State: After all iterations, `i` is 30, `length` is exactly 31, the character at index 29 of string `s` is '0', and the character at index 30 of string `s` is '1'. The value of `flag` is 0. The string `s` has been fully processed according to the loop's rules, and no further modifications can be made, ensuring that every possible transformation based on the given conditions has been applied.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4) and another positive integer \( x \) (1 ≤ \( x \) < 2^30). For each test case, it converts \( x \) into a 30-bit binary representation, modifies this binary representation according to specific rules, and then prints the length of the modified binary string along with the string itself. The final state ensures that the string has been fully processed, and no further modifications can be made based on the given conditions.

