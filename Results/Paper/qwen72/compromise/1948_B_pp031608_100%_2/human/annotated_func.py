#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, representing the number of test cases. Each test case consists of an integer n such that 2 <= n <= 50, and a list of n integers a_1, a_2, ..., a_n where 0 <= a_i <= 99.
def func():
    n = int(input())
    for _ in range(n):
        m = int(input())
        
        arr = [int(i) for i in input().split()]
        
        ans = True
        
        for i in range(m - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                nums = [int(i) for i in str(arr[i - 1])] + [arr[i]]
                if nums != sorted(nums):
                    ans = False
                    break
                arr[i - 1] = nums[0]
        
        print(['NO', 'YES'][ans])
        
    #State: `t` is an integer such that 1 <= t <= 10^3, `n` is an input integer such that 2 <= n <= 50, `m` is an input integer such that m >= 2, `_` is a placeholder, `arr` is a list of integers derived from the input, `i` is 0, and `ans` is either True or False depending on whether the condition `arr[i] < arr[i - 1]` and the subsequent checks were met during the loop execution. If any iteration found `arr[i] < arr[i - 1]` and the resulting `nums` was not sorted, `ans` is set to False. Otherwise, `ans` remains True. The elements of `arr` may have been modified based on the conditions within the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it checks if the list can be made non-decreasing by modifying at most one element according to specific rules. If the list can be made non-decreasing, it prints "YES"; otherwise, it prints "NO". The function processes up to 1000 test cases, with each list having between 2 and 50 elements. After processing all test cases, the function terminates.

