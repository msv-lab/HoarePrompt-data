#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
            L.append(m)
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * (k - tot) - 1))
            tot += a
            pow *= 2
        
    #State: Output State: The output state will consist of a series of integers printed based on the given logic within the loop. For each test case defined by `t`, the program processes values of `n` and `k` to compute and print specific integers according to the described algorithm. Specifically, it calculates a sequence `L` where each element `m` is derived from `n` by repeatedly setting `m = (n + 1) // 2` and decrementing `n` by `m`. Then, it determines and prints an integer based on the position `k` within the cumulative sum of elements in `L`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it calculates a sequence \( L \) where each element \( m \) is derived by repeatedly halving \( n \) (with rounding up) until \( n \) becomes zero. It then determines and prints an integer based on the position \( k \) within the cumulative sum of elements in \( L \). The function reads \( t \) test cases from the input, where \( 1 \leq t \leq 5 \times 10^4 \), and \( 1 \leq k \leq n \leq 10^9 \) for each test case.

