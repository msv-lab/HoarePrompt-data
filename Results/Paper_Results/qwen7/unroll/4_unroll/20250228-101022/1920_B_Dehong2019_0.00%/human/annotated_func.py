#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n. Additionally, there is a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 1000 for all i. The sum of n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state will be the maximum value of `ans` calculated for each iteration of the loop, printed after all iterations are completed. Each iteration processes a different set of inputs `n`, `k`, `x`, and a list of integers `a`, and calculates `ans` based on the given operations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers t, n, k, x, and a list of n integers a. It then calculates a value `ans` based on specific operations involving these inputs and prints the maximum value of `ans` for each test case.

