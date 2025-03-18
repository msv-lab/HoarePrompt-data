#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: `nums` is a list of `n` integers where each integer is `(1 << k.bit_length() - 1) - 1`, and `k` is `k - n * ((1 << k.bit_length() - 1) - 1)`.
    nums[-1] += k
    return nums
    #The program returns a list `nums` containing `n` integers, where each integer except the last one is `(1 << k.bit_length() - 1) - 1`, and the last integer is `(1 << k.bit_length() - 1) - 1 + k`. The value of `k` is `k - n * ((1 << k.bit_length() - 1) - 1)`.
#Overall this is what the function does:The function `func_1` accepts two integers `n` and `k`, and returns a list `nums` of `n` integers. Each integer in the list, except the last one, is set to `(1 << k.bit_length() - 1) - 1`. The last integer in the list is set to `(1 << k.bit_length() - 1) - 1 + k`. After the function concludes, the value of `k` is reduced by `n * ((1 << k.bit_length() - 1) - 1)`.

