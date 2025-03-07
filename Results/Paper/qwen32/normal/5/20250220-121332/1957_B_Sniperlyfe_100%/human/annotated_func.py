#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: `t` remains the same, `n` remains the same, `k` is 0 if enough iterations reduce `k` to 0, otherwise `k` retains the remaining value, `nums[0]` is `(1 << k.bit_length() - 1) - 1`, and `nums[i]` for `i` from 1 to `n-1` are `min(nums[0] + 1, k)` until `k` becomes 0, after which they are 0.
    nums[0] += k
    return nums
    #The program returns a list `nums` where `nums[0]` is `(1 << k.bit_length() - 1) - 1 + k`, and `nums[i]` for `i` from 1 to `n-1` are `min(nums[0] + 1, k)` until `k` becomes 0, after which they are 0.
#Overall this is what the function does:The function `func_1` takes two parameters, `n` and `k`, and returns a list `nums` of length `n`. The first element `nums[0]` is calculated as `(1 << k.bit_length() - 1) - 1 + k`. Each subsequent element from `nums[1]` to `nums[n-1]` is the minimum of `nums[0] + 1` and the remaining value of `k`, with `k` being decremented by this value. Once `k` becomes 0, all remaining elements in the list are set to 0.

