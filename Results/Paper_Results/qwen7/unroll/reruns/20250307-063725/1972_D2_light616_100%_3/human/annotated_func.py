#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6 and n, m are within the limits specified in the problem description.
def func_1():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n // ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: cnt is the sum of minimum values calculated for each pair (x, y) where x and y are coprime, and (x + y) * x <= n and (x + y) * y <= m.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of minimum values for each pair (x, y) satisfying the given conditions)
#Overall this is what the function does:The function reads two positive integers \( n \) and \( m \) from the user, calculates the sum of the minimum values for each pair \((x, y)\) where \(x\) and \(y\) are coprime and satisfy the conditions \((x + y) \cdot x \leq n\) and \((x + y) \cdot y \leq m\), and prints the total sum. The function does not accept any parameters and does not return any value.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6 and n + m does not exceed 2⋅10^6 across all test cases.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: t is an integer between 1 and 10^4 inclusive, and after the loop executes all the iterations, t remains the same value it was initially set to. The variable `func_1()` is called t times, but no other variables are defined or modified within the loop, so their states remain unchanged from the initial state.
#Overall this is what the function does:The function processes a series of test cases, each containing two integers \(n\) and \(m\), under specific constraints (1 ≤ \(n\), \(m\) ≤ 2⋅10^6 and \(n + m\) does not exceed 2⋅10^6 across all test cases), and an integer \(t\) (1 ≤ \(t\) ≤ 10^4) indicating the number of test cases. It calls the function `func_1()` exactly \(t\) times without modifying any variables outside of this call. After completing all iterations, the value of \(t\) remains unchanged.

