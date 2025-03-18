#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the square root of n does not exceed 2 ⋅ 10^3. Additionally, the sum of all n values and the sum of all m values across all test cases do not exceed 2 ⋅ 10^6.
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
        
    #State: Output State: `x` is greater than the square root of `n`, `n` is an input integer, `m` is an input integer, `cnt` is the sum of `min(n // ((x + y) * x), m // ((x + y) * y))` for each iteration where the gcd of `x` and `y` is 1, starting from `y = 1` until the condition `(x + y) * x > n` or `(x + y) * y > m` is met, `y` is the last value of `y` that satisfied the conditions in the inner loop.
    #
    #In simpler terms, after the loop has executed all its iterations, `x` will be greater than the square root of `n`. The variable `cnt` will hold the total count of valid pairs `(x, y)` such that the greatest common divisor of `x` and `y` is 1, and both `(x + y) * x <= n` and `(x + y) * y <= m` are true. The value of `y` will be the last value it took during the last iteration of the inner loop before the conditions were no longer satisfied.
    print(cnt)
    #This is printed: cnt (where cnt is the count of valid pairs (x, y) satisfying the given conditions)
#Overall this is what the function does:The function reads two positive integers \( n \) and \( m \) from the standard input. It then iterates over all pairs of positive integers \( (x, y) \) such that \( x \times x \leq n \) and \( (x + y) \times x \leq n \) and \( (x + y) \times y \leq m \). For each valid pair, if the greatest common divisor of \( x \) and \( y \) is 1, it adds the minimum of \( \frac{n}{(x + y) \times x} \) and \( \frac{m}{(x + y) \times y} \) to a counter. After completing all iterations, it prints the value of the counter, which represents the total count of such valid pairs. The function does not accept any parameters and does not return any value.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` is an integer between 0 and \(10^4 - 3\), `_` is 3.
    #
    #Explanation: After each iteration of the loop, the value of `t` is effectively decremented by 1 because the loop runs from `0` to `t-1`. Therefore, after the loop has executed all its iterations (i.e., `t` times), `t` will be `0`. The variable `_` will hold the value of the last iteration index, which is `t - 1`, so it will be `t - 1 = 3` if the loop ran `t` times. Given that the loop can run a maximum of `t` times, and `t` starts at a maximum of \(10^4\), after running `t` times, `t` will be `0`. Thus, `t` is an integer between `0` and \(10^4 - 3\), and `_` is `3`.
#Overall this is what the function does:The function processes up to \(10^4\) test cases. For each test case, it calls `func_1()`. After processing all test cases, it sets `t` to 0 and `_` to 3. The function does not return any value but modifies the variables `t` and `_` based on the number of iterations.

