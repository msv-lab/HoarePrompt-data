#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` and `k` are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9, and `nums` is a list of `n` integers where the first few elements are `min(nums[0] + 1, k)` and the rest are zeros; `k` is 0.
    nums[0] += k
    return nums
    #The program returns a list `nums` of `n` integers where the first element is `min(nums[0], 0)` and the rest are zeros.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, where `n` is the number of integers in the list and `k` is an integer. It returns a list `nums` of `n` integers where the first element is the maximum value that can be represented with the number of bits equal to the bit length of `k`, minus one, plus any remaining `k` after distributing values to subsequent elements, and the rest of the elements are as large as possible up to that value or zero if `k` is exhausted.

