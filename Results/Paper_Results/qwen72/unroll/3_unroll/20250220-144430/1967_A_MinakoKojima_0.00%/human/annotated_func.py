#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and k are integers for each test case where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, and a is a list of n integers where 1 ≤ a_i ≤ 10^12. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: The loop has finished executing for all test cases. The variable `t` has been exhausted, and the final output for each test case is printed. The values of `n`, `k`, and `a` are not retained between test cases, so they are reset for each iteration. The final state of `t` is 0, and the values of `n`, `k`, and `a` are undefined after the loop completes.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and an integer `k`, followed by a list `a` of `n` integers. It then computes a value `ans` based on the relationship between `k` and the elements of `a`. If `k` is greater than or equal to `n` times the minimum element of `a`, `ans` is set to the factorial of `n`. Otherwise, it modifies the elements of `a` and computes `ans` as a product of differences between consecutive elements of the modified list. The function prints the computed `ans` for each test case. After processing all test cases, the function completes, and the values of `n`, `k`, and `a` are undefined. The variable `t` is exhausted, and its final state is 0.

