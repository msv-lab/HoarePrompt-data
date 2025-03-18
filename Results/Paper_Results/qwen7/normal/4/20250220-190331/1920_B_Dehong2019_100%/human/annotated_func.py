#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n. Additionally, there is a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 1000 for each i. The sum of n across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: After the loop executes all iterations, `i` is equal to `k`, `k` is 0, `ans1` is the initial sum of all elements in list `a` minus twice the sum of the first `x` elements in list `a` plus the sum of the elements from index `i - x` to `i - 1` in the list `a`, `ans2` is the maximum value between its original value and the final `ans1`, `t` is decreased by `k * x * k` (which is 0), and the list `a` and the input integer `n` remain as they were initially.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes the number of test cases \( t \), the number of elements in a list \( n \), a positive integer \( k \), and another positive integer \( x \). It also processes a list of \( n \) integers \( a_1, a_2, \ldots, a_n \). The function calculates two values, \( ans1 \) and \( ans2 \), based on specific operations involving the list \( a \) and the integers \( k \) and \( x \). Finally, it prints the maximum value between the initial \( ans1 \) and the updated \( ans1 \) after performing the specified operations.

