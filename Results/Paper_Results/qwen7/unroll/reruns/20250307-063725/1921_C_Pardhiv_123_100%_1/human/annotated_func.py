#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2·10^5, 1 ≤ f, a, b ≤ 10^9. The list m contains n integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}.
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
        
    #State: Output State: The output state will consist of "YES" or "NO" printed for each iteration of the loop based on the conditions provided.
    #
    #Explanation: For each iteration of the loop, the program reads values for `n`, `f`, `a`, and `b`, along with a list `ls`. It then iterates through the list, updating the variable `f` by subtracting the minimum of two values (`a * (ls[i] - ls[i - 1])` or `b`). If `f` remains positive after processing all elements in the list, it prints "YES"; otherwise, it prints "NO". After processing each test case, `t` is decremented. The final output state will be a series of "YES" or "NO" responses corresponding to each test case processed within the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( n \), \( f \), \( a \), \( b \), and a list of \( n \) integers sorted in ascending order. For each test case, it updates the value of \( f \) by subtracting the minimum of \( a \times (\text{current element} - \text{previous element}) \) or \( b \) from \( f \). If \( f \) remains positive after processing all elements in the list, it prints "YES"; otherwise, it prints "NO". This process is repeated for each of the \( t \) test cases, where \( t \) is an integer between 1 and \( 10^4 \). The function does not return any value but prints "YES" or "NO" for each test case.

