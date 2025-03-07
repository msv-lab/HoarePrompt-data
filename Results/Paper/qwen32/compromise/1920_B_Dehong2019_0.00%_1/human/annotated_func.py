#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are integers such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ k ≤ n, and 1 ≤ x ≤ n. The sum of n over all test cases does not exceed 2 · 10^5. The array a contains n integers where each element a_i satisfies 1 ≤ a_i ≤ 1000.
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
        
    #State: After all iterations, `t` is 0; `n`, `k`, `x`, and `a` are undefined as they are re-read in each iteration; `i` is undefined as it is a loop variable; `ans1`, `ans2`, and `ans` are the final values computed in the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `k`, `x`, and an array `a` of `n` integers. For each test case, it calculates and prints a specific value based on the given constraints and operations.

