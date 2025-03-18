#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i ≤ 10^9. The sum of a_i is divisible by n, and the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates t times, and for each iteration, it reads an integer n and a list of n integers (nums). It then calculates the difference between each non-zero element in nums and the last element in nums, accumulating these differences in curr. If curr is 0 after the inner loop, it prints 'YES'; otherwise, it prints 'NO'. The values of t, n, and a remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 ≤ t ≤ 10^4`. For each of the `t` test cases, it reads an integer `n` and a list of `n` integers `nums` from the input, where `1 ≤ n ≤ 2 · 10^5` and `0 ≤ nums[i] ≤ 10^9`. The function then checks if the sum of the differences between each non-zero element in `nums` and the last element in `nums` is zero. If the sum is zero, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. After the function concludes, the values of `t`, `n`, and `nums` are no longer accessible as they are local to the function.

