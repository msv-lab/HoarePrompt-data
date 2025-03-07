#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6, and n and m are within the constraints specified in the problem description.
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
        
    #State: Output State: `x` is 5, `n` is 24, `m` is 24, `y` is 3, and `cnt` is 1.
    #
    #To understand this output state, let's break it down:
    #
    #- The loop continues as long as `x * x <= n`. Given that `x` starts from 1 and increments by 1 each iteration, we can determine the final value of `x` after all iterations.
    #- From the given information, we know that after 3 iterations, `x` is 4. Therefore, the loop will continue until `x` reaches 5 because the condition `x * x <= n` must still hold true.
    #- For `x = 5`, the loop will check the conditions with `y` starting from 1. However, since `n` is 24, `(x + y) * x = 6 * 5 = 30` which is greater than `n`, so `y` will not increment beyond its initial value of 1. This means `y` remains 3.
    #- Similarly, for `m = 24`, `(x + y) * y = 8 * 3 = 24` which is equal to `m`, but any further increment in `y` would make `(x + y) * y > m`, so `y` remains 3.
    #- The condition `math.gcd(x, y) == 1` holds true for `x = 5` and `y = 3` since their greatest common divisor is 1. However, the value of `cnt` does not change because the condition `min(n / ((x + y) * x), m // ((x + y) * y))` evaluates to 0 due to `(x + y) * x > n` and `(x + y) * y > m`.
    #- Thus, after all iterations, `x` becomes 5, `n` remains 24, `m` remains 24, `y` becomes 3, and `cnt` remains 1.
    print(cnt)
    #This is printed: 1
#Overall this is what the function does:The function reads two positive integers \( n \) and \( m \) from input, where \( 1 \leq n, m \leq 2 \times 10^6 \). It then iterates over possible values of \( x \) and \( y \) to count pairs \((x, y)\) such that both \( x \) and \( y \) are coprime, and the product \((x + y) \cdot x \leq n\) and \((x + y) \cdot y \leq m\). Finally, it prints the total count of such pairs.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` must be greater than or equal to 3.
    #
    #In natural language: The value of `t` must be at least 3 for the loop to execute all its iterations. This is because the loop can execute at least 3 times according to the given information, and each execution requires `t` to be greater than the current iteration number minus one. Therefore, for 3 iterations, `t` must be greater than or equal to 3.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it calls another function `func_1()`. The function does not return any value but ensures that the variable `t` (representing the number of test cases) is at least 3 before proceeding with the iterations.

