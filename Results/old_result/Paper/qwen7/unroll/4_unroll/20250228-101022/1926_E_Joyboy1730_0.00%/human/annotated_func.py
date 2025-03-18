#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * k - 1))
                break
            tot += a
            k -= tot
            pow *= 2
        
    #State: Output State: The value of `t` remains the same as the initial input, and for each iteration from 1 to `t`, the program processes the values of `n` and `k` entered by the user. After processing, it prints a value based on the conditions specified in the loop body. The final output state will consist of `t` printed values, each derived from the respective `n` and `k` inputs.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \( n \) and \( k \) (with \( 1 \leq k \leq n \leq 10^9 \)). It then calculates and prints a specific value based on these inputs. The function outputs \( t \) values, one for each test case provided, following the specified conditions.

