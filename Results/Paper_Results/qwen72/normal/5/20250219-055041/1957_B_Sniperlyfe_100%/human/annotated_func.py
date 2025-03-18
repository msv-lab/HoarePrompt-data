#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: `n` is the same as the initial state, `k` is 0, and `nums` is a list of length `n` where the first element `nums[0]` is \(2^{\text{k.bit_length() - 1}} - 1\) and the subsequent elements are set to the minimum of the previous element plus 1 and the remaining value of `k` at each iteration until `k` becomes 0.
    nums[0] += k
    return nums
    #The program returns a list `nums` of length `n` where the first element is \(2^{\text{k.bit_length() - 1}} - 1 + k\) and the subsequent elements are set to the minimum of the previous element plus 1 and the remaining value of `k` at each iteration until `k` becomes 0.
#Overall this is what the function does:The function `func_1` accepts two integers, `n` and `k`, and returns a list `nums` of length `n`. The first element of the list is \(2^{\text{k.bit_length() - 1}} - 1\). Each subsequent element is the minimum of the previous element plus 1 and the remaining value of `k` at each iteration, until `k` becomes 0. If `k` is not fully used up by the end of the loop, the remaining value of `k` is added to the first element of the list. The final state of the program is that `nums` is a list of length `n` where the first element is \(2^{\text{k.bit_length() - 1}} - 1 + \text{remaining } k\) and the subsequent elements are set as described.

