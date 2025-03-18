#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2⋅10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: After all iterations of the loop, `i` will be equal to `n`, `k` will be less than or equal to 0, and every element from `nums[1]` to `nums[n-1]` will be set to `min(nums[0] + 1, k)` as long as `k` was greater than 0 during the iterations.
    nums[0] += k
    return nums
    #The program returns a list `nums` where `nums[0]` is equal to its original value plus `k`, and every element from `nums[1]` to `nums[n-1]` is set to `min(nums[0] + 1, k)` if `k` was greater than 0 during the iterations. Additionally, `i` is equal to `n` and `k` is less than or equal to 0.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`. It initializes a list `nums` of size `n` with all elements set to 0. Then, it sets the first element `nums[0]` to a specific value based on `k`. After that, it iterates through the list, setting each subsequent element to the minimum of `nums[0] + 1` and the remaining value of `k`, until `k` is no longer positive. Finally, it adjusts `nums[0]` by adding any remaining value of `k`. The function returns the modified list `nums`, ensuring that `i` is set to `n` and `k` is less than or equal to 0.

