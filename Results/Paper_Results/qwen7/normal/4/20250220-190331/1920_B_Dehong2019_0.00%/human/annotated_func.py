#State of the program right berfore the function call: t is a positive integer such that \(1 \leq t \leq 10^4\); for each test case, n, k, and x are positive integers such that \(1 \leq n \leq 2 \cdot 10^5\), \(1 \leq k, x \leq n\); and a list of n integers \(a_1, a_2, \ldots, a_n\) where \(1 \leq a_i \leq 1000\). Additionally, the sum of n over all test cases does not exceed \(2 \cdot 10^5\).
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
        
    #State: t is `k + 1`, `x` is less than or equal to `k`, `i` is `k`, `ans` is the maximum value between `ans1` and `ans2` after all iterations of the loop, and `ans1` is the final sum calculated after iterating through the entire list `a`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a list of integers and three parameters \(t\), \(n\), and \(k\). For each test case, it calculates two sums, modifies them based on specific conditions involving indices \(x\) and \(k\), and prints the maximum value between these two sums. The function ultimately returns the maximum value found across all test cases.

