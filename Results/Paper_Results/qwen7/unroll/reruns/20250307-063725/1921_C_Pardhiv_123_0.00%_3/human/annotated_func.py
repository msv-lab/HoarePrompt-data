#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ f, a, b ≤ 10^9. Additionally, a list of n integers m_1, m_2, ..., m_n is provided where 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1} for all i.
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
        
    #State: Output State: The output state will consist of "YES" or "NO" printed for each iteration of the loop based on the remaining fuel `f` after processing each test case.
    #
    #To break it down:
    #- For each test case, the loop reads four integers `n`, `f`, `a`, and `b`, followed by a list of `n` integers `ls`.
    #- It then iterates through the list `ls` starting from the second element, updating the fuel `f` by subtracting the minimum of `a * (ls[i] - ls[i - 1])` or `b`.
    #- If `f` is greater than 0 after processing the entire list, it prints "YES"; otherwise, it prints "NO".
    #- This process repeats until `t` becomes 0, at which point the loop ends.
    #
    #The final output state will be a series of "YES" or "NO" strings corresponding to each test case processed within the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads four integers \( n \), \( f \), \( a \), and \( b \), along with a list of \( n \) integers. It then calculates the remaining fuel \( f \) after traveling through the list, subtracting the minimum of \( a \times (m_i - m_{i-1}) \) or \( b \) for each segment between consecutive elements in the list. If the remaining fuel \( f \) is greater than 0 after processing all segments, it prints "YES"; otherwise, it prints "NO". This process is repeated for each test case until all test cases are processed. The final output consists of a series of "YES" or "NO" strings corresponding to each test case.

