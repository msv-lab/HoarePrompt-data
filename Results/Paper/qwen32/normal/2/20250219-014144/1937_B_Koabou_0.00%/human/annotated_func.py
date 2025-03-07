#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 2 · 10^5), followed by two binary strings of length n representing the grid. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1():
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: `n` is an input integer (2 ≤ n ≤ 2 · 10^5); `a` is a list containing two binary strings, where the first binary string is the first binary string of length `n` obtained from the input, and the second binary string is the second binary string of length `n` obtained from the input.
    #
    #Using the required format:
    #
    #Output State:
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: `s` is `a[0] + a[1][n - 1]` and `x` is `n-1`.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: s is `a[0] + a[1][n - 1]`, x is `n-1`, t is `1`.
    print(s, sep='')
    #This is printed: a[0]a[1][n - 1] (where a[0] is the first element of list a and a[1][n - 1] is the last element of the second element of list a)
    print(t)
    #This is printed: 1
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and two binary strings of length `n`. For each test case, it constructs a new string `s` based on specific conditions involving the two binary strings and prints `s` followed by an integer `t`. The construction of `s` involves combining parts of the two binary strings under certain conditions, and `t` is determined based on the overlap between the initial part of `s` and the first binary string.

