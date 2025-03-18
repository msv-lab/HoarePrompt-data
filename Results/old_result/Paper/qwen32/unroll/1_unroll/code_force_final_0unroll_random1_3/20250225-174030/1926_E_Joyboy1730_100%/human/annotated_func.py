#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: The output state consists of `t` printed values, each calculated based on the input values `n` and `k` for that iteration.
#Overall this is what the function does:The function processes `t` test cases, each defined by two integers `n` and `k`. For each test case, it calculates and prints a specific value based on the relationship between `n` and `k`.

