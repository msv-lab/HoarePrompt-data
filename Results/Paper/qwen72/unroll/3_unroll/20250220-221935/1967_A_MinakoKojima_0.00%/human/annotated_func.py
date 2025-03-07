#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins, respectively. a is a list of n integers such that 1 ≤ a_i ≤ 10^12, representing the number of cards of type i initially available. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: For each test case, the loop outputs the value of `ans` which is calculated based on the initial conditions and the logic within the loop. The value of `ans` will be either the factorial of `n` if `k` is sufficiently large (i.e., `k >= n * m`), or a product of differences between the adjusted values in the list `a` if `k` is smaller. The variables `t`, `n`, `k`, and `a` are reset for each test case, so their final values are not retained after the loop completes.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of distinct types of cards `n`, the number of coins `k`, and a list `a` of integers representing the initial number of cards of each type. For each test case, it calculates and prints a value `ans`. If `k` is greater than or equal to `n * m` (where `m` is the minimum value in `a`), `ans` is set to the factorial of `n`. Otherwise, `ans` is calculated as a product of differences between the adjusted values in the list `a`. The variables `t`, `n`, `k`, and `a` are reset for each test case, so their final values are not retained after the loop completes.

