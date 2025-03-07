#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, k, and x are integers for each test case such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ k, x ≤ n, and a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n`, `k`, and `x` from input, sorts the list `a` in descending order, and calculates the maximum possible value of `ans` by applying the given transformations. The final value of `ans` for each test case is printed. The variables `t`, `n`, `k`, `x`, and `a` are reset for each test case, and their values are not retained between iterations. The sum of `n` over all test cases does not exceed 2 · 10^5, and the values of `a_i` remain within the specified range.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by integers `t`, `n`, `k`, and `x`, and an array `a` of integers. For each test case, it reads `n`, `k`, and `x` from input, sorts the array `a` in descending order, and calculates a value `ans` based on the given transformations. The final value of `ans` for each test case is printed. The function does not return any value; it only prints the results. The variables `t`, `n`, `k`, `x`, and `a` are reset for each test case, and their values are not retained between iterations. The sum of `n` over all test cases does not exceed 2 · 10^5, and the values of `a_i` remain within the specified range.

