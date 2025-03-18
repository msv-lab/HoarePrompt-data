#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `k` are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9, but `k` will be reduced by the sum of the values assigned to `nums`; `nums` is a list of `n` elements where each element is the largest possible value with the same number of bits as `k` at the start of that iteration.
    nums[-1] += k
    return nums
    #The program returns a list `nums` where the first `n-1` elements are the largest possible value with the same number of bits as `k` (i.e., `2^b - 1`), and the last element is this value plus `k`.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, where `n` is the number of elements in the list to be returned and `k` is an integer. It returns a list `nums` of length `n` such that the first `n-1` elements are the largest possible value with the same number of bits as the initial `k` (i.e., `2^b - 1`), and the last element is this value plus the remaining `k` after reducing `k` by the sum of the first `n-1` elements.

