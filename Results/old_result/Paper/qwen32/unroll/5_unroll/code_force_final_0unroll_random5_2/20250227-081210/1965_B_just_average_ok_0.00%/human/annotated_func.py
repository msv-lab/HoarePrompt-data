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
        
    #State: For each test case, the output consists of two lines: the first line is the length of the modified `nums` list, and the second line contains the space-separated elements of the modified `nums` list. The initial state of `t` (number of test cases) and the values of `n` for each test case remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`. For each test case, it constructs and modifies a list of numbers based on the value of `k`, then outputs the length of the modified list followed by its elements. The initial values of `n` and `k` for each test case remain unchanged.

