#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. Each of the next t lines contains two integers n and k such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. The sum of n over all test cases does not exceed 10^7.
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
        
    #State: After all iterations, the loop will have processed `t` test cases. For each test case, it reads integers `n` and `k`. It constructs a list `nums` initially containing powers of 2 up to \(2^{20}\). It then finds the largest power of 2 in `nums` that is less than or equal to `k` (or sets `idx` to -1 if `k` is greater than \(2^{20}\)). It modifies `nums` by removing this power of 2 and appending three new elements: `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`. Finally, it prints the length of the modified `nums` list followed by its elements. This process repeats for all `t` test cases.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it constructs a list of numbers starting with powers of 2 up to \(2^{20}\), modifies this list based on the value of `k`, and then prints the length of the modified list followed by its elements.

