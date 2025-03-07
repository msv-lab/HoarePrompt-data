#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6 and n, m are within the limits specified in the problem description.
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
        
    #State: Output State: `n` is less than 15, `m` is less than 10, `y` is 4, `x` is 4, and `cnt` remains unchanged.
    #
    #Explanation: After the loop has executed all its iterations, the conditions in the loop head (`while x * x <= n`) and the inner loop head (`while (x + y) * x <= n and (x + y) * y <= m`) dictate that the loop will stop when `x * x > n` or either `(x + y) * x > n` or `(x + y) * y > m`. Given the final state after 3 iterations, we know that `x` is 4, `n` is less than 15, and `m` is less than 10. Since `x` increments by 1 each iteration and starts at 1, the loop will stop when `x` reaches 4 because increasing `x` further would make `x * x > n`. The value of `y` remains 4 as it does not change within the loop once the outer loop's condition is met. The variable `cnt` remains unchanged because none of the conditions inside the loops would allow further increments of `x` or `y` that satisfy all the constraints.
    print(cnt)
    #This is printed: cnt (where cnt remains unchanged)
#Overall this is what the function does:The function reads two integers \( n \) and \( m \) from the user, where \( 1 \leq n, m \leq 2 \times 10^6 \). It then iterates over pairs of integers \( (x, y) \) such that \( x \) and \( y \) are positive integers, \( x \) starts from 1 and increments until \( x^2 > n \), and \( y \) starts from 1 and increments until either \( (x + y) \cdot x > n \) or \( (x + y) \cdot y > m \). For each valid pair \( (x, y) \) where \( \text{gcd}(x, y) = 1 \), it adds the minimum of \( \frac{n}{(x + y) \cdot x} \) and \( \frac{m}{(x + y) \cdot y} \) to the count \( cnt \). Finally, it prints the value of \( cnt \).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t is 0 and func_1() has been called exactly 3 times.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer between 1 and 10^4. For each test case, it calls `func_1()` exactly once without accepting or returning any direct values. After processing all test cases, `t` is set to 0.

