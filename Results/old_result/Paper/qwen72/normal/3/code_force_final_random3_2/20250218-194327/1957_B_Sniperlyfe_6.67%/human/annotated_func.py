#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: `i` is `n-1`, `n` remains unchanged, `k` is now `k - n * ((1 << (k.bit_length() - 1)) - 1)`, `nums` is a list of `n` elements where each element is `(1 << (k.bit_length() - 1)) - 1`.
    nums[-1] += k
    return nums
    #The program returns a list `nums` of `n` elements where each element is `(1 << (k.bit_length() - 1)) - 1`, except the last element, which is `(1 << (k.bit_length() - 1)) - 1 + k`.
#Overall this is what the function does:The function `func_1` accepts two integers `n` and `k`, and returns a list `nums` of `n` elements. Each element in the list, except the last one, is set to `(1 << (k.bit_length() - 1)) - 1`. The last element is set to `(1 << (k.bit_length() - 1)) - 1 + k`. The value of `n` remains unchanged, and `k` is modified during the function execution but its final state is not relevant to the user.

