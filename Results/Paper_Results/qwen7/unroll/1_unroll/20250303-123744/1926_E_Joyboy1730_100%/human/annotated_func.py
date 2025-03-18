#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: Output State: The output state depends on the inputs provided during each iteration of the loop. For each test case defined by `t`, the loop processes pairs of integers `(n, k)` and prints a result based on the operations performed within the loop. Specifically, it calculates a sequence `L` where each element represents half of the current value of `n` rounded up, subtracts this value from `n`, and appends the result to `L`. Then, it iterates over `L` to find the position where `k` falls within the cumulative sum of elements in `L`, and prints a calculated value based on this position. The output consists of multiple lines, one for each pair `(n, k)` processed, representing the computed results.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, and k. It first checks if t is within the range 1 to 50,000. If valid, it reads t test cases, where for each test case, it calculates a sequence L by repeatedly halving n (rounded up) until n becomes zero. Then, it determines the position where k falls within the cumulative sum of elements in L and computes and prints a specific value based on this position. The function outputs a series of results, one for each test case.

