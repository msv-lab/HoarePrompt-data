#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, k, and x are integers for each test case such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ x, k ≤ n, and a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is 0, `_` is a placeholder and does not need a specific value, `n` is the last input integer, `k` is the last input integer and must be greater than 0, `x` is the last input integer, `a` is a list of integers sorted in descending order from the last input, `i` is `k-1`, `ans1` is the sum of all integers in the list `a` minus twice the sum of the first `x` integers in the list `a` plus the sum of the first `k` integers in the list `a` minus `2 * (a[x] + a[x+1] + ... + a[x+k-1])` if `x + k - 1 < n`, otherwise `ans1` is the sum of all integers in the list `a` minus twice the sum of the first `x` integers in the list `a` plus the sum of the first `k` integers in the list `a`, `ans2` is the maximum value of `ans1` after all iterations, and `ans` is the maximum value of `ans1` after all iterations.
#Overall this is what the function does:The function `func` processes `t` test cases, where each test case is defined by integers `n`, `k`, and `x`, and a list of `n` integers. For each test case, it calculates and prints a result based on the following steps: It first sorts the list of integers in descending order. It then computes a modified sum of the list, where the sum of the first `x` elements is subtracted twice, and the sum of the first `k` elements is added. If `x + k - 1` is less than `n`, it further adjusts the sum by subtracting twice the sum of elements from `a[x]` to `a[x + k - 1]`. The function prints the maximum value of these adjusted sums for each test case. After processing all test cases, `t` is 0, and the function has no return value.

