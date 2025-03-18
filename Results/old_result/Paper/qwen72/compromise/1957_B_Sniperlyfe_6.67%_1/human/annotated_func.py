#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: `n` and `k` are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9; `nums` is a list of length `n` where each element is `(1 << k.bit_length() - 1) - 1`, and `k` is `k - n * ((1 << k.bit_length() - 1) - 1)`.
    nums[-1] += k
    return nums
    #The program returns a list `nums` of length `n` where each element, except the last one, is `(1 << k.bit_length() - 1) - 1`, and the last element is `(1 << k.bit_length() - 1) - 1 + k`.
#Overall this is what the function does:The function `func_1` accepts two integers `n` and `k` and returns a list `nums` of length `n`. Each element in the list, except the last one, is set to the value `(1 << (k.bit_length() - 1)) - 1`. The last element in the list is set to `(1 << (k.bit_length() - 1)) - 1 + k`. The function modifies the value of `k` during its execution, but the final state of `k` is not relevant to the user as it is not returned.

