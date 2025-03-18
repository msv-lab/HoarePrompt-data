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
        
    #State: After the loop has executed all iterations, the variable `_` is equal to `t`, indicating that the loop has run `t` times. The variable `t` remains unchanged from its initial value. For each iteration, the variables `n` and `k` are reset based on the input provided for that specific test case. The variable `m` is the last computed value of \((n + 1) // 2\) before `n` became 0 or non-positive for the last test case. The list `L` contains the values of \((n + 1) // 2\) computed during each iteration of the inner while loop for the last test case. The variable `tot` is the sum of all elements in `L` for the last test case. The variable `pow` is \(2^{\text{length of } L}\) for the last test case. If the condition `tot < k` and `k <= tot + a` is met for any `a` in `L` during the last test case, the corresponding output was printed.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of two integers `n` and `k`. It processes each test case to compute and print a specific value based on the relationship between `n` and `k`. Specifically, it divides `n` into parts and uses these parts to determine a value that is printed if certain conditions are met. The function does not return any value; instead, it prints the results directly to the standard output. After processing all test cases, the function completes without modifying the initial value of `t`, and the internal variables used for computation (`n`, `k`, `L`, `tot`, `pow`) are reset for each test case.

