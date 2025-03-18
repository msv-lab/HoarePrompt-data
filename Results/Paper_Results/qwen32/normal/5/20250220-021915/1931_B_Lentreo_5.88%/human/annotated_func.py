#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i <= 10^9. The sum of a_i for each test case is divisible by n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has executed `t` times. For each test case, `curr` is the sum of `i - last` for all non-zero `i` in `nums`, where `last` is the last element of `nums`. If `curr` is 0, the program prints 'YES'; otherwise, it prints 'NO'. The variables `t`, `n`, and `nums` remain unchanged throughout the loop except within the scope of each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then checks if the sum of the differences between each non-zero element in the list and the last element of the list equals zero. If this condition is met, it prints 'YES'; otherwise, it prints 'NO'.

