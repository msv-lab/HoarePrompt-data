#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element is greater than 0 (1 <= c_i <= 10^9). For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5. The sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` and `q` are integers read from input such that 1 <= n, q <= 3 * 10^5; `c` is a list of `n` integers where each element is greater than 0 (1 <= c_i <= 10^9); `nums` is a list of integers read from input; `ones` is a list of `n + 1` integers where `ones[i]` is the count of 1s in `nums` from index 0 to `i-1` for all i from 1 to n; `sum` is a list of `n + 1` integers where `sum[i]` is the cumulative sum of `nums` from index 0 to `i-1`, with each element decremented by 1.
    for _ in range(q):
        l, r = map(int, input().split(' '))
        
        if l == r:
            print('NO')
            continue
        
        onesInRange = ones[r] - ones[l - 1]
        
        sumInRange = sum[r] - sum[l - 1]
        
        if 2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange:
            print('YES')
        else:
            print('NO')
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` and `q` are integers where 1 <= n, q <= 3 * 10^5; `c` is a list of `n` integers where each element is greater than 0 (1 <= c_i <= 10^9); `nums` is a list of integers; `ones` is a list of `n + 1` integers where `ones[i]` is the count of 1s in `nums` from index 0 to `i-1` for all i from 1 to n; `sum` is a list of `n + 1` integers where `sum[i]` is the cumulative sum of `nums` from index 0 to `i-1`, with each element decremented by 1.
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers `nums`. It also reads `q` queries, each consisting of a range `[l, r]`. For each query, the function determines whether a specific condition is met based on the count of 1s and the sum of elements in the specified range `[l, r]` of `nums`, and prints 'YES' or 'NO' accordingly.

