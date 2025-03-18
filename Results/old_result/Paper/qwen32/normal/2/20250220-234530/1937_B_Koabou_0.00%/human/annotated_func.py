#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5. The first and second lines of each test case contain binary strings of length n, representing the rows a_{11} a_{12} \ldots a_{1n} and a_{21} a_{22} \ldots a_{2n}, respectively. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func_1():
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; for each test case, `n` is the input integer such that 2 ≤ n ≤ 2 · 10^5; the first line of each test case contains a binary string of length `n`; the second line of each test case contains another binary string of length `n`; `a` is a list containing two binary strings.
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: `s` is `a[0][:i + 1] + a[1][i:]` and `x` is `i` if the condition `a[0][i + 1] == '1' and a[1][i] == '0'` is satisfied for some `i`; otherwise, `s` is `a[0] + a[1][n - 1]` and `x` is `n - 1`.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: s is `a[0][:i + 1] + a[1][i:]` if `a[0][i + 1] == '1' and a[1][i] == '0'` for some `i`; otherwise, `s` is `a[0] + a[1][n - 1]`. `x` is `i` if `a[0][i + 1] == '1' and a[1][i] == '0'` for some `i` and `i >= 1`; otherwise, `x` is `n - 1`. `t` is `1`.
    print(s, sep='')
    #This is printed: s (where s is constructed based on the conditions involving a[0] and a[1])
    print(t)
    #This is printed: 1
#Overall this is what the function does:The function reads two binary strings of equal length `n` and constructs a new string `s` based on specific conditions involving the characters of these strings. It then prints the constructed string `s` followed by the value `1`.

