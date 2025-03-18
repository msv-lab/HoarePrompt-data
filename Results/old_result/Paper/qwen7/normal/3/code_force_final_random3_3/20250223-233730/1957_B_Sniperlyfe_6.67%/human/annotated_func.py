#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2⋅10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: Output State: `i` is equal to `n`; `k` is equal to 0; `n` is a positive integer; `nums` is a list where every element from index 0 to `n-1` is set to `(1 << k.bit_length() - 1) - 1`, and `k` has been reduced to 0 after subtracting the necessary values for each iteration of the loop.
    #
    #This means that after the loop completes all its iterations, the variable `i` will be equal to the original value of `n`, indicating that the loop has executed `n` times. The variable `k` will be 0 because it has been fully decremented by the operations within the loop. The list `nums` will contain `n` elements, each set to `(1 << k.bit_length() - 1) - 1`, which simplifies to the highest power of 2 less than `k` when `k` was originally set, ensuring that `k` is reduced to 0 through these operations.
    nums[-1] += k
    return nums
    #The program returns a list `nums` where the first `n-1` elements are all set to `0`, and the last element is `0`.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`. It initializes a list `nums` of size `n` with all elements set to the highest power of 2 less than `k`. After setting the initial values, it ensures the last element of `nums` is adjusted to make `k` equal to 0. Finally, it returns a list `nums` where the first `n-1` elements are `0`, and the last element is `0`.

