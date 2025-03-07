#State of the program right berfore the function call: t is a positive integer, n is a positive integer not exceeding 2 * 10^5, k is a non-negative integer not exceeding 10^15, and nums is a list of n integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, k, nums):
    if (k >= sum(nums)) :
        return n
        #The program returns the value of n, which is a positive integer not exceeding 2 * 10^5.
    #State: t is a positive integer, n is a positive integer not exceeding 2 * 10^5, k is a non-negative integer not exceeding 10^15, and nums is a list of n integers where each integer is between 1 and 10^9 inclusive. The sum of nums is greater than k.
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
        
    #State: Output State: `t` is a positive integer, `n` is a positive integer not exceeding 2 * 10^5, `k` is a non-negative integer not exceeding 10^15, `nums` is a list of n integers where each integer is between 1 and 10^9 inclusive, `a` is the ceiling value of `k / 2`, `b` is the floor value of `k // 2`, `ans` is the count of indices `i` (where `0 <= i < n`) such that the sum of the first `i+1` elements in `nums` is less than or equal to `a` or the sum of the last `i+1` elements in `nums` is less than or equal to `b`, `s_b` is the sum of the last `n` elements of `nums`.
    return ans
    #The program returns the count of indices `i` (where `0 <= i < n`) such that the sum of the first `i+1` elements in `nums` is less than or equal to `a` or the sum of the last `i+1` elements in `nums` is less than or equal to `b`, where `a` is the ceiling value of `k / 2`, and `b` is the floor value of `k // 2`.
#Overall this is what the function does:The function accepts three parameters: `n`, a positive integer not exceeding 2 * 10^5; `k`, a non-negative integer not exceeding 10^15; and `nums`, a list of `n` integers where each integer is between 1 and 10^9 inclusive. It returns either the value of `n` or the count of indices `i` (where `0 <= i < n`) such that the sum of the first `i+1` elements in `nums` is less than or equal to `a` or the sum of the last `i+1` elements in `nums` is less than or equal to `b`, where `a` is the ceiling value of `k / 2`, and `b` is the floor value of `k // 2`.

