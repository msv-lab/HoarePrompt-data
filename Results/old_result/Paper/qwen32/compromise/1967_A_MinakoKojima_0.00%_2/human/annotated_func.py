#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, k is an integer such that 0 <= k <= 10^12, and a is a list of n integers where each element a_i is such that 1 <= a_i <= 10^12. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: After all iterations, `t` is 0; `n`, `k`, and `a` are the values from the last test case processed; `m` is the minimum value in the last `a`; `ans` is the final result for the last test case, calculated as either `math.factorial(n)` if `k >= n * m`, or as the product of the differences between consecutive elements in the adjusted `a` list; and `i` is `n` if `k >= n * m`, or `n-1` otherwise.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and a list `a` of `n` integers. For each test case, it calculates and prints a result based on the values of `n`, `k`, and the elements in `a`. The result is either the factorial of `n` if `k` is sufficiently large, or a product of differences between consecutive elements in a modified version of `a`.

