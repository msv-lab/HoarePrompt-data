#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2 ⋅ 10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: Output State: After the loop executes all iterations, `i` will be equal to `n`, `k` will be less than or equal to 0, and `nums` will contain `n` elements where the first element `nums[0]` is `(1 << (`k`.bit_length() - 1)) - 1`, and each subsequent element `nums[i]` (for `i` from 1 to `n-1`) will be `min(nums[0] + 1, k)` if `k` was still positive after the previous iterations, otherwise `nums[i]` will be 0.
    #
    #In simpler terms, after the loop completes, the index `i` will be equal to the length of the `nums` list (`n`), meaning the loop has processed all elements. The variable `k` will either be fully consumed (less than or equal to 0) or reduced to 0 during the last iteration if it couldn't be further decremented due to its value being smaller than `min(nums[0] + 1, k)`. The `nums` list will start with a specific value based on `k` and then each following element will be the minimum possible value `k` could take in each iteration, ensuring no further decrements are possible.
    nums[0] += k
    return nums
    #The program returns a list `nums` containing `n` elements. The first element `nums[0]` is `(1 << (k.bit_length() - 1)) - 1`, and each subsequent element `nums[i]` (for `i` from 1 to `n-1`) is `0` since `k` is non-positive.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is the number of elements in the list `nums` and `k` is an integer. It initializes a list `nums` of size `n` with all elements set to 0. The first element `nums[0]` is set to `(1 << (k.bit_length() - 1)) - 1`. If `k` is greater than 0 after processing the first element, subsequent elements in `nums` are set to the minimum possible value of `k` that can be subtracted, ensuring `k` becomes non-positive. Finally, any remaining value of `k` is added to `nums[0]`. The function returns the list `nums` with these properties.

