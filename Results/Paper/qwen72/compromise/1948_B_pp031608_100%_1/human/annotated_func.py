#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, representing the number of test cases. Each test case consists of an integer n (2 <= n <= 50) and a list of n integers a_1, a_2, ..., a_n (0 <= a_i <= 99).
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
        
    #State: After all iterations of the loop, `t` remains an integer such that 1 <= t <= 10^3, `n` is 0, `_` has been incremented by `n` times (where `n` is the initial value of `n`), `m` is the last input integer read, `arr` is the last list of integers read from the input, and `ans` is either True or False depending on whether the conditions inside the loop were met for each test case. If any test case encountered a condition where `arr[i] < arr[i - 1]` and the resulting `nums` list was not sorted, `ans` is set to False for that test case. Otherwise, `ans` remains True for that test case.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case starts with an integer `n`, followed by a list of `n` integers. For each test case, the function checks if the list can be made non-decreasing by modifying at most one element. If it can, the function prints "YES"; otherwise, it prints "NO". After processing all test cases, the function terminates without returning any value.

