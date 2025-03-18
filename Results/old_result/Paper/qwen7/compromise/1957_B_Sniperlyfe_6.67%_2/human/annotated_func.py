#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2⋅10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: Output State: `t` test cases, `n` and `k` as specified, `nums` is a list of length `n` where each element is `2^k.bit_length() - 1`. After the loop executes, `k` is reduced by the value of `2^k.bit_length() - 1` for each iteration, but since `nums[i]` is assigned the same value in each iteration, `k` will eventually become less than `2^k.bit_length() - 1`, and the loop will stop when `k` is no longer positive. The final state of `nums` will be a list of `n` elements, each being the maximum possible value for the bit length of `k` before it became too small.
    nums[-1] += k
    return nums
    #The program returns a list `nums` of length `n`, where each element is `2^k - 1`, except for the last element which is `2^k - 1 + k
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`. It initializes a list `nums` of length `n` where each element is set to the maximum possible value for the bit length of `k` (i.e., `2^k - 1`). In the last iteration, if `k` is still positive, it adds the remaining value of `k` to the last element of `nums`. The function then returns this list `nums`.

