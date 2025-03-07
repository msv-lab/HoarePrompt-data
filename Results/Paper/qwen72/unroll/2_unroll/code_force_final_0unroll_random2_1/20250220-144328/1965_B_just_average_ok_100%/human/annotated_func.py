#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: The loop modifies the `nums` list by appending three new elements and removing one element in each iteration. The length of the `nums` list after each iteration will be 23, and the elements of the `nums` list will be the original list with the new elements added and the removed element taken out. The variables `n` and `k` will retain their values from the input for each iteration, but their final values will be the last values read from the input.
#Overall this is what the function does:The function `func` reads an integer from the input, indicating the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `2 <= n <= 10^6` and `1 <= k <= n`. It then modifies a list `nums` by appending three new elements and removing one element. Specifically, it appends `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1` to the list, and removes the element `1 << idx`, where `idx` is the largest index such that `nums[idx] <= k`. The function prints the length of the modified `nums` list and the elements of the list. After each iteration, the length of `nums` is 23, and the variables `n` and `k` retain their values from the input for that iteration. The function does not return any value.

