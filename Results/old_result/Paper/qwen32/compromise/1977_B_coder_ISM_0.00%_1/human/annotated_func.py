#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, x is a positive integer such that 1 ≤ x < 2^30.
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
        
    #State: The loop will have processed all `t` test cases. For each test case, the list `s` will be transformed such that no consecutive `'-1'` and `'1'` pairs exist, and all `'-1'`s are moved to the leftmost positions, followed by `0`s, and then the rest of the elements, which will be either `0` or `1`. The variable `flag` will be either 0 or 1, and `length` will be either 30 or 31. The variable `t` will remain unchanged, and `nalla` will have completed iterating through all `t` test cases. The variable `x` will be the input integer for the current test case being processed.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a positive integer `x`. For each `x`, it performs a series of transformations on its binary representation, ensuring no consecutive `'-1'` and `'1'` pairs exist, and outputs the transformed binary string along with its length.

