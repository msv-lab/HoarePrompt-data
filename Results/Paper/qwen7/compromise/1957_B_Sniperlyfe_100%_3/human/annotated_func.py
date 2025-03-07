#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2 ⋅ 10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` and `k` are integers for each test case such that 1 ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9, and the sum of all `n` over all test cases does not exceed 2 ⋅ 10^5; `nums` is a list of length `n` where `nums[0]` is (1 << (`k`'s bit length - 1)) - 1, and for all `i` from 1 to `n-1`, `nums[i]` is equal to `k` if `k > 0` and 1 otherwise, with `k` being 0 after the loop finishes.
    nums[0] += k
    return nums
    #The program returns a list `nums` of length `n` where `nums[0]` is (1 << (`k`'s bit length - 1)) - 1 + `k`. For all `i` from 1 to `n-1`, `nums[i]` is equal to `k` if `k > 0` and 1 otherwise, with `k` being 0 after the loop finishes.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`. It initializes a list `nums` of length `n` with all elements set to 0. It then calculates the first element `nums[0]` as `(1 << k's bit length - 1) - 1 + k`. For each subsequent element `nums[i]` (where `i` ranges from 1 to `n-1`), it sets the value to `k` if `k` is greater than 0, and 1 otherwise. After processing, it ensures `k` is set to 0. Finally, it returns the list `nums`.

