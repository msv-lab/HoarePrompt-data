#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i ≤ 10^9. The sum of a_i is divisible by n, and the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The value of `t` is reduced by the number of iterations that have been completed, and `n` and `nums` are updated based on the input provided during each iteration. The variables `last` and `curr` are used within each iteration and reset at the start of each new iteration. The final output for each iteration is either 'YES' or 'NO' based on the condition `curr == 0`. The initial state of `a` remains unchanged as it is not modified within the loop.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of an integer `n` and a list of `n` integers `nums`. For each test case, it calculates the difference between each non-zero element in `nums` and the last element of `nums`, summing these differences. If the sum is zero, it prints 'YES'; otherwise, it prints 'NO'. The function processes `t` test cases, and after processing all test cases, the value of `t` is reduced to zero. The initial list `a` mentioned in the annotations is not used or modified by the function.

