#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n and k are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` and `k` are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^9; `nums` is a list of `n` elements where each element is `(1 << k.bit_length() - 1) - 1`; `k` is `k - n * ((1 << k.bit_length() - 1) - 1)`
    nums[-1] += k
    return nums
    #The program returns a list `nums` where the first `n-1` elements are `(1 << k.bit_length() - 1) - 1` and the last element is `(1 << k.bit_length() - 1) - 1 + k`.
#Overall this is what the function does:The function takes two integers, `n` and `k`, and returns a list `nums` of length `n`. The first `n-1` elements of `nums` are all equal to `(1 << k.bit_length() - 1) - 1`, and the last element is `(1 << k.bit_length() - 1) - 1 + k`.

