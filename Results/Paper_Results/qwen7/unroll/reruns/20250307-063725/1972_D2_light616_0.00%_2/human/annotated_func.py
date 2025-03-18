#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6 and n, m are within the limits specified in the problem description.
def func_1():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n / ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: cnt is the sum of min(n / ((x + y) * x), m // ((x + y) * y)) for all pairs (x, y) where x * x <= n, (x + y) * x <= n, and (x + y) * y <= m, with gcd(x, y) == 1.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of min(n / ((x + y) * x), m // ((x + y) * y)) for all pairs (x, y) with gcd(x, y) == 1, and x * x <= n, (x + y) * x <= n, and (x + y) * y <= m)
#Overall this is what the function does:The function reads two positive integers \( n \) and \( m \) from the standard input, then calculates and prints the sum of the minimum values of \( \frac{n}{(x + y) \cdot x} \) and \( \left\lfloor \frac{m}{(x + y) \cdot y} \right\rfloor \) for all pairs of positive integers \( (x, y) \) that satisfy \( x \cdot x \leq n \), \( (x + y) \cdot x \leq n \), and \( (x + y) \cdot y \leq m \), with the condition that \( \text{gcd}(x, y) = 1 \).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6, and n + m does not exceed 2⋅10^6 across all test cases.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` invocations of `func_1()` have been executed.
#Overall this is what the function does:The function processes a series of test cases, each involving two integers \(n\) and \(m\), and an integer \(t\). For each test case, it invokes `func_1()` exactly \(t\) times. After processing all test cases, it does not return any value.

