#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. The sum of n over all test cases does not exceed 10^7.
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
        
    #State: the length of the modified `nums` list and the elements of `nums` after the last test case is processed.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it performs a series of operations to modify a list of numbers based on the value of `k`, and then outputs the length of the modified list followed by the elements of the list.

