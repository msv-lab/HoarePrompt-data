#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of an integer n such that 1 <= n <= 2 * 10^5, followed by a list of n integers a_1, a_2, ..., a_n where 0 <= a_i <= 10^9. The sum of a_i for each test case is divisible by n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: A series of 'YES' or 'NO' printed for each test case, based on whether the condition `curr == 0` is met.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it checks if the sum of differences between each non-zero element and the last element of the list equals zero. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'.

