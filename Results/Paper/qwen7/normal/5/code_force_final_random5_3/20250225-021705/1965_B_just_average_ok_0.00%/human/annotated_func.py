#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are positive integers satisfying 2 <= n <= 10^6 and 1 <= k <= n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        nums = [(1 << i) for i in range(24)]
        
        idx = 0
        
        while k >= 1 << idx:
            idx += 1
        
        idx -= 1
        
        nums.append(k - nums[idx])
        
        nums.append(k + 1)
        
        nums.append(k + nums[idx] + 1)
        
        nums.remove(1 << idx)
        
        print(len(nums))
        
        print(*nums)
        
    #State: Output State: The loop will continue to execute for each test case provided by the user until all test cases are processed. After all iterations of the loop have finished, `idx` will be equal to the highest power of 2 less than or equal to `k` for the last test case processed. `nums` will be a list containing integers from \(2^0\) to \(2^{\text{idx} - 1}\), with the following elements added based on the value of `k` for the last test case:
    #
    #- `k - 2^{\text{idx} - 1}`
    #- `k + 1`
    #- `k + 2^{\text{idx} - 1} + 1`
    #
    #Additionally, the element \(2^{\text{idx}}\) will be removed from `nums`. The length of `nums` will be \(\text{idx} + 3\).
    #
    #The loop will print the length of `nums` and then print the elements of `nums` in the order they appear in the list. This process will repeat for each test case, and once all test cases are processed, the final state of `nums` will reflect the last test case's `k` value and the corresponding `idx`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` (1 ≤ t ≤ 1000), and two positive integers `n` and `k` (2 ≤ n ≤ 10^6, 1 ≤ k ≤ n). For each test case, it calculates a list `nums` containing specific integers derived from `k` and prints the length of `nums` followed by its elements. After processing all test cases, the final state of `nums` reflects the last test case's `k` value and the corresponding `idx` (the highest power of 2 less than or equal to `k`).

