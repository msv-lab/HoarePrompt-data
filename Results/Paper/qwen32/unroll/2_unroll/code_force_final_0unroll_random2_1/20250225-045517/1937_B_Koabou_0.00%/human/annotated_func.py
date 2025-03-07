#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains an integer n (2 ≤ n ≤ 2 · 10^5) representing the length of the grid. The next two lines each contain a binary string of length n, representing the binary values in the first and second row of the grid, respectively. It is guaranteed that the sum of n over all test cases does not exceed 2 · 10^5.
def func_1():
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: The list `a` contains two binary strings, one from each iteration of the loop. The values of `t` and `n` remain unchanged.
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: List `a` contains two binary strings, `t` and `n` remain unchanged, `s` is `'1011'`, and `x` is `2`.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: List `a` contains two binary strings, `t` is 3, `n` remains unchanged, `s` is `'1011'`, and `x` is `2`.
    print(s, sep='')
    #This is printed: 1011
    print(t)
    #This is printed: 3
#Overall this is what the function does:The function `func_1` reads multiple test cases. For each test case, it receives an integer `n` and two binary strings of length `n`. It then processes these inputs to derive a new binary string `s` and an integer `t`, which it prints. The string `s` is constructed based on specific conditions comparing the two input binary strings, and `t` is determined based on the prefix matching of the derived string `s` with the first input binary string.

