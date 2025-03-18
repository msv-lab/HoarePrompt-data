#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 1000 for all i; and the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all its iterations, `k` will be 0, `ans` will be the maximum value between `ans1` and `ans2`, `ans1` will be the sum of all elements in `a` minus twice the sum of the first `x` elements of `a` after processing all elements in the loop, `i` will be `k` (which is 0), `t` will be 0 (since it decreases by 1 in each iteration and starts from a positive integer), `n` will be an input integer, `k` will be an input integer, `x` will be an input integer, `a` will be a list of integers sorted in descending order, and `ans2` will be equal to the final value of `ans1`.
    #
    #In simpler terms, after the loop completes all its iterations, `k` will be 0 because it is decremented by 1 in each iteration until it reaches 0. The variable `ans` will hold the maximum value between `ans1` and `ans2`, where `ans1` is the adjusted sum of all elements in the list `a` as per the given logic. The variable `i` will also be 0 since it starts from a value that is at least `k` and decreases by 1 in each iteration until it reaches 0. The variable `t` will be 0 because it is decremented by 1 in each iteration of the outer loop until it reaches 0. The variables `n`, `k`, and `x` will retain their initial values, and `a` will remain a list of integers sorted in descending order.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of integers t, n, k, x, and a list a of n integers. For each test case, it calculates a specific value based on the given conditions and prints the result. The final output is the maximum value between two calculated sums, where one sum is adjusted by subtracting twice the first x elements of the list a, and the other sum is adjusted by adding the first k elements of the list a after the initial adjustment.

