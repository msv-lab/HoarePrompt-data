#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2⋅10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: Output State: `t` test cases, `n` and `k` are integers for each test case such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2⋅10^5; `nums` is a list of length `n` where each element is `k-1`, and `k` is reduced to 0 after all iterations.
    nums[-1] += k
    return nums
    #The program returns a list `nums` of length `n` where each element is `k-1`, and the last element is `2*k-1` with `k` being 0.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`. It initializes a list `nums` of length `n` where each element is set to `k-1`. After iterating through the list, it adjusts the last element to `2*k-1` and sets `k` to 0. The function then returns the list `nums`.

