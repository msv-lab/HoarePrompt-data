#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 * 10^5, f, a, and b are integers such that 1 <= f, a, b <= 10^9, m_1, m_2, ..., m_n are integers such that 1 <= m_i <= 10^9 and m_i < m_{i + 1}. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: t = 0, n, f, a, b, and ls remain unchanged for each test case, but f is updated within the loop for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads four integers `n`, `f`, `a`, and `b`, followed by a list of `n` integers `m`. It then iterates through the list `m`, updating `f` by subtracting the minimum of `a * (m[i] - m[i-1])` and `b` for each element. After processing all elements in the list, it prints 'YES' if `f` is greater than 0, otherwise it prints 'NO'. The function continues this process for all `t` test cases until `t` reaches 0.

