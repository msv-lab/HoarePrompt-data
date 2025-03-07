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
        
    #State: `t` is 0, `_` is a placeholder (not used), `n` is an input integer, `nums` is a list of integers provided by the user input, `last` is the last element of the `nums` list, and `curr` is the sum of the differences between each non-zero element in `nums` and the last element of `nums`. If `curr` is 0, the program prints 'YES'. If `curr` is not 0, the program prints 'NO'.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `nums` from user input. It then checks if the sum of the differences between each non-zero element in `nums` and the last element of `nums` is zero. If this sum is zero, the function prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function concludes, and the final state is that `t` is 0, `_` is a placeholder (not used), `n` is the last input integer, `nums` is the last list of integers provided by the user, `last` is the last element of the last `nums` list, and `curr` is the sum of the differences calculated for the last `nums` list.

