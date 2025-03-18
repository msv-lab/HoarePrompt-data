#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n; and a is a list of n integers such that 1 ≤ a_i ≤ 1000. Additionally, the sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: After the loop executes all its iterations, `ans` will be the maximum value between the final `ans1` and `ans2`. `ans1` will be the sum of elements from index `x` to `x + k - 1` in list `a`, adjusted based on the conditions inside the loop. Specifically, if `i + x < n`, the value at index `i + x` will be subtracted twice from `ans1`. `ans2` will remain equal to the final value of `ans1`.
#Overall this is what the function does:The function processes a list of integers `a` along with three integers `n`, `k`, and `x`. It calculates two values, `ans1` and `ans2`, based on specific conditions involving the elements of `a`. After iterating through certain indices, it determines the maximum of these two values and prints it. Specifically, `ans1` is initially set to the sum of all elements in `a`, then adjusted by subtracting twice the first `x` elements. `ans2` starts as `ans1` and is further adjusted by adding the first `k` elements and subtracting twice the elements at indices `x + i` where `i < k` and `i + x < n`. The function ultimately outputs the maximum of `ans1` and `ans2`.

