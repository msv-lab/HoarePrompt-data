#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6, and the square root of n is less than or equal to the maximum possible value that can be computed within the constraints.
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
        
    #State: cnt is the sum of the minimum values of \( \frac{n}{(x+y)x} \) and \( \frac{m}{(x+y)y} \) for all pairs (x, y) where \( (x+y)x \leq n \) and \( (x+y)y \leq m \) and gcd(x, y) = 1.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of the minimum values of \( \frac{n}{(x+y)x} \) and \( \frac{m}{(x+y)y} \) for all pairs (x, y) where \( (x+y)x \leq n \) and \( (x+y)y \leq m \) and gcd(x, y) = 1)
#Overall this is what the function does:The function reads two integers \( n \) and \( m \) from the input, then calculates and prints the sum of the minimum values of \( \frac{n}{(x+y)x} \) and \( \frac{m}{(x+y)y} \) for all pairs \( (x, y) \) where \( (x+y)x \leq n \) and \( (x+y)y \leq m \) and \( \text{gcd}(x, y) = 1 \).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: t is an integer between 1 and 10^4 inclusive, and after executing the loop, t remains unchanged; no other variables are defined or modified within the loop.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads two integers `n` and `m` (where 1 ≤ n, m ≤ 2,000,000) and calls another function `func_1()` to process these values. After processing all test cases, it outputs the value of `t`, which remains unchanged throughout the function execution.

