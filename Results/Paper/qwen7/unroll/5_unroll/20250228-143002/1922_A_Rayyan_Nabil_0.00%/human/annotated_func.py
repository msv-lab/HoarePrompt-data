#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func():
    t = int(input())
    l = 'YES'
    for i in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        for i in range(n):
            if a[i] != c[i] and b[i] != c[i]:
                l = 'YES'
        else:
            l = 'NO'
        
        print(l)
        
    #State: Output State: `t` is an integer between 1 and 1000 (inclusive), `l` is determined based on the comparison of strings `a`, `b`, and `c` for each index within the range of `n`, `n`, `a`, `b`, and `c` remain unchanged.
    #
    #In this output state, the variable `l` will be set to 'NO' if for any value of `i` in the range of `n`, the characters at the same index in strings `a`, `b`, and `c` do not satisfy the condition `a[i] != c[i] and b[i] != c[i]`. Otherwise, `l` will be set to 'YES'.
#Overall this is what the function does:Functionality: The function processes a series of test cases, each containing an integer t (1 ≤ t ≤ 1000), an integer n (1 ≤ n ≤ 20), and three strings a, b, and c, each consisting of exactly n lowercase Latin letters. For each test case, it compares the characters at each index of strings a, b, and c. If for any index i, the characters in a and c are different and the characters in b and c are also different, it sets the variable l to 'YES'. Otherwise, it sets l to 'NO'. After processing all test cases, it prints the value of l for each test case.

