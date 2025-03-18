#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ f, a, b ≤ 10^9. Additionally, m_1, m_2, ..., m_n are integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}.
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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' responses, each corresponding to whether the value of `f` is greater than 0 after processing each test case.
    #
    #To elaborate, for each iteration of the loop, the program reads in values for `n`, `f`, `a`, and `b`, followed by a list `ls`. It then iterates through the list, updating `f` based on the minimum cost (`a * (ls[i] - ls[i - 1])` or `b`). If `f` remains positive after processing all elements in the list, it prints 'YES'; otherwise, it prints 'NO'. This process repeats `t` times, with `t` being the initial value provided as input.
    #
    #The final output state is a sequence of 'YES' or 'NO' strings, where each string indicates the result of processing one test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer t (1 ≤ t ≤ 10^4), followed by n, f, a, b, and a list of n integers m_1, m_2, ..., m_n (1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}). For each test case, it calculates the value of f after iterating through the list and subtracting the minimum cost at each step. If f remains positive after processing all elements in the list, it prints 'YES'; otherwise, it prints 'NO'. The function outputs a sequence of 'YES' or 'NO' strings, each corresponding to the result of processing one test case.

