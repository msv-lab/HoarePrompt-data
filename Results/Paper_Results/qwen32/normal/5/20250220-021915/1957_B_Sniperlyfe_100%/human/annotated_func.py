#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer such that \(1 \leq n \leq 2 \cdot 10^5\), `k` is 0 if it was exhausted during the loop, otherwise it is the remaining value, and `nums` is a list where the first element is \((1 << k.bit_length() - 1) - 1\) and the subsequent elements are filled with the values `min(nums[0] + 1, k)` until `k` is 0, and the rest are 0.
    nums[0] += k
    return nums
    #The program returns a list `nums` where the first element is \((1 << k.bit_length() - 1) - 1 + k\), the subsequent elements are `min(nums[0] + 1, k)` until `k` is 0, and the rest are 0, making the total length of `nums` equal to `n`.
#Overall this is what the function does:The function takes two parameters, `n` and `k`, and returns a list `nums` of length `n`. The first element of `nums` is calculated as \((1 << k.bit_length() - 1) - 1 + k\). The subsequent elements are the minimum of `nums[0] + 1` and the remaining `k` until `k` is reduced to 0. The rest of the elements in the list are filled with 0.

