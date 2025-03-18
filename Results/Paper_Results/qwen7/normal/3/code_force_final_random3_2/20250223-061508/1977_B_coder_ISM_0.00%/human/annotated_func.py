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
        
    #State: Output State: `i` is 31, `length` is 31, `s` is a list of 31 elements where the 29th, 30th, and 31st elements are '1', and the rest of the elements in `s` are '0'.
    #
    #Explanation: After the loop has executed all its iterations, `i` will be 31 because the loop increments `i` from 1 to the length of `s`, which is 31. The length of `s` remains 31 as no new elements are appended to the list. The values of `s[0]` to `s[28]` become '0' due to the operations performed within the loop, while `s[29]`, `s[30]`, and `s[31]` remain '1'. This final state is consistent with the behavior described for the third iteration, extended to cover all iterations of the loop.
#Overall this is what the function does:The function processes a series of test cases, each containing a positive integer \(x\). For each \(x\), it converts \(x\) into a 30-bit binary representation, modifies this binary representation according to specific rules, and then prints the modified binary string along with its length. The final state of the program after processing all test cases is that it outputs the modified binary strings and their lengths for each test case.

