#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, f, a, b are integers such that 1 ≤ f, a, b ≤ 10^9, and m_1, m_2, ..., m_n are integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i + 1}. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    t = int(input(''))
    while t > 0:
        n, f, a, b = map(int, input('').split(' '))
        
        ls = list(map(int, input('').split(' ')))
        
        for i in range(1, len(ls)):
            f = f - min(a * (ls[i] - ls[i - 1]), b)
        
        if f > 0:
            print('YES')
        else:
            print('NO')
        
        t -= 1
        
    #State: t = 0, n, f, a, b, ls remain unchanged for the next iteration but are re-assigned within each iteration.
#Overall this is what the function does:The function `func` reads input values for `t`, `n`, `f`, `a`, `b`, and a list of integers `ls` from the user. It processes `t` test cases, where for each test case, it iterates through the list `ls` and updates the value of `f` based on the minimum of `a * (ls[i] - ls[i - 1])` and `b`. After processing the list, it prints 'YES' if `f` is greater than 0, otherwise it prints 'NO'. The function continues to process test cases until `t` becomes 0. After the function concludes, `t` is 0, and the values of `n`, `f`, `a`, `b`, and `ls` are re-assigned within each iteration and do not persist between test cases.

