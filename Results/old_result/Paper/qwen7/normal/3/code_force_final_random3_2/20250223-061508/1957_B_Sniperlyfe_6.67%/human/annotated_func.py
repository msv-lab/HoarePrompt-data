#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2 ⋅ 10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: Output State: After the loop executes all iterations, `n` will be 0, `k` will be 0, and `nums` will be a list where each element is `(1 << (k.bit_length() - 1)) - 1` for the indices where the loop executed, and 0 otherwise.
    #
    #To understand this, let's break it down:
    #
    #- The loop runs from `i = 0` to `i = n-1`.
    #- For each iteration, `nums[i]` is set to `(1 << k.bit_length() - 1) - 1`.
    #- Then, `k` is decreased by `nums[i]`.
    #
    #Since `k` starts as some positive value and is decreased by a value that depends on its bit length, eventually `k` will become 0 after enough iterations. When `k` reaches 0, the subtraction operation will no longer change `k`, and since `n` is decremented with each iteration, `n` will also reach 0.
    #
    #Each time through the loop, `nums[i]` is set to a value based on the current bit length of `k`. As `k` decreases, the bit length of `k` decreases, and thus the value of `nums[i]` will be adjusted accordingly. By the end of the loop, `nums` will contain the sequence of values that were assigned to it during the iterations, and `k` will be 0.
    nums[-1] += k
    return nums
    #The program returns a list `nums` where each element is `(1 << (k.bit_length() - 1)) - 1` for the indices where the loop executed, and 0 otherwise, and the last element of `nums` is 0.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is the number of elements in the list `nums` and `k` is an integer. It initializes a list `nums` of size `n` with zeros. For each index `i` from 0 to `n-1`, it sets `nums[i]` to a value derived from the bit length of `k`, specifically `(1 << (k.bit_length() - 1)) - 1`, and then decreases `k` by this value. After the loop, it adjusts the last element of `nums` by adding any remaining value of `k`. Finally, it returns the list `nums`. The returned list contains the sequence of values assigned to it during the iterations, with zeros in the positions not affected by the loop, and the last element set to zero.

