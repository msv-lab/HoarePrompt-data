#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, n is an integer such that 2 <= n <= 50, and a is a list of n integers where each integer a_i is in the range 0 <= a_i <= 99.
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
        
    #State: The value of `t` remains unchanged, `n` remains unchanged, and `a` remains unchanged. The loop prints 'YES' or 'NO' for each iteration based on the condition described in the loop. Specifically, for each iteration, if the list `arr` can be made non-decreasing by changing at most one element, the loop prints 'YES'; otherwise, it prints 'NO'.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `n` from the user input, which represents the number of test cases. For each test case, it reads another integer `m` and a list of `m` integers `arr`. The function then checks if the list `arr` can be made non-decreasing by changing at most one element. If it can, the function prints 'YES'; otherwise, it prints 'NO'. The function performs this check for each of the `n` test cases. The state of the program remains unchanged with respect to any external variables like `t` or `a` that might have been present before the function call.

