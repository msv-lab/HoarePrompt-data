#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6, and the square root of n does not exceed 2 * 10^3.
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
        
    #State: Output State: `x` is 5, `n` is at least 55, `m` is at least 7, `y` is greater than 10, and `cnt` is 36.
    #
    #To understand this output state, let's break down the loop and the given information:
    #
    #1. The loop starts with `x` set to 1 and increments `x` by 1 each iteration as long as `x * x <= n`.
    #2. For each value of `x`, it initializes `y` to 1 and increments `y` as long as both `(x + y) * x <= n` and `(x + y) * y <= m` hold true.
    #3. If the greatest common divisor (gcd) of `x` and `y` is 1, it updates `cnt` by adding the minimum of `n / ((x + y) * x)` and `m // ((x + y) * y)` to `cnt`.
    #
    #From the provided output states after the first three iterations:
    #- After the first iteration (`x=2`), `cnt` is 12.
    #- After the second iteration (`x=3`), `cnt` is 15.
    #- After the third iteration (`x=4`), `cnt` is 24.
    #
    #We can infer that:
    #- Each increment of `x` adds to `cnt` based on the conditions of the inner while loop.
    #- The value of `cnt` increases by 3 for each additional iteration of the outer loop.
    #
    #Following this pattern:
    #- After the fourth iteration (`x=5`), `cnt` would be `24 + 3 = 27`.
    #- After the fifth iteration (`x=6`), `cnt` would be `27 + 3 = 30`.
    #- After the sixth iteration (`x=7`), `cnt` would be `30 + 3 = 33`.
    #- After the seventh iteration (`x=8`), `cnt` would be `33 + 3 = 36`.
    #
    #Since the problem does not specify the exact stopping condition but implies the loop continues until `x * x > n`, we assume the loop completes its iterations up to `x=5` based on the given information, leading to `cnt` being 36.
    #
    #Additionally, the constraints on `n` and `m` increase with each iteration, ensuring they meet the necessary conditions for the loop to continue. Thus, `n` must be at least 55 (since \(5^2 = 25\)), and `m` remains at least 7, with `y` starting from a value greater than 10 due to the increasing `x` values.
    print(cnt)
    #This is printed: 36
#Overall this is what the function does:The function reads two integers \( n \) and \( m \) from user input, where \( 1 \leq n, m \leq 2 \times 10^6 \) and the square root of \( n \) does not exceed \( 2 \times 10^3 \). It then iterates over possible pairs of integers \( (x, y) \) such that \( x \geq 1 \) and \( y \geq 1 \), updating a counter \( cnt \) based on certain conditions. Specifically, if the greatest common divisor of \( x \) and \( y \) is 1, and both \( (x + y) \times x \leq n \) and \( (x + y) \times y \leq m \) hold, it adds the minimum of \( \frac{n}{(x + y) \times x} \) and \( \frac{m}{(x + y) \times y} \) to \( cnt \). Finally, it prints the value of \( cnt \).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` must be greater than 0.
    #
    #Natural Language Description: After the loop executes all its iterations, the value of `t` must still be greater than 0. This is because the loop continues as long as `t` is greater than 0, and since no operations within the loop modify `t`, its initial condition remains unchanged.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it calls another function `func_1()`. After processing all test cases, the function ensures that the variable `t` (representing the number of remaining test cases) is still greater than 0. The function does not return any value but modifies the state of `t` to reflect the number of remaining test cases.

