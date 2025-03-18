#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. Each test case consists of two lines: the first line contains a single integer n such that 2 ≤ n ≤ 50, and the second line contains n integers a_1, a_2, …, a_n such that 0 ≤ a_i ≤ 99.
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
        
    #State: Output State: `ans` is `False`, `i` is `0`, `m` is an integer such that `1 ≤ m ≤ n`, and `arr` is a list of integers obtained from the input after all iterations of the loop have completed.
    #
    #Explanation: After the loop has executed all its iterations, the value of `i` will be decremented until it reaches 0. The loop continues to run for each value of `m` from `n` down to 1. If at any point during these iterations, the condition `arr[i] < arr[i - 1]` is met and the concatenated number is not sorted, `ans` is set to `False` and the loop breaks. Given the provided conditions, `ans` remains `False` throughout all iterations unless the condition is never met, which is not specified in the problem statement. Therefore, after all iterations, `i` will be 0, `ans` will be `False`, and `m` will be the smallest value it was set to during the loop, which is at least 1 and at most `n`. The value of `arr[i-1]` will be the first digit of the number formed by concatenating `arr[i-1]` and `arr[i]` if the condition was met, but since `ans` is `False`, this condition was not met for any `i`, so `arr[i-1]` retains its value from the last iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( n \) (2 ≤ \( n \) ≤ 50) followed by \( n \) integers \( a_1, a_2, \ldots, a_n \) (0 ≤ \( a_i \) ≤ 99). For each test case, it checks if the sequence can be made non-decreasing by swapping adjacent elements only once. If such a swap is possible, it prints "YES"; otherwise, it prints "NO". The function does not return a value but prints the result for each test case.

