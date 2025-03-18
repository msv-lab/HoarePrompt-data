#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, representing the number of containers. a is a list of n integers such that 0 ≤ a_i ≤ 10^9, representing the amounts of water in the containers. The sum of a_i is divisible by n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates `t` times, and for each iteration, it reads an integer `n` and a list of `n` integers `nums`. After processing, the variable `curr` is either 0 or a non-zero value, and the loop prints 'YES' if `curr` is 0, otherwise it prints 'NO'. The variables `t`, `n`, and `nums` are reset for each iteration, and the final state of these variables is undefined after the loop completes. The sum of `n` over all test cases does not exceed 2 · 10^5, and the sum of `a_i` is divisible by `n` for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves reading an integer `n` and a list of `n` integers `nums` representing the amounts of water in `n` containers. The function checks if the sum of the differences between each non-zero element in `nums` and the last element in `nums` is zero. If the sum is zero, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value, and the state of the variables `t`, `n`, and `nums` is undefined after the function completes.

