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
        
    #State: A series of printed values, each determined by the values of `n` and `k` for each iteration of the outer loop, following the logic described in the code.
#Overall this is what the function does:The function processes `t` test cases, each defined by integers `n` and `k` with `1 ≤ k ≤ n`. For each test case, it computes and prints a specific integer value based on the values of `n` and `k`.

