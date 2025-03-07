#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, n and k are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 2 * 10^5, `k` is the remaining value after subtracting the sum of `nums[i]` for i from 1 to n-1, `nums` is a list of `n` integers where `nums[0]` is `(1 << k.bit_length() - 1) - 1` and the rest of the elements are `min(nums[0] + 1, k)` until `k` becomes 0, after which they are 0.
    nums[0] += k
    return nums
    #The program returns a list `nums` where the first element is `(1 << k.bit_length() - 1) - 1 + k` and the subsequent elements are `min(nums[0] + 1, k)` until `k` becomes 0, after which the remaining elements are 0.
#Overall this is what the function does:The function accepts two integer parameters, `n` and `k`. It returns a list `nums` of length `n` where the first element is `(1 << k.bit_length() - 1) - 1 + k`. The subsequent elements are the minimum of `nums[0] + 1` and the remaining value of `k` until `k` becomes 0, after which the remaining elements are 0.

