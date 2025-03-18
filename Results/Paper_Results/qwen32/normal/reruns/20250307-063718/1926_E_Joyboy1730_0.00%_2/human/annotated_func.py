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
        
    #State: t is 0, n is 0, L is an empty list, tot is 0, pow is 1.
#Overall this is what the function does:The function processes `t` test cases, each defined by two integers `n` and `k` with `1 ≤ k ≤ n`. For each test case, it calculates and prints a specific value based on the relationship between `n` and `k`.

