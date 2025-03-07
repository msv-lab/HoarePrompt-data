#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: Output State: `k` is reduced by the total sum of all elements in `L` multiplied by the number of iterations, `n` is 0, `m` is 0, `pow` is \(2^t\), where \(t\) is the total number of iterations the loop executed, and `tot` equals the sum of all elements in `L`.
    #
    #Explanation: After the loop completes all its iterations, `k` will be reduced by the total sum of all elements in `L` for each iteration, resulting in a reduction of `k` by `t * (tot + a)` where `t` is the total number of iterations. The variable `n` becomes 0 because it is set to 0 in the while loop condition once `n` is fully processed. The variable `m` is no longer relevant since the loop has ended. The variable `pow` will be \(2^t\) where \(t\) is the total number of iterations, as it doubles with each iteration. The variable `tot` will be the sum of all elements in `L` because it accumulates the sum of elements from `L` throughout the iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \(n\) and \(k\). For each test case, it calculates a specific value based on the relationship between \(n\), \(k\), and the number of iterations \(t\). The function outputs this calculated value for each test case.

