#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, f is an integer such that 1 ≤ f ≤ 10^9, a is an integer such that 1 ≤ a ≤ 10^9, b is an integer such that 1 ≤ b ≤ 10^9, and m_1, m_2, ..., m_n are integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i + 1}. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t = 0, n remains unchanged, f is updated based on the loop's operations, a remains unchanged, b remains unchanged, ls is updated with the input list for each iteration.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of elements `n`, a fixed cost `f`, a per-unit cost `a`, and a flat rate `b`. It then reads a list of `n` strictly increasing integers. The function calculates whether the remaining cost `f` is positive after subtracting the minimum of `a` times the difference between consecutive elements in the list or `b` for each pair of consecutive elements. If `f` is positive after all calculations, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, `t` is set to 0, `n`, `a`, and `b` remain unchanged, and `f` and `ls` are updated for each test case.

