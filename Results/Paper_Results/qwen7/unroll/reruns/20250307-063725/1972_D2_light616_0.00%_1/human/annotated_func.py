#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6 and the square root of n is less than or equal to the maximum possible value derived from the conditions (x + y) * x ≤ n and (x + y) * y ≤ m.
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
        
    #State: cnt is the sum of the minimum values of \( \frac{n}{(x+y)x} \) and \( \left\lfloor \frac{m}{(x+y)y} \right\rfloor \) for all pairs of integers (x, y) where \( x \) starts from 1 and increments by 1, and \( y \) starts from 1 and increments by 1 until \( (x+y)x > n \) or \( (x+y)y > m \), with the condition that \( \text{gcd}(x, y) = 1 \).
    print(cnt)
    #This is printed: cnt (where cnt is the sum of the minimum values of \(\frac{n}{(x+y)x}\) and \(\left\lfloor \frac{m}{(x+y)y} \right\rfloor\) for all valid (x, y) pairs)
#Overall this is what the function does:The function calculates and prints the sum of the minimum values of \(\frac{n}{(x+y)x}\) and \(\left\lfloor \frac{m}{(x+y)y} \right\rfloor\) for all pairs of integers (x, y) where \(x\) starts from 1 and increments by 1, and \(y\) starts from 1 and increments by 1 until \((x+y)x > n\) or \((x+y)y > m\), with the condition that \(\text{gcd}(x, y) = 1\).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` is an integer between 1 and 10^4 inclusive, and it has been used to control the number of iterations in the loop. After the loop executes all the iterations, no other variables are affected by the loop, so their states remain unchanged.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` (1 ≤ t ≤ 10^4) and then calls another function `func_1()` `t` times. After processing all test cases, it does not modify any variables and simply returns when the loop completes.

