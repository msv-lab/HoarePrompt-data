#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2⋅10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: After the loop executes all iterations, `i` will be equal to `n`, `k` will be less than or equal to 0, and `nums` will be a list where the first element `nums[0]` is equal to `(1 << (k.bit_length() - 1)) - 1`, and all other elements `nums[i]` (for `i` from 1 to `n-1`) will be equal to `min(nums[0] + 1, k)` as long as `k > 0`. If `k` becomes 0 or negative before the loop completes, the remaining elements in `nums` will be 0.
    nums[0] += k
    return nums
    #The program returns a list `nums` where the first element is `nums[0] + k`, and all other elements `nums[i]` (for `i` from 1 to `n-1`) are equal to `min(nums[0] + 1, k)`, with `k` being less than or equal to 0.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`. It initializes a list `nums` of size `n` with all elements set to 0. It then sets the first element `nums[0]` to `(1 << (k.bit_length() - 1)) - 1` and adjusts `k` accordingly. For each subsequent element in `nums`, it assigns the value of `min(nums[0] + 1, k)` while decrementing `k`. After the loop, if `k` is still positive, it adds the remaining value of `k` to `nums[0]`. Finally, it returns the list `nums` where the first element is `nums[0] + k`, and all other elements are `min(nums[0] + 1, k)`, with `k` guaranteed to be less than or equal to 0.

