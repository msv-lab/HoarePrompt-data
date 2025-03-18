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
            y = 2 ** (i - 1) * (2 * f - 1)
            print(y)
        else:
            print(2 * k - 1)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^9. After all the executions of the loop have finished, the value of `y` is printed for each test case based on the conditions given in the loop body. The other variables (`s`, `i`, `d`, `h`, `p`, `g`, `f`) are used during the computation but their final values do not affect the output.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \) where \( 1 \leq k \leq n \leq 10^9 \). For each test case, it calculates and prints a value \( y \) based on the relationship between \( n \), \( k \), and the number of test cases \( t \) (where \( 1 \leq t \leq 5 \cdot 10^4 \)). If \( k \) is greater than half of \( n + 1 \), it computes \( y \) using a specific formula involving binary operations. Otherwise, it simply prints \( 2k - 1 \).

