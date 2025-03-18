#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 2 · 10^5), followed by two binary strings of length n, representing the rows of the 2xN grid. The sum of n across all test cases does not exceed 2 · 10^5.
def func_1():
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: a is a list containing two elements: the first element is the integer `n` (2 ≤ `n` ≤ 2 · 10^5), and the second element is a binary string of length `n`.
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
        
    #State: If the loop breaks at iteration `k`, then `s` is `a[0][:k + 1] + a[1][k:]`, `x` is `k`, and `y` is the last value it was set to before the loop broke. If the loop completes all iterations without breaking, then `s` is `a[0] + a[1][n - 1]`, `x` is `n - 1`, and `y` is the last index where `a[0][i + 1] == '0'` and `a[1][i] == '1'`.
    t = 1
    for i in range(y, x):
        if a[1][i:x] == s[i + 1:x + 1]:
            t = x - i + 1
            break
        
    #State: s is a[0] + a[1][n - 1], x is n - 1, y is the last index where a[0][i + 1] == '0' and a[1][i] == '1', t is 1.
    print(s, sep='')
    #This is printed: a[0]a[1][n - 1] (where a[0] is the first element of the list a and a[1][n - 1] is the last element of the second element of the list a)
    print(t)
    #This is printed: 1
#Overall this is what the function does:The function `func_1` reads a test case consisting of an integer `n` and two binary strings of length `n`. It processes these strings to produce a new string `s` which is a concatenation of parts of the input strings, and an integer `t`. The function prints the string `s` and the integer `t`.

