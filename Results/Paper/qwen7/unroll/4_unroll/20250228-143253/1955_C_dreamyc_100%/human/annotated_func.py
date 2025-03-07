#State of the program right berfore the function call: t is a positive integer, n and k are positive integers such that 1 ≤ n ≤ 2 * 10^5 and 1 ≤ k ≤ 10^15, and nums is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func_1(n, k, nums):
    if (k >= sum(nums)) :
        return n
        #The program returns the number of integers 'n' in the list 'nums'
    #State: t is a positive integer, n and k are positive integers such that 1 ≤ n ≤ 2 * 10^5 and 1 ≤ k ≤ 10^15, and nums is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. Additionally, the sum of nums is greater than k.
    a, b = math.ceil(k / 2), k // 2
    ans = 0
    s_a = 0
    s_b = 0
    for i in range(n):
        s_a += nums[i]
        
        s_b += nums[n - i - 1]
        
        if s_a <= a:
            ans += 1
        
        if s_b <= b:
            ans += 1
        
    #State: Output State: `t` is a positive integer, `n` and `k` are positive integers such that 1 ≤ `n` ≤ 2 * 10^5 and 1 ≤ `k` ≤ 10^15, `nums` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 10^9, `a` is `math.ceil(k / 2)`, `b` is `k // 2`, `ans` is the sum of all indices `i` for which either the sum of the first `i+1` elements of `nums` is less than or equal to `a` or the sum of the last `i+1` elements of `nums` is less than or equal to `b`.
    return ans
    #The program returns the sum of all indices `i` for which either the sum of the first `i+1` elements of `nums` is less than or equal to `math.ceil(k / 2)` or the sum of the last `i+1` elements of `nums` is less than or equal to `k // 2`.
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `k`, and `nums`. `n` represents the number of integers in the list `nums`, `k` is a positive integer, and `nums` is a list of `n` integers where each integer is between 1 and 10^9 inclusive. The function returns either the number of integers `n` in the list `nums` or the count of indices `i` for which the sum of the first `i+1` elements of `nums` is less than or equal to `math.ceil(k / 2)` or the sum of the last `i+1` elements of `nums` is less than or equal to `k // 2`.

