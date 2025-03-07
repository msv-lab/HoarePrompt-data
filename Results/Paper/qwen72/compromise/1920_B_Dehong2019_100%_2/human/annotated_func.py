#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, k, and x are integers for each test case such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ k, x ≤ n, and a_i are integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is 0, `_` is `t-1` (which is -1 after the last iteration), `n` is an input integer, `k` is an input integer, `x` is an input integer, `a` is a sorted list of integers in descending order based on the last input, `i` is `k-1`, `ans1` is the sum of all integers in the list `a` minus `2 * (a[0] + a[1] + ... + a[x-1])` plus the sum of the first `k` elements of `a` minus `2 * (a[x] + a[x+1] + ... + a[x+k-1])` if `x + k - 1 < n`, otherwise `ans1` is the sum of all integers in the list `a` minus `2 * (a[0] + a[1] + ... + a[x-1])` plus the sum of the first `k` elements of `a` minus `2 * (a[x] + a[x+1] + ... + a[n-1])`, `ans2` is the maximum value of `ans1` after all iterations.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `k`, `x`, and a list of integers `a_i`. For each test case, it calculates the maximum possible sum of the list `a` after performing a series of operations that involve subtracting and adding elements based on the values of `k` and `x`. The final result for each test case is printed. After processing all test cases, the function concludes with `t` being 0, `_` being `t-1` (which is -1), `n`, `k`, and `x` being the last input integers, `a` being the last sorted list of integers in descending order, `i` being `k-1`, `ans1` being the final sum after the operations, and `ans2` being the maximum value of `ans1` across all iterations.

