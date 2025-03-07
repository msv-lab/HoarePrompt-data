#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        
        k -= nums[i]
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` and `k` are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9 (reduced by the sum of the largest numbers representable with `k.bit_length() - 1` bits for each iteration), and `nums` is a list of `n` elements, each being the largest number representable with `k.bit_length() - 1` bits at the time of its assignment.
    nums[-1] += k
    return nums
    #The program returns a list `nums` containing `n` elements, where each element except the last one is the largest number representable with `k.bit_length() - 1` bits, and the last element is the largest number representable with `k.bit_length() - 1` bits plus `k`.
#Overall this is what the function does:The function takes two parameters, `n` and `k`. It returns a list `nums` of `n` elements, where each element except the last one is the largest number that can be represented with `k.bit_length() - 1` bits, and the last element is this largest number plus the remaining value of `k` after distributing the largest numbers to the first `n-1` elements.

