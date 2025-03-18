#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each of the t test cases, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: `t` is the number of test cases, `n` and `k` are the values from the last test case, `L` is an empty list, `tot` is 0, and `pow` is 1.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k` where `1 ≤ k ≤ n`. For each test case, it calculates and prints a specific integer value based on the values of `n` and `k`.

