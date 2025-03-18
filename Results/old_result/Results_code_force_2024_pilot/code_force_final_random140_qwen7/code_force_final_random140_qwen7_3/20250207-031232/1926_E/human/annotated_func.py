#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        s = 0
        
        i = 0
        
        d = n
        
        h = n
        
        p = 1
        
        g = 0
        
        if k > (n + 1) // 2:
            while s < k and d > 0:
                s += (d + 1) // 2
                d -= (d + 1) // 2
                i += 1
            while p <= i - 1:
                g += (h + 1) // 2
                h -= (h + 1) // 2
                p += 1
            f = k - g
            y = 2 ** (i - 1) * f
            print(y)
        else:
            print(2 * k - 1)
        
    #State: Output State: The loop will continue to execute as long as there are more inputs provided via `input()`. After all iterations of the loop have finished, the final output state will depend on the last set of inputs `n` and `k` provided. 
    #
    #- If `k > (n + 1) // 2`, then:
    #  - `i` will be the total number of iterations in the first while loop.
    #  - `g` will be the sum of `(n + 1) // 2` and the series of terms resulting from the operation `(h + 1) // 2` for each iteration.
    #  - `f` will be `k - g`.
    #  - `y` will be calculated as `2 ** (i - 1) * f`.
    #
    #- If `k <= (n + 1) // 2`, then:
    #  - `i` will be 0.
    #  - `y` will be `2 * k - 1`.
    #
    #The final value of `y` will be printed for each test case, and the process repeats until all inputs are processed. The output state after all iterations will include the final computed value of `y` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), and \( k \). For each test case, it calculates and prints a value \( y \) based on specific conditions involving \( n \) and \( k \). If \( k > \frac{n + 1}{2} \), it computes \( y \) using a series of arithmetic operations. Otherwise, it directly calculates \( y \) as \( 2k - 1 \). The function continues processing until all test cases are exhausted.

