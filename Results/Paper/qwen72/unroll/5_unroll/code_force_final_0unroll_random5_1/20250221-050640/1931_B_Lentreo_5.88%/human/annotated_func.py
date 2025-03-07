#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2·10^5, and a is a list of n integers where 0 ≤ a_i ≤ 10^9. The sum of a_i is divisible by n, and the sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: After all iterations of the loop, the value of `t` is 0, and the values of `n` and `a` remain unchanged for each test case. The variable `last` holds the last element of the list `nums` for the last test case, and `curr` holds the result of the computation for the last test case. The output for each test case is either 'YES' or 'NO' based on the condition `if curr == 0`.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of `n` integers `nums`. It then checks if the sum of the differences between each non-zero element in `nums` and the last element of `nums` is zero. If the sum is zero, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function does not return any value, but the output for each test case is either 'YES' or 'NO' based on the condition described. The variables `t`, `n`, and `nums` are used internally and are not returned or modified outside the function.

