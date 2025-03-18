#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^3. Each test case consists of two lines: the first line contains a single integer n such that 2 <= n <= 50, and the second line contains n integers a_1, a_2, ..., a_n such that 0 <= a_i <= 99.
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
        
    #State: Output State: t is a positive integer such that 1 <= t <= 10^3, n is an input integer where 2 <= n <= 50, each iteration of the loop processes a list `arr` of integers `m` (where 1 <= m), and determines if the list can be transformed by swapping adjacent elements to make the first element of each pair non-decreasing, printing 'YES' if possible or 'NO' otherwise after all iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer n followed by n integers. For each test case, it checks if the list of integers can be transformed by swapping adjacent elements to ensure the first element of each pair is non-decreasing. If possible, it prints 'YES'; otherwise, it prints 'NO'. The function iterates through all test cases and outputs the result for each one.

