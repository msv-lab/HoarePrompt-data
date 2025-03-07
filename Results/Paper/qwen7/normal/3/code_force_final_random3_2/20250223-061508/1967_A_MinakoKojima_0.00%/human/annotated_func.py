#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of each type initially.
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
        
    #State: The final value of `ans` is the product of differences between consecutive elements from `a[1]` to `a[n-1]` if `k` is less than `n * m` after all iterations, otherwise `ans` is `math.factorial(n)`.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it takes three inputs: the number of types of cards `n`, the integer `k`, and a list `a` of `n` integers representing the initial number of cards of each type. It then calculates and prints a result based on these inputs. If `k` is greater than or equal to `n * m` (where `m` is the minimum value in `a`), the result is `math.factorial(n)`. Otherwise, it adjusts the values in `a` to satisfy the condition `k < n * m` and calculates the product of differences between consecutive elements in the adjusted list `a`.

