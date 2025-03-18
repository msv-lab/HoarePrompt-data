#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: `n` and `k` are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9; `nums` is a list of length `n` with all elements set to `(1 << k.bit_length() - 1) - 1`, and `k` is reduced by the sum of all elements in `nums`.
    nums[-1] += k
    return nums
    #The program returns a list `nums` of length `n` where all elements are `(1 << k.bit_length() - 1) - 1`, except the last element which is `(1 << k.bit_length() - 1) - 1 + k`. Since `k` is 0, all elements in the list are 0, and the last element is also 0. Therefore, the list `nums` is a list of `n` zeros.
#Overall this is what the function does:The function `func_1` accepts two integers `n` and `k`, and returns a list `nums` of length `n`. Each element in the list is initially set to `(1 << k.bit_length() - 1) - 1`, except the last element, which is adjusted to be `(1 << k.bit_length() - 1) - 1 + k` after the loop. The final state of the program is a list `nums` where all elements are `(1 << k.bit_length() - 1) - 1`, except the last element which is `(1 << k.bit_length() - 1) - 1 + k`. If `k` is 0, the function returns a list of `n` zeros.

