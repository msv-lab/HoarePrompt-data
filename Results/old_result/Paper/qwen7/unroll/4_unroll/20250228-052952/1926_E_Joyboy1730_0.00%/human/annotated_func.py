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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4, and for each input pair `(n, k)`, the program prints a number based on the conditions specified in the loop body. After all iterations of the loop, the variable `t` remains unchanged, but the output consists of a series of numbers printed during each iteration.
#Overall this is what the function does:The function processes multiple test cases, each containing integers t, n, and k. For each test case, it calculates and prints a number based on specific conditions involving n and k. The function does not return any value but produces a series of outputs, one for each test case. The variable t remains unchanged after processing all test cases, but the output consists of numbers printed during each iteration.

