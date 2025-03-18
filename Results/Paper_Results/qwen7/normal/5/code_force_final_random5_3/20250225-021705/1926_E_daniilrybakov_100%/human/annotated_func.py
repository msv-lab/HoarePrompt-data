#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5 ⋅ 10^4. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        s = 0
        
        m = 1
        
        while n:
            x = (n + 1) // 2
            n //= 2
            if s < k and k <= s + x:
                break
            s += x
            m *= 2
        
        print((2 * (k - s) - 1) * m)
        
    #State: `n` is 0, `m` is 327680, `s` is the final accumulated sum of `x` values, and `k` is an input integer.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it calculates and prints a specific value based on the relationship between \( n \) and \( k \). Specifically, it finds the smallest integer \( m \) such that the sum of certain values \( x \) up to \( m \) meets or exceeds \( k \), and then computes and outputs a derived value involving \( k \) and \( m \). The function handles up to 50,000 test cases, where \( 1 \leq k \leq n \leq 10^9 \) and \( 1 \leq t \leq 5 \times 10^4 \).

