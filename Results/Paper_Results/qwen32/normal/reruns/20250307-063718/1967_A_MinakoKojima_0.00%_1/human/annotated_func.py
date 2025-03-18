#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and k is a non-negative integer such that 0 <= k <= 10^12. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^12. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: The loop has executed `t` times, where `t` is the initial integer input representing the number of test cases. For each test case, the variables `n`, `k`, and `a` are updated based on the new input. The variable `m` is the minimum value of the list `a`. The variable `ans` is calculated as `math.factorial(n)` if `k` is greater than or equal to `n * m`; otherwise, `ans` is the product `a[0] * (a[1] - a[0]) * (a[2] - a[1]) * ... * (a[n-1] - a[n-2])`. The final `ans` for each test case is printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n`, a non-negative integer `k`, and a list `a` of `n` integers. It calculates and prints a result based on these inputs. If `k` is greater than or equal to `n` times the minimum value in `a`, the result is the factorial of `n`. Otherwise, it modifies the list `a` and calculates the result as the product of differences between consecutive elements in the modified list.

