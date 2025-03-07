#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each element a_i satisfies 0 <= a_i <= 10^9. The sum of a_i for each test case is divisible by n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has executed `t` times, and for each test case, it has read an integer `n`, a list of `n` integers `nums`, computed `last` as the last element of `nums`, and calculated `curr` as the sum of `(i - last)` for all non-zero elements `i` in `nums`. If `curr` is 0, it prints 'YES', otherwise it prints 'NO'. After all iterations, `t` is decremented to 0, and no further iterations occur.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it checks if the sum of the differences between each non-zero element and the last element of the list is zero. If this condition is met, it prints 'YES'; otherwise, it prints 'NO'.

