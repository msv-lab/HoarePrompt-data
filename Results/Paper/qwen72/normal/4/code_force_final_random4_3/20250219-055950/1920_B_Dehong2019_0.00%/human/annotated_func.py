#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, k, and x are integers for each test case such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ k, x ≤ n, and a is a list of n integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` must be at least `t`, `_` is `t-1`, `n`, `k`, and `x` are input integers, `a` is a list of input integers sorted in descending order, `i` is `k-1`, `ans1` is the sum of all elements in the list `a` minus 2 times the sum of the first `x` elements of `a`, plus the sum of the first `k` elements of `a`, minus 2 times the sum of the elements at indices `x` to `x + k - 1` (if these indices are within the bounds of the list `a`), and `ans` is the maximum value between the final `ans1` and the initial `ans2`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it takes an integer `n`, two integers `k` and `x`, and a list of `n` integers `a`. It calculates and prints the maximum possible value of a modified sum of the elements in `a`. The modification involves subtracting twice the sum of the first `x` elements from the total sum of `a`, then adding the sum of the first `k` elements, and finally subtracting twice the sum of the elements from index `x` to `x + k - 1` (if these indices are within the bounds of `a`). The function does not return any value; it only prints the result for each test case.

