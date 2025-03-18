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
        
    #State: Output State: `t` is an input integer, 1 ≤ `t` ≤ 5 ⋅ 10^4, and for each input pair `(n, k)`, the output is calculated based on the given logic inside the loop. The final state of `t` remains unchanged, but the outputs for each `(n, k)` pair are printed according to the formula `(2 * (k - s) - 1) * m`.
#Overall this is what the function does:The function processes up to 50,000 test cases, each consisting of two integers \( n \) and \( k \) where \( 1 \leq k \leq n \leq 10^9 \). For each test case, it calculates and prints a value based on the relationship between \( n \) and \( k \) using a specific algorithm. The final state of the program includes printing these calculated values for each test case.

