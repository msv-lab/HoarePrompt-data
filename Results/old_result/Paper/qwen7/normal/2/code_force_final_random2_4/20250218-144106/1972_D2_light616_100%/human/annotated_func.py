#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6, and the product of n and m does not exceed 2 * 10^6.
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
        
    #State: Output State: `x` is greater than or equal to 5, `y` is 5, `n` is at least 10, `m` is at least 20, and `cnt` is 1.
    #
    #Explanation: After the loop has executed all its iterations, the value of `x` will be incremented until the condition `x * x > n` is met. Since the loop stops when `x * x` exceeds `n`, and given that `x` starts from 1 and increments by 1 each iteration, `x` will be at least 5 when the loop terminates (as it was 4 after 3 iterations and would increment to 5 on the next iteration). The value of `y` remains 5 because the inner loop does not change it. The conditions for `n` and `m` ensure they are at least 10 and 20 respectively, as these were the minimum values required even after 3 iterations. The value of `cnt` remains 1 because the inner loop only increments `cnt` once, regardless of how many times the outer loop runs.
    print(cnt)
    #This is printed: 1
#Overall this is what the function does:The function reads two positive integers \( n \) and \( m \) from the standard input, where \( 1 \leq n, m \leq 2 \times 10^6 \) and \( n \times m \leq 2 \times 10^6 \). It then iterates over pairs of integers \( (x, y) \) starting from \( (1, 1) \) up to the point where \( x^2 > n \) and \( (x + y) \times x \leq n \) and \( (x + y) \times y \leq m \). For each valid pair \( (x, y) \) where \( \text{gcd}(x, y) = 1 \), it increments a counter \( cnt \) by the minimum of \( \frac{n}{(x + y) \times x} \) and \( \frac{m}{(x + y) \times y} \). Finally, it prints the value of \( cnt \), which is guaranteed to be 1 based on the given constraints and logic. The function does not return any value.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4 and t equals 1 after all iterations of the loop have been executed, and func_1() has been called t times.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads two integers `n` and `m`. It then calls `func_1()` exactly `t` times, where `t` is the number of test cases. After processing all test cases, it does not return any value.

