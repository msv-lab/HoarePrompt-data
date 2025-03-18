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
        
    #State: The loop has finished executing all iterations, and for each test case, the value of `ans` is printed. The variables `t`, `n`, `k`, and `a` are no longer in their initial states and have been modified during the loop execution. Specifically, for each test case, `ans` is either the factorial of `n` if `k` is greater than or equal to `n * m`, or it is the product of the differences between consecutive elements in the modified list `a`. The list `a` has been updated such that each element is increased by a value that depends on `k` and the minimum value `m` in the list. The value of `k` is reduced during the loop, and `m` is the minimum value of the initial list `a`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of elements `n` and a value `k`, followed by a list `a` of `n` integers. It then calculates a result `ans` which is printed for each test case. If `k` is greater than or equal to `n * m` (where `m` is the minimum value in `a`), `ans` is the factorial of `n`. Otherwise, `ans` is the product of the differences between consecutive elements in a modified list `a`, where each element is adjusted based on `k` and `m`. The function does not return any value; it only prints the results. After the function concludes, the variables `t`, `n`, `k`, and `a` have been modified and are no longer in their initial states.

