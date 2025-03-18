#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2 ⋅ 10^5.
def func_1(n, k):
    nums = [0] * n
    nums[0] = (1 << k.bit_length() - 1) - 1
    k -= nums[0]
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` and `k` are integers for each test case such that 1 ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2 ⋅ 10^5; `nums` is a list of n integers where `nums[0]` is (1 << (k.bit_length() - 1)) - 1, and for each `i` from 1 to `n-1`, `nums[i]` is the minimum value between `nums[0] + 1` and `k`, with `k` being decremented by `nums[i]` after each assignment.
    nums[0] += k
    return nums
    #The program returns a list `nums` where `nums[0]` is `k`, and for each `i` from 1 to `n-1`, `nums[i]` is the minimum value between `nums[0] + 1` and `k`. After each assignment, `k` is decremented by `nums[i]`
#Overall this is what the function does:The function accepts two parameters, `n` and `k`. It initializes a list `nums` of size `n` with all elements set to 0. Then, it sets the first element `nums[0]` to `(1 << k.bit_length() - 1) - 1` and adjusts `k` accordingly. For each subsequent element `nums[i]` (where `i` ranges from 1 to `n-1`), it assigns the minimum value between `nums[0] + 1` and `k` to `nums[i]` and decreases `k` by the assigned value. Finally, it ensures `nums[0]` is updated to the remaining value of `k`. The function returns the list `nums`.

