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
        
    #State: Output State: The loop will execute for each test case provided by the user. After all iterations, `idx` will be set to the index where `2^idx` is just greater than `k` for the last test case processed. The `nums` list will contain specific elements derived from `k` and the largest power of 2 less than or equal to `k`. Specifically, `nums` will include `[2, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 1048577, k + nums[idx] + 1]` for the last test case. The length of `nums` will be printed for each test case, and the final list `nums` will be printed out after all test cases have been processed. The variable `t` will remain unchanged as it was in the initial state, and `n` and `k` will retain their values from the last test case processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it calculates a list of specific numbers derived from \( k \) and the largest power of 2 less than or equal to \( k \). It then prints the length of this list followed by the list itself. After processing all test cases, the function outputs the final state of the list and its length. The function does not return any value but modifies and prints a list for each test case.

