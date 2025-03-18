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
        
    #State: Output State: `t` is 0, `n` is 0, `k` is an input integer, `s` is the cumulative sum of `(n + 1) // 2` for each iteration until `n` becomes 0, `m` is \(2^{\text{number of iterations}}\), and `x` is (n + 1) // 2 for the last iteration when `n` is 0.
    #
    #In simpler terms, after the loop completes all its iterations, `t` will be 0 because it decreases by 1 for each iteration until it reaches 0. `n` will be 0 because it keeps halving until it reaches 0. The variable `s` will be the total sum of the values of `(n + 1) // 2` for each iteration. The variable `m` will be \(2^{\text{number of iterations}}\), representing the number of times the loop was executed. The variable `x` will hold the value of `(n + 1) // 2` from the last iteration when `n` is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it calculates a specific value based on the relationship between \( n \) and \( k \). Specifically, it iteratively halves \( n \) and accumulates a sum \( s \) until \( k \) falls within a certain range defined by \( s \) and the current value of \( n \). Finally, it computes and prints a result using \( s \), \( k \), and the accumulated multiplier \( m \). The function does not return any value but prints the calculated result for each test case.

