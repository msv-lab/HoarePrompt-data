#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6, and the product of n and m does not exceed 2 * 10^6.
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
    #This is printed: cnt (where cnt is the sum of min(n / ((x + y) * x), m // ((x + y) * y)) for all pairs (x, y) satisfying the given conditions)
#Overall this is what the function does:The function reads two positive integers \( n \) and \( m \) from input, then calculates and prints the sum of the minimum values between \( \frac{n}{(x + y) \cdot x} \) and \( \frac{m}{(x + y) \cdot y} \) for all pairs of positive integers \( (x, y) \) that satisfy the conditions \( x \cdot x \leq n \), \( (x + y) \cdot x \leq n \), and \( (x + y) \cdot y \leq m \), with the greatest common divisor of \( x \) and \( y \) being 1. The function returns nothing.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` is an integer between 1 and 10^4 inclusive, `func_1` has been called `t` times.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (1 ≤ t ≤ 10^4), and calls another function `func_1()` exactly `t` times. After processing all test cases, it does not return any value.

