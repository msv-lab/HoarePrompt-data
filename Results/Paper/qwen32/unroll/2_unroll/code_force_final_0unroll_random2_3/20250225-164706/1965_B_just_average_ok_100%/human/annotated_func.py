#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n. The sum of n over all test cases does not exceed 10^7.
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
        
    #State: For each test case, the length of the modified list `nums` followed by the elements of the modified list `nums`. The value of `t` remains unchanged.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it constructs a list of numbers based on the value of `k`, modifies this list by adding and removing specific elements, and then outputs the length of the modified list followed by its elements. The value of `t` remains unchanged throughout the execution.

