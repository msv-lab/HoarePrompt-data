#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i ≤ 10^9. The sum of a_i is divisible by n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().strip().split()))
        
        last = nums[-1]
        
        curr = 0
        
        for i in nums:
            if i != 0:
                curr += i - last
        
        if curr == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The loop iterates `t` times, and for each iteration, it reads an integer `n` and a list of `n` integers `nums`. After processing, it prints 'YES' if the sum of the differences between each non-zero element in `nums` and the last element in `nums` is zero, otherwise it prints 'NO'. The variables `t`, `n`, and `a` remain unchanged outside of the loop, but `n` and `nums` are redefined within each iteration.
#Overall this is what the function does:The function reads `t` test cases, where for each test case, it reads an integer `n` and a list of `n` integers `nums`. It then calculates the sum of the differences between each non-zero element in `nums` and the last element in `nums`. If this sum is zero, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any values, and the variables `t`, `n`, and `a` (if they exist) are not modified outside of the function.

