#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: Output State: The output state after the loop executes all the iterations depends on the value of `k` relative to \((n + 1) // 2\).
    #
    #- If `k > (n + 1) // 2`, then:
    #  - `i` will be the number of iterations required for `s` to reach `k`.
    #  - `s` will be exactly `k`.
    #  - `d` will be 0.
    #  - `h` will be 0.
    #  - `p` will be the number of iterations it took for `s` to reach `k`.
    #  - `g` will be the accumulated sum of \((h + 1) // 2\) over all iterations.
    #  - `f` will be `k - g`.
    #  - `y` will be \(2^{(i - 1)} * (k - g)\).
    #
    #- If `k <= (n + 1) // 2`, then:
    #  - `i` will remain 0.
    #  - `s`, `d`, `h`, `p`, `g`, `f`, and `y` will all be 0.
    #
    #In both cases, after all iterations, the final value of `y` will be printed.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it calculates and prints a value based on the relationship between \( n \), \( k \), and the number of iterations required to reach \( k \). If \( k \) is greater than half of \( n + 1 \), it computes a specific formula involving powers of 2. Otherwise, it simply prints \( 2k - 1 \). The function does not return any value but prints the result for each test case.

