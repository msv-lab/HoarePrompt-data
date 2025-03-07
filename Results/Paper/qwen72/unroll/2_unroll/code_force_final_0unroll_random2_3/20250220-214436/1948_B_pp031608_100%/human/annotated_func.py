#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, n is an integer such that 2 <= n <= 50, and a is a list of n integers where 0 <= a_i <= 99.
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
        
    #State: The value of `t` remains unchanged, `n` remains unchanged, and `a` remains unchanged. The loop reads `n` lines of input, each containing an integer `m` and a list of `m` integers `arr`. For each line, it checks if the list can be made non-decreasing by changing at most one element. If it can, it prints 'YES'; otherwise, it prints 'NO'.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads `n` lines of input, where `n` is an integer provided by the user. Each line contains an integer `m` followed by a list of `m` integers. For each list, the function checks if the list can be made non-decreasing by changing at most one element. If it can, the function prints 'YES'; otherwise, it prints 'NO'. The state of the program remains unchanged with respect to any external variables `t` and `a` that might have been present before the function call.

