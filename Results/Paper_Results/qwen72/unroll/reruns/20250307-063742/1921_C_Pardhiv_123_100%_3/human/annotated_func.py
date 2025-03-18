#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 * 10^5, f, a, and b are integers such that 1 <= f, a, b <= 10^9, and m_1, m_2, ..., m_n are integers such that 1 <= m_i <= 10^9 and m_i < m_{i + 1}. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    t = int(input(''))
    while t > 0:
        n, f, a, b = map(int, input('').split(' '))
        
        ls = [0] + list(map(int, input('').split(' ')))
        
        for i in range(1, n + 1):
            f = f - min(a * (ls[i] - ls[i - 1]), b)
        
        if f > 0:
            print('YES')
        else:
            print('NO')
        
        t -= 1
        
    #State: t = 0, n, f, a, b, ls are reset for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads four integers `n`, `f`, `a`, and `b`, followed by a list of `n` integers. It then iterates through the list, reducing `f` by the minimum of `a` times the difference between consecutive elements in the list or `b`. After processing, it prints 'YES' if `f` is greater than 0, otherwise it prints 'NO'. The function continues this process for all `t` test cases, and upon completion, `t` is 0.

