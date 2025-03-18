#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^9.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: `nums` is a list of length `n` where `nums[0]` is \(2^{\text{k.bit_length()} - 1} - 1\) and for each `i` from 1 to `n-1`, `nums[i]` is the minimum of \(2^{\text{k.bit_length()} - 1}\) and the remaining value of `k` at the start of each iteration, and `k` is 0.
    nums[0] += k
    return nums
    #The program returns the list `nums` where the first element is \(2^{\text{k.bit_length()} - 1} - 1\) and each subsequent element is the minimum of \(2^{\text{k.bit_length()} - 1}\) and the remaining value of `k` at the start of each iteration, with `k` being 0.
#Overall this is what the function does:The function `func_1` accepts two integers `n` and `k`, where `1 <= n <= 2 * 10^5` and `1 <= k <= 10^9`. It returns a list `nums` of length `n` where the first element is \(2^{\text{k.bit_length()} - 1} - 1\), and each subsequent element is the minimum of \(2^{\text{k.bit_length()} - 1}\) and the remaining value of `k` at the start of each iteration. After the function concludes, the value of `k` is 0, and the list `nums` contains the computed values.

