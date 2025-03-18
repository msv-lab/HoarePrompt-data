#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, a is a list of n integers where 1 ≤ a_i ≤ 10^12. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: After the loop executes all the iterations, `_` is incremented by `t` (the number of test cases), `n` and `k` are integers greater than 0, `a` is a list of integers input by the user, and `m` is the smallest integer in the list `a`. For each test case, if `k` is greater than or equal to `n * m`, `ans` is set to `math.factorial(n)`. Otherwise, `ans` is set to the product of the differences between consecutive elements of the updated list `a` from `a[1] - a[0]` to `a[n-1] - a[n-2]`. The list `a` is updated such that each `a[i]` is set to `m + min(k, m + k // n - a[i])`, and `k` is updated to `k - sum(min(k, m + k // n - a[i]) for i in range(n))` for each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`, an integer `k`, and a list `a` of `n` integers. For each test case, it calculates a result `ans` based on the values of `n`, `k`, and `a`. If `k` is greater than or equal to `n * m` (where `m` is the minimum value in `a`), `ans` is set to the factorial of `n`. Otherwise, `ans` is set to the product of the differences between consecutive elements of the updated list `a`. The list `a` is updated such that each element is adjusted based on `k` and `m`. After processing all test cases, the function prints the result `ans` for each test case. The function does not return any value.

