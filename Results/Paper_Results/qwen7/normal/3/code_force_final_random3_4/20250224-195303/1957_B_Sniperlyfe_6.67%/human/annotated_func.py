#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2 ⋅ 10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: Output State: All elements in the `nums` list are set to `(1 << k.bit_length() - 1) - 1`, and the variable `k` is reduced by the sum of all values assigned to `nums`.
    #
    #Explanation: The loop runs from `i = 0` to `i = n-1`. In each iteration, `nums[i]` is set to `(1 << k.bit_length() - 1) - 1`, which is the largest value that can be represented with `k.bit_length()` bits. This value is then subtracted from `k`. After `n` iterations, `k` will be reduced by the sum of `n` such values, and all elements in the `nums` list will be equal to `(1 << k.bit_length() - 1) - 1`.
    nums[-1] += k
    return nums
    #The program returns a list `nums` where each element is initially set to the value `(1 << (k.bit_length() - 1)) - 1`, then `k` is reduced by the sum of all values in `nums`, and finally, `nums[-1]` is incremented by the final value of `k`.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`. It initializes a list `nums` of length `n` where each element is set to the maximum value that can be represented with `k`'s bit length minus one. It then reduces `k` by the sum of all values in `nums` and increments the last element of `nums` by the final value of `k`. The function returns the modified list `nums`.

