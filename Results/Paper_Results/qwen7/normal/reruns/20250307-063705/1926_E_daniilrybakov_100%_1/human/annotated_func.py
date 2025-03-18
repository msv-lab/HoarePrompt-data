#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: `n` is now `n // 2
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it calculates and prints a specific value based on the relationship between \( n \) and \( k \). Specifically, it finds the smallest integer \( m \) such that the sum of certain terms up to \( m \) is just less than or equal to \( k \), and then computes and outputs a formula involving \( k \) and \( m \). The function reads \( t \) test cases from the input, where \( 1 \leq t \leq 5 \times 10^4 \), and \( 1 \leq k \leq n \leq 10^9 \) for each test case.

