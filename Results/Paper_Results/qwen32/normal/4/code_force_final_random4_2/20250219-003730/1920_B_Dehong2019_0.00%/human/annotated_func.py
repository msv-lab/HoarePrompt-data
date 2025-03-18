#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, k, and x are integers such that 1 <= n <= 2 * 10^5, 1 <= k <= n, and 1 <= x <= n. The sum of n over all test cases does not exceed 2 * 10^5. a is a list of integers of length n such that 1 <= a_i <= 1000 for each i from 1 to n.
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
        
    #State: After all iterations, `t` will be 0 (since it is decremented in each iteration). The variables `n`, `k`, `x`, and `a` will hold the values from the last iteration's input. The values of `ans1`, `ans2`, and `ans` will be the results of the last iteration's computation.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, `x`, and a list `a` of `n` integers. For each test case, it computes and prints a value that represents the maximum possible sum of the list `a` after performing specific operations based on the values of `k` and `x`.

