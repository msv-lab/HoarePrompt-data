#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}; a is a list of n integers such that 1 ≤ a_i ≤ 10^{12}.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        m = min(a)
        
        ans = 0
        
        if k >= n * m:
            ans = math.factorial(n)
        else:
            k -= n * m
            for i in range(n):
                a[i] = m + min(k, m + k // n - a[i])
                k -= min(k, m + k // n - a[i])
            ans = a[0]
            for i in range(1, n):
                ans *= a[i] - a[i - 1]
        
        print(ans)
        
    #State: The loop has executed all its iterations, and the final state of the variables is as follows: `t` is an integer such that 1 ≤ t ≤ 100; `n` is the last integer input for the nth iteration; `k` is the last integer input for the kth iteration; `a` is a list of integers representing the last input list for the nth iteration; `m` is the minimum value of the list `a`; `ans` is the final calculated answer based on the conditions inside the loop. If `k` was greater than or equal to `n * m` throughout all iterations, `ans` will be the factorial of `n`. Otherwise, `ans` will be the cumulative product of differences between consecutive elements of the list `a` from index 1 to `n-1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n and k, and a list a of n integers. It calculates and prints a value based on the input parameters. Specifically, it determines the minimum value in the list a and adjusts the values in a according to certain conditions involving k. Finally, it computes and outputs a result derived from the adjusted list a.

