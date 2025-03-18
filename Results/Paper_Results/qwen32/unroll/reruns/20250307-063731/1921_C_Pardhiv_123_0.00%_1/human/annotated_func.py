#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, f, a, and b are integers such that 1 <= n <= 2 * 10^5, 1 <= f, a, b <= 10^9. m is a list of n integers such that 1 <= m_i <= 10^9 and m_i < m_{i + 1}. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: t is 0, n, f, a, b, and ls are the values from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, `a`, `b`, and a strictly increasing list `m` of `n` integers. For each test case, it calculates whether a certain condition can be satisfied based on the values of `f`, `a`, `b`, and the differences between consecutive elements in `m`. It prints "YES" if the condition is met and "NO" otherwise. After processing all test cases, the function concludes.

