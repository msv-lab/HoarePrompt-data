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
        
    #State: After the loop executes all iterations, `nalla` is equal to `t - 1`, `x` is an input integer, `t` is greater than or equal to the number of iterations executed, `length` is 30 or 31 depending on the final state of `flag` and `s[29]`, `i` is 29, and `s` is a list containing 30 or 31 elements where each element is either '1', '0', or '-1'. The list `s` represents the modified binary representation of `x` after processing all the rules specified in the loop, including the propagation of `-1` through the list and the potential addition of an extra bit if `flag` is set and `s[29]` is not '0'.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, which specifies the number of test cases. For each test case, it reads another integer `x` (where 1 ≤ x < 2^30). It then processes `x` to generate a modified binary representation stored in a list `s`. This list is manipulated according to specific rules, potentially extending its length to 31 bits. Finally, the function prints the length of the modified list and the elements of the list. The function does not return any value.

