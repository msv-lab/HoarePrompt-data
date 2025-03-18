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
        
    #State: t is 0; n, k, a, m, ans are undefined as the loop has finished executing for all test cases.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n`, a non-negative integer `k`, and a list `a` of `n` integers. It calculates and prints a specific value based on these inputs. If `k` is greater than or equal to the product of `n` and the minimum value in `a`, it returns the factorial of `n`. Otherwise, it modifies the list `a` according to a specific rule and returns the product of the differences between consecutive elements in the modified list.

