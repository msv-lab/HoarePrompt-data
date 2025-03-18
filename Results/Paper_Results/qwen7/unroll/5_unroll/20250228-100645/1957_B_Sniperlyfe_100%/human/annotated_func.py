#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2⋅10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` and `k` are integers for each test case such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2⋅10^5; `nums` is a list of length `n` where `nums[0]` is equal to ((1 << (`k`'s bit length)) - 1) - 1 and all other elements `nums[i]` (for i from 1 to n-1) are equal to the minimum of `nums[0] + 1` and `k`, with `k` being reduced accordingly by the value of `nums[i]` during each iteration.
    nums[0] += k
    return nums
    #The program returns a list `nums` of length `n` where the first element `nums[0]` is equal to `nums[0] + k` and all other elements `nums[i]` (for i from 1 to n-1) are equal to the minimum of `nums[0] + 1` and `k`, with `k` being reduced accordingly by the value of `nums[i]` during each iteration.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 1 and 10^4 inclusive, and `k` is an integer between 1 and 10^9 inclusive. It returns a list `nums` of length `n`. The first element `nums[0]` is set to `nums[0] + k`, and all other elements `nums[i]` (for i from 1 to n-1) are set to the minimum of `nums[0] + 1` and `k`, with `k` being decremented by the value of `nums[i]` during each iteration.

