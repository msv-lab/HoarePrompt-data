#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are positive integers satisfying 2 <= n <= 10^6 and 1 <= k <= n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        nums = [(1 << i) for i in range(21)]
        
        idx = -1
        
        for i in range(len(nums)):
            if nums[i] > k:
                idx = i - 1
                break
        
        nums.append(k - nums[idx])
        
        nums.append(k + 1)
        
        nums.append(k + nums[idx] + 1)
        
        nums.remove(1 << idx)
        
        print(len(nums))
        
        print(*nums)
        
    #State: Output State: The loop will execute `t` times, where `t` is the number of test cases. After all iterations, `idx` will be set to the largest index `i` such that `1 << i` is less than or equal to the maximum `k` value encountered across all test cases. The list `nums` will contain the following elements:
    #
    #- All powers of 2 from \(2^0\) to \(2^{20}\).
    #- For each `k` value, the elements `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`.
    #- The length of `nums` will be `24 + t`, as we start with 21 elements (powers of 2) and add 3 elements per test case.
    #
    #The final state of `nums` will include all the unique elements added during the iterations, and the length of `nums` will reflect the total number of unique elements plus the initial 21 elements.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \(t\), \(n\), and \(k\). For each test case, it calculates specific values based on \(k\) and appends these values to a list `nums`. The list initially contains all powers of 2 from \(2^0\) to \(2^{20}\). For each \(k\), it adds \(k - \text{max power of 2} \leq k\), \(k + 1\), and \(k + \text{max power of 2} + 1\) to `nums`, then removes the largest power of 2 less than or equal to \(k\). After processing all test cases, the function prints the length of the final `nums` list and the list itself.

