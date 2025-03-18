#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 1000 for all i; the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: `ans1` is the sum of elements from `a[0]` to `a[k-1]` with specific adjustments based on the value of `x`, `ans2` is the maximum value between `ans1` and `ans2` after all iterations, `i` equals `k`, and `k` is less than `n`.
    #
    #In this final state, after the loop has executed all its iterations, `ans1` will reflect the sum of the first `k` elements of list `a`, adjusted by subtracting twice the value of each element from indices `x+i` to `k-1` for each `i` from `0` to `k-1`. The variable `ans2` will hold the maximum value between itself and `ans1` after all iterations. The variable `i` will be equal to `k` after the last iteration, and `k` will be less than `n` because the loop condition `i < k` ensures that `i` does not exceed `k-1`.
#Overall this is what the function does:The function processes a list of integers `a` and three additional integers `n`, `k`, and `x`. It calculates and returns the maximum value of a modified sum of the first `k` elements of `a`, where the sum is adjusted by subtracting twice the value of each element from indices `x+i` to `k-1` for each `i` from `0` to `k-1`.

