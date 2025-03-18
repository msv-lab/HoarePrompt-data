#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and k = 0, and nums is a list of length n where nums[0] is (1 << k.bit_length() - 1) - 1 and the subsequent elements are filled with the remaining k values until k becomes 0.
    nums[0] += k
    return nums
    #The program returns the list `nums` where `nums[0]` is 0 and all subsequent elements are 0 since `k` is 0.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is the length of the list to be returned and `k` is a non-negative integer. The function returns a list `nums` of length `n` where the first element `nums[0]` is the largest power of 2 less than or equal to `k`, and the remaining elements are filled with the remaining value of `k` distributed such that no element exceeds the value of the first element plus one. After distributing `k`, any remaining value is added to `nums[0]`.

