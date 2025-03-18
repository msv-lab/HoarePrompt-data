#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: For each test case, the loop modifies the list `nums` by removing the element `1 << idx` and adding three new elements: `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`. The length of `nums` will be 24, and the elements will be the original elements of `nums` (excluding the removed one), plus the three new elements. The variables `t`, `n`, and `k` remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` indicating the number of test cases, and for each test case, it reads two integers `n` and `k`. The function then modifies a list `nums` which initially contains powers of 2 from 1 to 2^20. It removes one element from `nums` and adds three new elements based on the value of `k`. Finally, it prints the length of the modified `nums` list and the elements of the list. The variables `t`, `n`, and `k` remain unchanged after the function execution.

