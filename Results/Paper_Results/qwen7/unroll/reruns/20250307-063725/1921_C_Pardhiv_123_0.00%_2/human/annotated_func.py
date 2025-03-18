#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2·10^5, 1 ≤ f, a, b ≤ 10^9. The list m contains n integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}.
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
        
    #State: Output State: The output state will consist of "YES" or "NO" printed for each iteration of the while loop, depending on whether the value of `f` is greater than 0 after executing the operations inside the loop.
    #
    #To break it down further:
    #- For each value of `t`, the program reads four integers (`n`, `f`, `a`, `b`) and a list of integers (`ls`).
    #- It then iterates through the list `ls` starting from the second element, calculating the minimum cost of moving from one element to the next using either `a` or `b`.
    #- The variable `f` is updated by subtracting the minimum cost for each step.
    #- If `f` is still positive after processing all elements in `ls`, "YES" is printed; otherwise, "NO" is printed.
    #- After printing the result for the current `t`, `t` is decremented by 1.
    #- This process repeats until `t` becomes 0.
    #
    #The final output state will be a series of "YES" or "NO" responses, one for each iteration of the while loop, based on the calculations performed within the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads four integers \( n \), \( f \), \( a \), and \( b \), and a list of \( n \) integers. It then calculates the minimum cost required to move from each element to the next in the list, subtracting this cost from \( f \). If \( f \) remains positive after processing all elements, it prints "YES"; otherwise, it prints "NO". This process is repeated for each test case, and the final output consists of "YES" or "NO" for each test case.

