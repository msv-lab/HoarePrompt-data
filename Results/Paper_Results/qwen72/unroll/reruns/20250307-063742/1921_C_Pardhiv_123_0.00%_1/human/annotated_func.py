#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 * 10^5, f, a, and b are integers such that 1 <= f, a, b <= 10^9, and m_1, m_2, ..., m_n are integers such that 1 <= m_i <= 10^9 and m_i < m_{i + 1}. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: t is 0, n, f, a, b, and ls are unchanged for the next iteration, but their values are re-assigned based on the new input for each test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads four integers `n`, `f`, `a`, `b` and a list of `n` integers `ls`. It then iterates through the list `ls` and updates the value of `f` by subtracting the minimum of `a * (ls[i] - ls[i - 1])` and `b` for each pair of consecutive elements. After processing the list, it prints 'YES' if `f` is greater than 0, and 'NO' otherwise. The function continues this process for all `t` test cases. After all test cases are processed, `t` is 0, and the function ends.

