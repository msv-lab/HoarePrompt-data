#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: `nums` is a list where `nums[0]` is `2^(k.bit_length()) - 1` and the subsequent elements are either `nums[0] + 1` or the remaining `k` if `k` is smaller than `nums[0] + 1`, and `k` is reduced to the remaining value after filling `nums`.
    nums[0] += k
    return nums
    #The program returns the list `nums` where the first element is `2^(k.bit_length()) - 1 + k` and the subsequent elements are either `nums[0] + 1` or the remaining `k` if `k` is smaller than `nums[0] + 1`.
#Overall this is what the function does:The function `func_1` takes two parameters, `n` and `k`. It returns a list `nums` of length `n` where the first element is `2^(k.bit_length()) - 1 + k`, and the subsequent elements are either `nums[0] + 1` or the remaining `k` if `k` is smaller than `nums[0] + 1`.

