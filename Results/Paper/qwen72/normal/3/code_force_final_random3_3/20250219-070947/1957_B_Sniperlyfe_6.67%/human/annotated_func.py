#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^9.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: `n` is an integer such that 1 <= n <= 2 * 10^5, `i` is `n-1`, `nums` is a list of length `n` where all elements are initialized to `(1 << k.bit_length() - 1) - 1`, and `k` is now `k - n * ((1 << k.bit_length() - 1) - 1)`.
    nums[-1] += k
    return nums
    #The program returns a list `nums` of length `n` where all elements except the last one are initialized to `(1 << k.bit_length() - 1) - 1`, and the last element is `(1 << k.bit_length() - 1) - 1 + k`. The value of `k` is now `k - n * ((1 << k.bit_length() - 1) - 1)`.
#Overall this is what the function does:The function `func_1` accepts two integers `n` and `k`, and returns a list `nums` of length `n`. All elements in the list except the last one are set to `(1 << k.bit_length() - 1) - 1`, and the last element is set to `(1 << k.bit_length() - 1) - 1 + k`. The function modifies the value of `k` during its execution, but this change is not visible to the user as `k` is not returned.

