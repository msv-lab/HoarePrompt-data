#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: `nums` is a list of length `n` where the first element is `2^(k.bit_length() - 1) - 1` and the remaining elements are `min(2^(k.bit_length() - 1), k)`. `k` is now `0`.
    nums[0] += k
    return nums
    #The program returns a list `nums` of length `n` where the first element is `0` and the remaining elements are `0`.
#Overall this is what the function does:The function `func_1` accepts two integers `n` and `k`, and returns a list `nums` of length `n`. The first element of `nums` is set to `2^(k.bit_length() - 1) - 1`, and the remaining elements are set to the minimum of `2^(k.bit_length() - 1)` and the remaining value of `k`, ensuring that the sum of all elements in `nums` equals the initial value of `k`. After the function concludes, `k` is reduced to `0` and the list `nums` is returned.

