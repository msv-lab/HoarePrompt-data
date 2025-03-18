#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: 
    nums[-1] += k
    return nums
    #The program returns the list `nums` where the last element has been increased by `k`.
#Overall this is what the function does:The function generates a list `nums` of length `n` where each element is initialized to the maximum value that can be represented with the number of bits in `k`. It then increases the last element of `nums` by the remaining value of `k` after distributing the initial values. The function returns this modified list `nums`.

