#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n. The sum of n over all test cases does not exceed 10^7.
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
        
    #State: For each test case, the output will be the length of the modified `nums` list followed by the elements of the modified `nums` list. The value of `t` remains unchanged, and it represents the number of test cases processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes two integers `n` and `k` as input, constructs a list of specific values based on `k`, and outputs the length of this list followed by the list's elements. The number of test cases is determined by the input integer `t`.

