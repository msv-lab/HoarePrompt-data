#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: After all iterations, `_` is a placeholder, `n` and `k` are the final input values for the last test case, `nums` is a list of integers from 1 to 1048576 (powers of 2 from \(2^0\) to \(2^{20}\)) with three additional elements: `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`, but without the element `1 << idx`. The variable `i` is the index of the first element in `nums` that is greater than `k` or `len(nums)` if no such element exists, and `idx` is `i - 1` if `i` is less than `len(nums)`, otherwise `idx` remains -1.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes two integers `n` and `k` as input. It then constructs a list `nums` initially containing powers of 2 up to \(2^{20}\). The function modifies this list by adding three specific elements (`k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`) and removing one element (`1 << idx`). Finally, it prints the length of the modified list followed by the elements of the list. The function does not return any value; its primary action is to print the results for each test case.

