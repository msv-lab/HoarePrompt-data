#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: `t` is 0, `n` is 0, `k` is an input integer, `L` is a list containing the sequence of values \((n + 1) // 2\) calculated during each iteration until `n` becomes 0 for each test case, `tot` is the sum of all elements in `L` for each test case, `pow` is \(2^{\text{length of } L}\) for each test case.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it takes two integers `n` and `k` (where `1 ≤ k ≤ n ≤ 10^9`). It then performs a series of calculations to generate a sequence of values and prints a specific result based on the value of `k` and the sequence generated. After processing all test cases, the function terminates without returning any value. The final state of the program is that all test cases have been processed, and the corresponding results have been printed to the standard output.

