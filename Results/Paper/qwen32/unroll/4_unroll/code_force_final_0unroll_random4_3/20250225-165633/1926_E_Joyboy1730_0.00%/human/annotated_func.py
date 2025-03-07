#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: A series of integers printed to the console, each corresponding to the result of the operations within each iteration of the outer loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k` where `1 ≤ k ≤ n ≤ 10^9`. It then performs a series of operations based on these values and prints an integer result for each test case.

