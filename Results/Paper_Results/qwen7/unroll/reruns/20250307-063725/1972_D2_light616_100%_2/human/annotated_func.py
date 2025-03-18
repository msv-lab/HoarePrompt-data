#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the square root of n is less than or equal to the maximum possible value derived from the conditions (x + y) * x ≤ n and (x + y) * y ≤ m.
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
        
    #State: cnt is the sum of the minimum values of \( \frac{n}{(x+y)x} \) and \( \frac{m}{(x+y)y} \) for all pairs of \( x \) and \( y \) that satisfy the conditions \( (x+y)x \leq n \), \( (x+y)y \leq m \), and \( \text{gcd}(x, y) = 1 \).
    print(cnt)
    #This is printed: cnt (where cnt is the sum of the minimum values of \(\frac{n}{(x+y)x}\) and \(\frac{m}{(x+y)y}\) for all pairs of \(x\) and \(y\) that satisfy the given conditions)
#Overall this is what the function does:The function reads two positive integers \( n \) and \( m \) from the input, where \( 1 \leq n, m \leq 2 \cdot 10^6 \). It then calculates the sum of the minimum values of \( \frac{n}{(x+y)x} \) and \( \frac{m}{(x+y)y} \) for all pairs of \( x \) and \( y \) that satisfy the conditions \( (x+y)x \leq n \), \( (x+y)y \leq m \), and \( \text{gcd}(x, y) = 1 \). Finally, it prints the calculated sum.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6, and n + m ≤ 2⋅10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` is the number of times `func_1()` has been called.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( n \) and \( m \), where \( 1 \leq n, m \leq 2 \times 10^6 \) and \( n + m \leq 2 \times 10^6 \). It also reads an integer \( t \) indicating the number of test cases, where \( 1 \leq t \leq 10^4 \). The function does not return any specific value but performs operations based on these inputs.

