#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case contains four integers n, f, a, and b such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ f, a, b ≤ 10^9, representing the number of messages, the initial phone's charge, the charge consumption per unit of time, and the consumption when turned off and on sequentially. Each test case also contains a list of n integers m_1, m_2, ..., m_n such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i + 1}, representing the moments at which messages need to be sent. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t = 0.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by four integers (n, f, a, b) and a list of n integers (m_1, m_2, ..., m_n). For each test case, it determines whether the initial phone charge (f) is sufficient to send all messages at the specified moments (m_1, m_2, ..., m_n), considering the charge consumption per unit of time (a) and the charge consumption when the phone is turned off and on sequentially (b). If the charge is sufficient, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function terminates with `t` equal to 0.

