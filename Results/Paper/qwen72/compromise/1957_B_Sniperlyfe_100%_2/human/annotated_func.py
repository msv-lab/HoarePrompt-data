#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: `nums` is a list of length `n` with the first element `nums[0]` set to \(2^{\text{k.bit_length()} - 1} - 1\) and the remaining elements filled with the minimum value between `nums[0] + 1` and the remaining `k` until `k` is exhausted. `k` is 0.
    nums[0] += k
    return nums
    #The program returns the list `nums` where the first element is \(2^{\text{k.bit_length()} - 1} - 1\) and the remaining elements are filled with the minimum value between `nums[0] + 1` and the remaining `k` until `k` is exhausted. Since `k` is 0, the remaining elements of `nums` are all 0.
#Overall this is what the function does:The function `func_1` accepts two integers `n` and `k` and returns a list `nums` of length `n`. The first element of `nums` is set to \(2^{\text{k.bit_length()} - 1} - 1\). The remaining elements of `nums` are filled with the minimum value between `nums[0] + 1` and the remaining `k` until `k` is exhausted. If `k` is 0 after the first element is set, the remaining elements of `nums` are all 0.

