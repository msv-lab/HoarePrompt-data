#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: `t` is 0, `n` is 0 for all test cases, `k` is `k - tot` after the last iteration for each test case, `L` is a non-empty list with elements that were generated during the execution of the loop, `tot` is the sum of all elements in `L` for each test case, `pow` is `2^len(L)` if the loop did not break, or `2^(i+1)` where `i` is the index of the element in `L` that caused the loop to break, and `a` is the last element of `L` that was processed for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k` where 1 ≤ k ≤ n ≤ 10^9, and the total number of test cases `t` is such that 1 ≤ t ≤ 5 · 10^4. For each test case, it calculates and prints an integer value based on the relationship between `n` and `k`. The function does not return any value. After the function concludes, `t` is 0, `n` is 0 for all test cases, `k` is modified to `k - tot` after the last iteration for each test case, `L` is a non-empty list with elements generated during the execution, `tot` is the sum of all elements in `L` for each test case, and `pow` is either `2^len(L)` if the loop did not break or `2^(i+1)` where `i` is the index of the element in `L` that caused the loop to break.

