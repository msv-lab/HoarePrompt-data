#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 2 ⋅ 10^5) followed by two binary strings of length n, representing the grid. The number of test cases t is between 1 and 10^4, and the sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func_1():
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: a is a list containing two binary strings of length `n`; `n` is unchanged.
    s = []
    x = 0
    y = 0
    for i in range(n - 1):
        if a[0][i + 1] == '0' and a[1][i] == '1':
            y = i
        
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: a is ['1101', '0110']; n is unchanged; s is '1110'; x is 0; y is 0.
    t = 1
    for i in range(y, x):
        if a[1][i:x] == s[i + 1:x + 1]:
            t = x - i + 1
            break
        
    #State: a is ['1101', '0110']; n is unchanged; s is '1110'; x is 0; y is 0; t is 1.
    print(s, sep='')
    #This is printed: 1110
    print(t)
    #This is printed: 1
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and two binary strings of length `n`. For each test case, it processes the binary strings and prints a modified binary string `s` and an integer `t`. The modified binary string `s` is derived based on specific conditions involving transitions between '0' and '1' in the input strings, and `t` is determined by the length of a matching substring.

