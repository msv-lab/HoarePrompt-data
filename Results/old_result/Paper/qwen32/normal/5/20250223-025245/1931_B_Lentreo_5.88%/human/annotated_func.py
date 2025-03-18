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
        
    #State: After all iterations, `t` test cases have been processed. For each test case, "YES" is printed if the sum of differences `i - last` for all non-zero `i` in `nums` equals 0; otherwise, "NO" is printed. The variables `n`, `nums`, `last`, and `curr` will reflect the state of the last test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then determines if the sum of the differences between each non-zero element in the list and the last element equals zero. If it does, it prints "YES"; otherwise, it prints "NO".

