#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and k is a non-negative integer such that 0 <= k <= 10^12. a is a list of n integers where each a_i satisfies 1 <= a_i <= 10^12. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: a list of t integers, each representing the answer for the corresponding test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it calculates and prints an integer value based on the number of elements `n`, a non-negative integer `k`, and a list `a` of `n` integers. The final output for each test case is a computed value `ans` that depends on the conditions specified within the function.

