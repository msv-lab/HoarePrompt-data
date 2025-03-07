#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. The sum of n over all test cases does not exceed 10^7.
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
        
    #State: After all iterations, the program will have processed `t` test cases. For each test case, it will output the length of the modified list `nums` followed by the elements of `nums`. The list `nums` starts with the first 21 powers of 2 (from 2^0 to 2^20), then modifies this list based on the value of `k` by removing the largest power of 2 less than or equal to `k` and adding three new elements: `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`. For each test case, it constructs a list starting with the first 21 powers of 2, modifies this list by removing the largest power of 2 less than or equal to `k`, and adds three new elements: `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`. It then outputs the length of the modified list followed by its elements.

