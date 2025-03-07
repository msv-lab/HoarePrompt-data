#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, k, and x are integers such that 1 <= n <= 2 * 10^5, 1 <= k <= n, and 1 <= x <= n. The array a contains n integers such that 1 <= a_i <= 1000 for each i. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    """
    Created on Fri Sep  6 21:42:15 2024
     
    @author: dehon
    """
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        
        a = sorted(list(map(int, input().split())), reverse=True)
        
        ans1 = sum(a)
        
        for i in range(x):
            ans1 -= a[i] * 2
        
        ans2 = ans1
        
        for i in range(k):
            ans1 += a[i]
            if i + x < n:
                ans1 -= a[i + x] * 2
            ans = max(ans1, ans2)
        
        print(ans)
        
    #State: The sequence of printed values for each of the t test cases.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it receives integers `n`, `k`, and `x`, and an array `a` of `n` integers. It calculates and prints a value based on the specified operations involving the array and the parameters `k` and `x`. Specifically, it computes a modified sum of the array elements after applying certain reductions and additions as defined in the code.

