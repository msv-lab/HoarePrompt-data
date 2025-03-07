#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n, k, and x are integers where 1 ≤ n ≤ 2 · 10^5 and 1 ≤ x, k ≤ n, and a is a list of n integers where 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop will print the maximum possible value of the modified sum of the list `a` for each test case, after performing the specified operations. The variables `t`, `n`, `k`, `x`, and the list `a` will retain their values as they were at the start of each iteration, but the intermediate variables `ans1` and `ans2` will be recalculated for each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `n`, `k`, and `x`, and a list `a` of `n` integers. It then calculates and prints the maximum possible value of a modified sum of the list `a` for each test case. The modified sum is computed by initially summing all elements of `a`, then subtracting twice the value of the first `x` elements, and finally adjusting the sum by adding and subtracting specific elements based on the values of `k` and `x`. The function does not return any value; it only prints the result for each test case. The variables `t`, `n`, `k`, `x`, and the list `a` are reset for each test case, and their values do not persist across test cases.

