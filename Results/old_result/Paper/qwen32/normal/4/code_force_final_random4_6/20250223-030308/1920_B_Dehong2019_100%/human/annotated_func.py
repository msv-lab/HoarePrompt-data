#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are integers such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ k ≤ n, and 1 ≤ x ≤ n. The array a contains n integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
            ans2 = max(ans1, ans2)
        
        print(ans2)
        
    #State: `t` remains the input integer such that 1 ≤ `t` ≤ 10^4; `n`, `k`, and `x` remain unchanged; `a` remains the sorted list of integers in descending order; `i` is `k - 1`; `ans1` is the sum of the initial `ans1` plus the sum of `a[i]` for `i` from `0` to `k-1` minus twice the sum of `a[i + x]` for `i` from `0` to `k-1` where `i + x < n`; `ans2` is the maximum value of `ans1` encountered during the loop iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `k`, `x`, and an array `a` of `n` integers. For each test case, it computes and prints a value that is derived by adjusting the sum of the array based on the values of `k` and `x`. Specifically, it maximizes a computed sum by adding the largest `k` elements and subtracting twice the largest `x` elements, considering overlaps appropriately.

