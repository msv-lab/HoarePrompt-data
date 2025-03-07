#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. Each test case consists of two lines: the first line contains a single integer n such that 2 ≤ n ≤ 50, and the second line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i ≤ 99.
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^3, `n` is an input integer such that 2 ≤ n ≤ 50, and for each iteration of the loop, `m` is an integer input, `arr` is a list of integers input as a space-separated string, and `ans` is a boolean value determined based on the conditions inside the loop. After all iterations, the output will be a list of "NO" or "YES" strings corresponding to the boolean values of `ans` for each iteration.
#Overall this is what the function does:The function processes a series of test cases where each test case consists of an integer \( n \) followed by \( n \) integers. It checks whether the sequence of integers can be made non-decreasing by swapping adjacent elements at most once. If such a sequence can be formed, it prints "YES"; otherwise, it prints "NO". The function reads input from standard input and prints output to standard output, handling up to 1000 test cases.

