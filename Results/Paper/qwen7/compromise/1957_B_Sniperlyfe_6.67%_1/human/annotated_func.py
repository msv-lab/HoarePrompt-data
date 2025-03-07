#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2 ⋅ 10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` and `k` are integers for each test case such that 1 ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9, and the sum of all `n` over all test cases does not exceed 2 ⋅ 10^5; `nums` is a list of length `n` where each element is `k-1`, and `k` is less than or equal to 0.
    #
    #Explanation: In each iteration of the loop, `nums[i]` is assigned the value `(1 << k.bit_length() - 1) - 1`, which is `k-1` if `k` is a positive power of 2, otherwise it's the largest number with all bits set to 1 that fits within the bit length of `k`. Then `k` is decreased by the value of `nums[i]`. Since `nums[i]` is always `k-1`, `k` will eventually become less than or equal to 0 after at most `k` iterations. Thus, after the loop, each element in `nums` will be `k-1`, and `k` will be less than or equal to 0.
    nums[-1] += k
    return nums
    #The program returns a list `nums` of length `n` where each element is `k-1`, and the last element is also `k-1` with `k` being less than or equal to 0.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, both integers. It initializes a list `nums` of length `n` where each element is set to `k-1`. After the loop, the last element of `nums` is adjusted by adding any remaining value of `k` (which is guaranteed to be less than or equal to 0). The function then returns the list `nums`.

