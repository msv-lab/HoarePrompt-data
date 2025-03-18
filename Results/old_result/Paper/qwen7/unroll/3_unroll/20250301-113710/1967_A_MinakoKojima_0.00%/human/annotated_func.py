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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100; for each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}; a is a list of n integers such that 1 ≤ a_i ≤ 10^{12}; after executing all iterations of the loop, ans is an integer representing the product of differences between consecutive elements in the modified list a, where the list a is adjusted based on the value of k and the minimum element m in the initial list a.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n` and `k`, and a list `a` of `n` integers. For each test case, it first finds the minimum element `m` in the list `a`. If `k` is greater than or equal to `n * m`, it calculates the factorial of `n`. Otherwise, it adjusts the list `a` based on `k` and `m`, then computes the product of the differences between consecutive elements in the modified list `a`. Finally, it prints the computed value for each test case.

